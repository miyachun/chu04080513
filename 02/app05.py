from flask import Flask, render_template,redirect, request

import json,urllib.request


app = Flask(__name__)

url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=(API_KEY)&format=JSON'
@app.route('/')
def index():
    #print('aa')    
    dict_example ={"city":[],"wx8":[],"maxt8":[],"mint8":[],"pop8":[]}    
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    location=output['records']['location']
    for i in location:
        city = i['locationName']    # 縣市名稱
        wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']    # 天氣現象
        maxt8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName']  # 最高溫
        mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']  # 最低溫
        ci8 = i['weatherElement'][3]['time'][0]['parameter']['parameterName']    # 舒適度
        pop8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']   # 降雨機率
        #print(f'{city}未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %')
        dict_example['city'].append(city)
        dict_example['wx8'].append(wx8)
        dict_example['maxt8'].append(maxt8)
        dict_example['mint8'].append(mint8)
        dict_example['pop8'].append(pop8)
        
    #print(dict_example)
    return render_template('indexc.html',dict_example=dict_example)

@app.route('/dropdown', methods = ['POST'])
def dropp():
    dropdownval = request.form.get('colour')
    print(dropdownval)
    #return redirect("/", code=302)
    city_example ={"city":[]}     
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    location=output['records']['location']
    for i in location:
        city = i['locationName']        
        city_example['city'].append(city)      
    #print(dict_example)
    return render_template('indexd.html',d=dropdownval)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        dropdownval = request.form.get('colour')
        print(dropdownval)
        render_template('indexe.html',d="ssscityexample")
    cityexample =[]     
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    location=output['records']['location']
    for i in location:
        cityc = i['locationName']        
        cityexample.append(cityc)    
    return render_template('indexe.html',d=cityexample)

@app.route('/findA', methods = ['POST'])
def findA():
    dropdownval = request.form.get('colour')
    #print(dropdownval)
    dict_example ={"city":[],"wx8":[],"maxt8":[],"mint8":[],"pop8":[]}
    ansA=[]    
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    location=output['records']['location']
    for i in location:
        city = i['locationName']
        if city==dropdownval:
            wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']    # 天氣現象
            maxt8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName']  # 最高溫
            mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']  # 最低溫
            ci8 = i['weatherElement'][3]['time'][0]['parameter']['parameterName']    # 舒適度
            pop8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']   # 降雨機率
            #print(f'{city}未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %')
            dict_example['city'].append(city)
            dict_example['wx8'].append(wx8)
            dict_example['maxt8'].append(maxt8)
            dict_example['mint8'].append(mint8)
            dict_example['pop8'].append(pop8)
            ansA.append(wx8)
            ansA.append(maxt8)
            ansA.append(mint8)
            ansA.append(pop8)
    return render_template('indexf.html',d=dropdownval,dict_example=ansA)


if __name__ == '__main__':
    #app.run()
    app.run(debug=True)
