import json


data = open('F-C0032-001.json',"r",encoding="utf-8")
 
output = json.load(data)
location=output['records']['location']
 
for i in location:
    city = i['locationName']
    wx = i['weatherElement'][0]['time'][0]['parameter']['parameterName']
    maxtT = i['weatherElement'][4]['time'][0]['parameter']['parameterName']
    mintT = i['weatherElement'][2]['time'][0]['parameter']['parameterName']
    ci = i['weatherElement'][3]['time'][0]['parameter']['parameterName']
    pop = i['weatherElement'][4]['time'][0]['parameter']['parameterName']
    print(f'{city}未來 8 小時{wx}，最高溫 {maxtT} 度，最低溫 {mintT} 度，降雨機率 {pop} %')

