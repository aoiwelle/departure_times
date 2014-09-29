import unittest
from models import TransitStop, MuniStop

stop_data = """
<?xml version="1.0" encoding="utf-8" ?> 
<body copyright="All data copyright San Francisco Muni 2014.">
<route tag="F" title="F-Market &amp; Wharves" color="555555" oppositeColor="ffffff" latMin="37.7625199" latMax="37.8085899" lonMin="-122.43487" lonMax="-122.39345">
<stop tag="5184" title="Jones St &amp; Beach St" lat="37.8072499" lon="-122.41737" stopId="15184"/>
<stop tag="3092" title="Beach St &amp; Mason St" lat="37.80741" lon="-122.4141199" stopId="13092"/>
<stop tag="3095" title="Beach St &amp; Stockton St" lat="37.8078399" lon="-122.41081" stopId="13095"/>
<stop tag="4502" title="The Embarcadero &amp; Bay St" lat="37.8066299" lon="-122.4060299" stopId="14502"/>
<stop tag="4529" title="The Embarcadero &amp; Sansome St" lat="37.8050199" lon="-122.4033099" stopId="14529"/>
<stop tag="4516" title="The Embarcadero &amp; Greenwich St" lat="37.80296" lon="-122.40103" stopId="14516"/>
<stop tag="4518" title="The Embarcadero &amp; Green St" lat="37.80061" lon="-122.39892" stopId="14518"/>
<stop tag="4504" title="The Embarcadero &amp; Broadway" lat="37.7988999" lon="-122.3974299" stopId="14504"/>
<stop tag="4534" title="The Embarcadero &amp; Washington St" lat="37.7963599" lon="-122.3951799" stopId="14534"/>
<stop tag="7283" title="The Embarcadero &amp; Ferry Building" lat="37.7948299" lon="-122.3937699" stopId="17283"/>
<stop tag="4726" title="Ferry Plaza" lat="37.7940499" lon="-122.39345" stopId="14726"/>
<stop tag="5669" title="Market St &amp; Drumm St" lat="37.7934699" lon="-122.39618" stopId="15669"/>
<stop tag="5657" title="Market St &amp; Battery St" lat="37.7911099" lon="-122.39907" stopId="15657"/>
<direction tag="F__OBCTRO" title="Outbound to Castro Station via Downtown" name="Outbound" useForUI="true">
  <stop tag="5184" />
  <stop tag="3092" />
  <stop tag="3095" />
  <stop tag="4502" />
  <stop tag="4529" />
  <stop tag="4516" />
  <stop tag="4518" />
  <stop tag="4504" />
  <stop tag="4534" />
  <stop tag="7283" />
  <stop tag="4726" />
  <stop tag="5669" />
  <stop tag="5657" />
  <stop tag="5639" />
  <stop tag="5678" />
  <stop tag="5694" />
  <stop tag="5655" />
  <stop tag="5695" />
  <stop tag="5656" />
  <stop tag="5676" />
  <stop tag="5679" />
  <stop tag="5696" />
  <stop tag="5672" />
  <stop tag="5681" />
  <stop tag="5659" />
  <stop tag="5661" />
  <stop tag="5690" />
  <stop tag="5686" />
  <stop tag="33311" />
</direction>
<direction tag="F__IBCTRO" title="Inbound to Fisherman&apos;s Wharf via Downtown" name="Inbound" useForUI="true">
  <stop tag="3311" />
  <stop tag="5687" />
  <stop tag="5691" />
  <stop tag="5662" />
  <stop tag="5668" />
  <stop tag="5675" />
  <stop tag="5673" />
  <stop tag="5692" />
  <stop tag="5652" />
  <stop tag="5651" />
  <stop tag="5650" />
  <stop tag="5647" />
  <stop tag="5645" />
  <stop tag="5643" />
  <stop tag="5640" />
  <stop tag="5685" />
  <stop tag="7264" />
  <stop tag="5682" />
  <stop tag="4727" />
  <stop tag="4513" />
  <stop tag="4532" />
  <stop tag="4503" />
  <stop tag="4517" />
  <stop tag="4515" />
  <stop tag="7281" />
  <stop tag="4501" />
  <stop tag="4530" />
  <stop tag="5174" />
  <stop tag="5175" />
  <stop tag="35184" />
</direction>
<path>
<point lat="37.76252" lon="-122.43487"/>
<point lat="37.76267" lon="-122.4352"/>
<point lat="37.76396" lon="-122.43332"/>
<point lat="37.76569" lon="-122.43114"/>
<point lat="37.76726" lon="-122.42915"/>
</path>
<path>
<point lat="37.78036" lon="-122.41261"/>
<point lat="37.7821" lon="-122.4104"/>
<point lat="37.78389" lon="-122.40814"/>
<point lat="37.7856499" lon="-122.40589"/>
</path>
<path>
<point lat="37.7856499" lon="-122.40589"/>
<point lat="37.7875299" lon="-122.40352"/>
<point lat="37.78861" lon="-122.40216"/>
<point lat="37.79094" lon="-122.39919"/>
</path>
<path>
<point lat="37.79094" lon="-122.39919"/>
<point lat="37.79298" lon="-122.39663"/>
<point lat="37.7944699" lon="-122.39476"/>
<point lat="37.79369" lon="-122.39379"/>
<point lat="37.7939" lon="-122.39345"/>
</path>
<path>
<point lat="37.77506" lon="-122.41932"/>
<point lat="37.77741" lon="-122.41634"/>
<point lat="37.77861" lon="-122.41483"/>
<point lat="37.78036" lon="-122.41261"/>
</path>
<path>
<point lat="37.79405" lon="-122.39345"/>
<point lat="37.79369" lon="-122.39379"/>
<point lat="37.7944699" lon="-122.39476"/>
<point lat="37.79347" lon="-122.39618"/>
<point lat="37.79111" lon="-122.39907"/>
</path>
<path>
<point lat="37.7939" lon="-122.39345"/>
<point lat="37.79426" lon="-122.39305"/>
<point lat="37.79511" lon="-122.39386"/>
<point lat="37.79709" lon="-122.39567"/>
<point lat="37.79955" lon="-122.39787"/>
<point lat="37.80126" lon="-122.39937"/>
<point lat="37.80326" lon="-122.40111"/>
<point lat="37.80407" lon="-122.40198"/>
<point lat="37.80515" lon="-122.40323"/>
<point lat="37.80615" lon="-122.40479"/>
<point lat="37.80695" lon="-122.40628"/>
<point lat="37.8081" lon="-122.40906"/>
<point lat="37.80835" lon="-122.41029"/>
</path>
<path>
<point lat="37.78586" lon="-122.40574"/>
<point lat="37.78408" lon="-122.40799"/>
<point lat="37.78232" lon="-122.41023"/>
<point lat="37.78057" lon="-122.41244"/>
</path>
<path>
<point lat="37.7752399" lon="-122.41918"/>
<point lat="37.7732699" lon="-122.42177"/>
<point lat="37.77095" lon="-122.42467"/>
<point lat="37.76979" lon="-122.42615"/>
<point lat="37.7678299" lon="-122.42863"/>
</path>
<path>
<point lat="37.78057" lon="-122.41244"/>
<point lat="37.77911" lon="-122.41438"/>
<point lat="37.7775899" lon="-122.41621"/>
<point lat="37.7752399" lon="-122.41918"/>
</path>
<path>
<point lat="37.7678299" lon="-122.42863"/>
<point lat="37.76619" lon="-122.43071"/>
<point lat="37.76449" lon="-122.43281"/>
<point lat="37.7642" lon="-122.43308"/>
<point lat="37.76262" lon="-122.43295"/>
<point lat="37.76252" lon="-122.43487"/>
</path>
<path>
<point lat="37.80784" lon="-122.41081"/>
<point lat="37.8080799" lon="-122.40924"/>
<point lat="37.80737" lon="-122.40731"/>
<point lat="37.80663" lon="-122.40603"/>
<point lat="37.80615" lon="-122.40479"/>
<point lat="37.80502" lon="-122.40331"/>
<point lat="37.80407" lon="-122.40198"/>
<point lat="37.80296" lon="-122.40103"/>
<point lat="37.80061" lon="-122.39892"/>
<point lat="37.7989" lon="-122.39743"/>
<point lat="37.79636" lon="-122.39518"/>
<point lat="37.79483" lon="-122.39377"/>
<point lat="37.79426" lon="-122.39305"/>
<point lat="37.79405" lon="-122.39345"/>
</path>
<path>
<point lat="37.80835" lon="-122.41029"/>
<point lat="37.80862" lon="-122.4124"/>
<point lat="37.80859" lon="-122.41336"/>
<point lat="37.80832" lon="-122.41551"/>
<point lat="37.80801" lon="-122.41745"/>
<point lat="37.80725" lon="-122.41737"/>
</path>
<path>
<point lat="37.79111" lon="-122.39907"/>
<point lat="37.78935" lon="-122.40131"/>
<point lat="37.78773" lon="-122.40337"/>
<point lat="37.78586" lon="-122.40574"/>
</path>
<path>
<point lat="37.76726" lon="-122.42915"/>
<point lat="37.76888" lon="-122.4271"/>
<point lat="37.77057" lon="-122.42497"/>
<point lat="37.77288" lon="-122.42199"/>
<point lat="37.77506" lon="-122.41932"/>
</path>
<path>
<point lat="37.80725" lon="-122.41737"/>
<point lat="37.80741" lon="-122.41412"/>
<point lat="37.80784" lon="-122.41081"/>
</path>
</route>
</body>
"""

departure_predictions = """
<?xml version="1.0" encoding="utf-8" ?> 
<body copyright="All data copyright San Francisco Muni 2014.">
<predictions agencyTitle="San Francisco Muni" routeTitle="F-Market &amp; Wharves" routeTag="F" stopTitle="The Embarcadero &amp; Washington St" stopTag="4534">
  <direction title="Outbound to Castro Station via Downtown">
  <prediction epochTime="1411689931604" seconds="325" minutes="5" isDeparture="false" dirTag="F__OBCTRO" vehicle="1053" block="9816" tripTag="6344681" />
  <prediction epochTime="1411690360915" seconds="754" minutes="12" isDeparture="false" affectedByLayover="true" dirTag="F__OBCTRO" vehicle="1074" block="9809" tripTag="6344682" />
  <prediction epochTime="1411690672915" seconds="1066" minutes="17" isDeparture="false" affectedByLayover="true" dirTag="F__OBCTRO" vehicle="1011" block="9820" tripTag="6344683" />
  <prediction epochTime="1411691392915" seconds="1786" minutes="29" isDeparture="false" affectedByLayover="true" dirTag="F__OBCTRO" vehicle="1057" block="9817" tripTag="6344685" />
  <prediction epochTime="1411692472915" seconds="2866" minutes="47" isDeparture="false" affectedByLayover="true" dirTag="F__OBCTRO" vehicle="1071" block="9811" tripTag="6344688" />
  </direction>
<message text="For real time srv alerts follow us on Twitter: sfmta_muni" priority="Normal"/>
<message text="Be alert and report any unusual activity." priority="Normal"/>
</predictions>
</body>
"""

class MockSession:
  def __init__(self):
    self.added = []

  def merge(self, item):
    item._sa_instance_state = None
    self.added.append(item)

class MuniStopTest(unittest.TestCase):

  def test_fetch_stop_data_url(self):
    expected_fetch_string = "http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=sf-muni"
    self.assertEqual(MuniStop.fetch_stop_data_url(), expected_fetch_string) 

  def test_fetch_url(self):
    stop_id = 123
    stop = MuniStop(id=stop_id)
    expected_fetch_string = "http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=sf-muni&stopId=" + str(stop_id)
    self.assertEqual(stop.fetch_url(), expected_fetch_string) 

  def test_stop_departure_predictions(self):
    stop = MuniStop(id=14534)
    stop.longitude = -122.3951799
    stop.latitude = 37.7963599
    json_dict = {}
    json_dict['stop_name'] = "The Embarcadero & Washington St"
    json_dict['longitude'] = stop.longitude
    json_dict['latitude'] = stop.latitude
    json_dict['route_name'] =  "F-Market & Wharves"
    directions_json = []
    direction_json = {}
    direction_json['direction_name'] = "Outbound to Castro Station via Downtown"
    direction_json['predictions'] = [5, 12, 17, 29, 47]
    directions_json.append(direction_json)
    json_dict['directions'] = directions_json
    self.assertEqual(stop.stop_departure_predictions(departure_predictions.strip()),json_dict)

  def test_add_stops(self):
    session = MockSession()
    MuniStop.add_stops(session,stop_data.strip())
    self.assertEquals(len(session.added), 13)
    ms = MuniStop(id=15184, name="Jones St & Beach St", agency=MuniStop._agency,stop_location="POINT(-122.41737 37.8072499)")
    # do equality on subset of attributes for MuniStop
    ms._sa_instance_state = None
    contains_item = reduce(lambda x,y: x or y, map(lambda x: isinstance(ms, x.__class__)
        and x.__dict__ == ms.__dict__ , session.added)) 
    self.assertTrue(contains_item)

class TransitStopTest(unittest.TestCase):
  def test_fetch_url(self):
    with self.assertRaises(NotImplementedError):
      t = TransitStop()
      t.fetch_url()

  def test_fetch_stop_data_url(self):
    with self.assertRaises(NotImplementedError):
      TransitStop.fetch_stop_data_url()

  def test_fetch_stop_data_url(self):
    with self.assertRaises(NotImplementedError):
      TransitStop.add_stops()

  def test_stop_departure_predictions(self):
    with self.assertRaises(NotImplementedError):
      t = TransitStop()
      t.stop_departure_predictions()

if __name__ == '__main__':
    unittest.main()
