#!/usr/bin/env python

import os.path
import os
import tornado.ioloop
import tornado.web
import tornado.httpclient
from tornado.options import define, options, parse_command_line
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from geoalchemy2 import Geography, WKTElement

import models
from models import TransitStop, MuniStop

define("port", default=8080, help="Set listener port", type=int)
define("radius", default=321.868, help="Set stop search radius in meters", type=float)
define("postgres_url", default='postgresql://localhost/departure_times', help="url for postgres instance", type=str)


class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.render('index.html')

class MigrateHandler(tornado.web.RequestHandler):
  @tornado.gen.coroutine
  def get(self):
    http = tornado.httpclient.AsyncHTTPClient()
    response = yield http.fetch(MuniStop.fetch_stop_data_url())
    session = self.application.Session()
    MuniStop.add_stops(session, response.body.strip())
    session.commit()
    self.write('complete')

class RealtimeDepartureHandler(tornado.web.RequestHandler):
  @tornado.gen.coroutine
  def get(self):
    """
    Departure Estimates

    The time predicted for departure of nearby transit stops. 
     
    Query Parameters
    =================

    Name             |   Type      |    Description
    ---------------------------------------------------------
    longitude        |   float     |   Longitude component of location
    latitude         |   float     |   Latitude component of location
    radius(optional) |   float     |   Search radius size in meters 
    
    Sample Request
    =============

    GET /predictions?lat=37.7538790&long=-122.4349690

    Response
    ============

    Status-Code: 200 OK

    ```
{
  nearby_departures: [
    {
      route_name: "24-Divisadero",
      longitude: -122.4346199,
      directions: [
        {
          direction_name: "Outbound to the Bayview District",
          predictions: [
            3,
            8,
            21,
            27,
            37
          ]
        }
      ],
      latitude: 37.7560999,
      stop_name: "Castro St & 21st St"
    },
    {
      route_name: "24-Divisadero",
      longitude: -122.43448,
      directions: [
        {
          direction_name: "Outbound to the Bayview District",
          predictions: [
              3,
              9,
              21,
              27,
              38
          ]
        }
      ],
      latitude: 37.75464,
      stop_name: "Castro St & 22nd St"
    },
    {
      route_name: "24-Divisadero",
      longitude: -122.4343199,
      directions: [
        {
          direction_name: "Outbound to the Bayview District",
          predictions: [
              4,
              9,
              22,
              28,
              39
          ]
        }
      ],
      latitude: 37.7528999,
      stop_name: "Castro St & 23rd St"
    }
  ]
}
    ```
     Name            |   Type        |    Description
    ---------------------------------------------------------
    longitude        |   float       |   Longitude component of location
    latitude         |   float       |   Latitude component of location
    stop_name        |   string      |   Human-readable name of the stop
    route_name       |   string      |   Human-readable name of the route
    direction_name   |   string      |   Human-readable name of the route direction
    predictions      |  array of int |   List of prediction times in minutes 

    """
    session = self.application.Session()
    point_string = 'POINT(%s %s)' % (self.get_argument('longitude'),self.get_argument('latitude'))
    radius = self.get_argument('radius',options.radius)

    #extracting along with lat-longs to prevent n+1 query load on the DB
    query = session.query(TransitStop,func.ST_X(func.ST_AsText(TransitStop.stop_location)).label('longitude'),
                          func.ST_Y(func.ST_AsText(TransitStop.stop_location)).label('latitude'))\
            .filter(func.ST_DWithin(TransitStop.stop_location, point_string, radius))
    
    stop_locations = {}
    stops = []
    for stop in query:
      # pull object out of result
      stops.append(stop[0])
      stop[0].longitude = stop[1]
      stop[0].latitude = stop[2]
    http = tornado.httpclient.AsyncHTTPClient()

    responses = yield map(lambda stop: http.fetch(stop.fetch_url()), stops)
    json_responses = []
    for stop, response in zip(stops, responses):
      item = stop.stop_departure_predictions(response.body.strip())
      if item is not None:
        json_responses.append(item)
    self.write({'nearby_departures': json_responses })
    self.set_header("Content-Type", "application/json")

def main():
  parse_command_line()
  app = tornado.web.Application(
    [
      (r"/", MainHandler),
      (r"/migrate", MigrateHandler),
      (r"/predictions", RealtimeDepartureHandler),
    ],
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
  )
  app.listen(options.port)
  engine = create_engine(options.postgres_url, echo=False)
  app.Session = sessionmaker(bind=engine)
  tornado.ioloop.IOLoop.instance().start()
  models.init_db(engine)
  
if __name__ == "__main__":
  main()
