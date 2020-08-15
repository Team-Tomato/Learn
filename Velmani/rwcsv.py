import csv


with open("data.csv","w+") as csvfile:
	 writer = csv.writer(csvfile)
	 writer.writerow(["col1","col2"])
	 writer.writerow(["Data1","Data2"])



with open("data.csv","r") as csvfile:
     reader = csv.reader(csvfile)
     for row in reader:
	      print(row)
 


with open("data.csv","a") as csvfile:
	 writer = csv.writer(csvfile)
	 writer.writerow(["Data3","Data4"])

  

 with open("data.csv","r") as csvfile:
	 reader = csv.DictReader(csvfile)
     for row in reader:
         print(row)



with open("data.csv", "a") as csvfile:
    fieldnames = ["id", "title"]
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writerow({"id": 123, "title": "New Title"})

