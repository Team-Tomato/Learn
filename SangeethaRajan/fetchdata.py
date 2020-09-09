import requests
import json
import csv
url="https://teamtomato.herokuapp.com/api/v1/question"
response=requests.get(url)
data=response.text
parsed=json.loads(data)
outfile=open("Datafrom_api.csv","w")
writer=csv.writer(outfile)
count = 0
for row in parsed:
    if count == 0:
        header = row.keys()
        print(writer.writerow(header))
        count+=1
    writer.writerow(row.values())
outfile.close()


