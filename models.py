from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geography
import xml.etree.ElementTree as ET

Base = declarative_base()

def init_db(engine):
  Base.metadata.create_all(bind=engine)

class TransitStop(Base):
  __tablename__ = 'transit_stop'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  agency = Column(String)
  stop_location = Column(Geography('POINT'))
  type = Column(String(30))

  __mapper_args__ = {
      'polymorphic_on':type,
      'polymorphic_identity':'transit_stop'
    }

  def fetch_url(self):
    raise NotImplementedError()

  @classmethod
  def fetch_stop_data_url(cls):
    raise NotImplementedError()

  @classmethod
  def add_stops(cls, *args):
    raise NotImplementedError()

  def stop_departure_predictions(self, *args):
    raise NotImplementedError()

class MuniStop(TransitStop):

  _agency = 'sf-muni'
  __mapper_args__ = {
        'polymorphic_identity':'muni_stop'
    }

  def fetch_url(self):
    return "http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=%s&stopId=%s" % (self._agency, str(self.id))

  @classmethod
  def fetch_stop_data_url(cls):
    return "http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=%s" % (cls._agency)

  @classmethod
  def add_stops(cls, session, response_body):
    xml = ET.fromstring(response_body)
    stops = xml.findall('.//route/stop')
    for stop in stops:
      ms = cls(id=int(stop.get('stopId')),name=stop.get('title'),
            agency=cls._agency,stop_location="POINT(%s %s)"%(stop.get('lon'),stop.get('lat')))
      session.merge(ms)

  def stop_departure_predictions(self, response_body):
    xml = ET.fromstring(response_body)
    json_response = {} 
    json_response['stop_name'] = xml.find('.//predictions').get('stopTitle')
    json_response['longitude'] = self.longitude
    json_response['latitude'] = self.latitude
    json_response['route_name'] =  xml.find('.//predictions').get('routeTitle')
    directions = xml.findall('.//predictions/direction')
    directions_json = []
    for direction in directions:
      direction_json = {}
      direction_json['direction_name'] = direction.get('title')
      direction_json['predictions'] =  map(lambda x: int(x.get('minutes')),direction.findall('./prediction'))
      if len(direction_json['predictions']) > 0:
        directions_json.append(direction_json)
    
    if len(directions_json) > 0:
      json_response['directions'] = directions_json
      return json_response
    else:
      return None
