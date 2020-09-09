import json
f=open('data.json')
jsObj=json.load(f)
for i in jsObj['product']:
	print(i)
f.close()
f=open('data.json','a')

#jsObj=json.load(f)

jsObj["product"]:{"fruit":"banana"}
    

	

f.close()

