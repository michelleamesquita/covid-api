from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app= Flask(__name__)

page = requests.get("https://www.worldometers.info/coronavirus/")
page_text=page.text

soup = BeautifulSoup(page.content, 'html.parser')
# soup.find_all('p') soup.find_all('p')[0].get_text() soup.find_all(id="first")
table= soup.find_all(id='main_table_countries_today')

infoTable=[]
country=[]
totalCases=[]
newCases=[]
totalDeath=[]
totalRecovered=[]
activeCases=[]
seriousCritical=[]
firstCase=[]


info=soup.find_all('td')
for i in info:
    infoTable.append(i.text)

for i in range(0,len(infoTable),11):
    country.append(infoTable[i])

for i in range(1,len(infoTable),11):
    totalCases.append(infoTable[i])

for i in range(2,len(infoTable),11):
    newCases.append(infoTable[i])

for i in range(3,len(infoTable),11):
    totalDeath.append(infoTable[i])

for i in range(4,len(infoTable),11):
    totalRecovered.append(infoTable[i])

for i in range(5,len(infoTable),11):
    activeCases.append(infoTable[i])

for i in range(6,len(infoTable),11):
    seriousCritical.append(infoTable[i])

for i in range(10,len(infoTable),11):
    firstCase.append(infoTable[i].strip('\n'))

json_country=[]
# json
for i in range(len(country)):
    json ={
        'id': i,
        'country': str(country[i]),
        'totalCases': str(totalCases[i]),
        'newCases': str(newCases[i]),
        'totalDeath': str(totalDeath[i]),
        'totalRecovered': str(totalRecovered[i]),
        'activeCases': str(activeCases[i]),
        'seriousCritical': str(seriousCritical[i]),
        'firstCase': str(firstCase[i])

    }
    json_country.append(json)

#print(json_country[403]['id'])

@app.route('/',methods=['GET'])
def home():
    return "Hello world :)",200

@app.route('/country',methods=['GET'])
def country():
    return jsonify(json_country),200


@app.route('/country/<int:id>',methods=['GET'])
def id(id):
    for i in json_country:
        if i['id'] == id:
            return jsonify(i), 200

    return jsonify({'error':'not found'}),404



@app.route('/country/<string:country>',methods=['GET'])
def country_id(country):
    for i in json_country:
        if i['country'] == country:
         return jsonify(i),200


@app.route('/world/',methods=['GET'])
def world():
    data=json_country[403]
    return jsonify(data),200


if __name__ == '__main__' :
    app.run(debug=True)
