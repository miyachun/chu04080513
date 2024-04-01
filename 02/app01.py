#https://opendata.cwa.gov.tw/dist/opendata-swagger.html
import json,urllib.request

url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-093?Authorization=CWB-F6A0BAC9-E773-4B09-B048-D30A55EEBED2&locationId=F-D0047-009'

data = urllib.request.urlopen(url).read()
output = json.loads(data)
location=output['records']['locations'][0]['location']


for i in location:
    print(f'{i}')


for i in location:
  name = i['locationName']
  lat=i['lat']
  print(name,lat)







