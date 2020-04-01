import plotly.express as px
import requests
import pandas as pd


activeCases=[]
country=[]
firstCase=[]
newCases=[]
seriousCritical=[]
totalCases=[]
totalDeath=[]
totalRecovered=[]
id=[]
iso_alpha=[]

for i in range(404):
    url = 'http://127.0.0.1:5000/country/'+str(i)
    r = requests.get(url)
    app_json = r.json()
    id.append(app_json['id'])
    activeCases.append(app_json['activeCases'])
    country.append(app_json['country'])
    firstCase.append(app_json['firstCase'])
    newCases.append(app_json['newCases'])
    seriousCritical.append(app_json['seriousCritical'])
    totalCases.append(app_json['totalCases'])
    totalDeath.append(app_json['totalDeath'])
    totalRecovered.append(app_json['totalRecovered'])
    a = country[i]
    iso_alpha.append(a[:3].upper())

newCases2=[]
for i in range(404):
     total = str(newCases[i]).replace(",", ".")
     total = total.replace("+","")
     if total == '':
         total = 0
         # newCases2.append(total)
     else:
        total=float(total)
     #    new_total=total/100
     #    if new_total > 0.001:
     #         total=total*1000

     # total=round(total)
     newCases2.append(total)

print(newCases2)

data = {
        'id': id,
        'activeCases':activeCases,
        'iso_alpha': iso_alpha,
        'country':country,
        'firstCase':firstCase,
        'newCases':newCases2,
        'seriousCritical':seriousCritical,
        'totalCase':totalCases,
        'totalDeath':totalDeath,
        'totalRecovered':totalRecovered
        }



# Create DataFrame
df = pd.DataFrame(data)
print(df)
fig = px.scatter_geo(df, locations="iso_alpha",color="country",hover_name="country", size="newCases",
                       projection="natural earth")

fig.show()


