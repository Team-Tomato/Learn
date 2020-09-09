import json
import csv
import io
#import urllib2
import requests
import codecs
import unicodedata

urlcomp = 'https://teamtomato.herokuapp.com/api/v1/question'
headers = {'authorization': "Basic API Key Ommitted", 'accept': "application/json", 'accept': "text/csv"}

## API Call to retrieve report
rcomp = requests.get(urlcomp, headers=headers)

## API Results
data = rcomp.text
S=data.replace("\u2013", "-")
d=json.loads(S)

with open('pqrs.csv', 'w') as csvFile:
 
  writer = csv.writer(csvFile)
  fields = ['id', 'shortForm', 'staff', 'subjectName', 'url', 'year']
   
  writer = csv.DictWriter(csvFile, fieldnames=fields)
  writer.writeheader()
 
  for line in d:
    print(writer.writerow(line))


