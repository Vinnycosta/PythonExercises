import requests as req
#import datetime as dt
import csv

url = 'https://api.covid19api.com/dayone/country/brazil'
resp = req.get('https://api.covid19api.com/dayone/country/brazil')

raw_data = resp.json()
endData = []
for obs in raw_data:
    endData.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])
endData.insert(0, ['Confirmados', 'Óbitos', 'Recuperados', 'Ativos', 'Data'])

Data = 4
Obitos = 1
Confirmados = 0
Recuperados = 2
Ativos = 3

for i in range(1, len(endData)):
    endData[i][Data] = endData[i][Data][:10]

with open('brasil-covid.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(endData)

for i in range(1, len(endData)):
    endData[i][Data] = dt.datetime.strptime(endData[i][Data], '')
    
