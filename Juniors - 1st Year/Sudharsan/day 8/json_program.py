jsonfile=open('jsonfile.json','r')
jsondata=jsonfile.read()
print(jsondata)

jsonwrite=open('newjson.json','w')

for i in jsondata:
    jsonwrite.write(i)