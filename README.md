Departure Times
====================

## Description and Learnings
To demonstrate the backend for giving real-time departure times. A minimal front end is provided to show a sample consumer of the API.
Using data NextBus data, I've pulled Muni stop locations to search against when a consumer of the API gives a Latitude-Longitude coordinates and an optional radius(in meters, the postgis default).
For demo/prototype purposes, I've limited the scope to Muni times in San Francisco, but used STI on the data model to decouple the searching of POIs from the business logic of supplying a specific ageny's data.
I decided to query for prediction times every time the endpoint was hit instead of pre-emptively caching, given the lack of insights around usage patterns or bottlenecks as well as allowing for more accurate data.
Also, had there been more data sources and a better understanding of the frequency of data updates per agency, I would have created a job server to make these updates to the database in the background according to the freshness needs of the data.

## Dependencies
Postgresql-9.3 with the PostGIS 2.1 extension enabled
Tornado 4.0.1
GeoAlchemy2 0.2.4
psycopg2 2.5.4

## More About Libraries and Architectual Decisions
Though I've had no prior experience with PostGIS, I've found that the libraries available are robust enough to do the kind of POI searches required by the service.
I chose Tornado because I've had some limited exposure to the library in some other spare-time projects with friends I've worked on, and that it allowed for high-volume asynchronous networking calls, which were good for making concurrent fetches against a third party data source, and a minimal web server, which lends itself well to defining APIs.
I've used SQLAlchemy in a similar scope to Tornado, but have never used GeoAlchemy2, but given it allowed for a similar flexibility to SQLAlchemy, I thought it would be appropriate to fetching business logic for the results of each POI and give a unified interface for heterogenous agency data.
Though I've had very limited experience with the tech stack and language, I did find it fun to have the opportunity to explore using python again in addition to learning how to use PostGis and GeoAlchemy2.

## Running
To run the app, you can use the following command(with default options explicitly set)
```bash
python departure_times.py --port=8080 --radius=321.868 --postgres_url=postgresql://localhost/departure_times
```
If this is the first time starting up, navigate to http://localhost:8080/migrate to load muni data

# Demo
Check out the app at http://departure-times-aoiwelle.crabdance.com:8080/

## Learn More About Me
Check me out on [LinkedIn](www.linkedin.com/pub/neal-wiggins/6/878/388/)
