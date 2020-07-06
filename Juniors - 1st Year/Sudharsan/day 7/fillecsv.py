csvfile=open('csvfile.csv','r')
readcsv=csvfile.read()

csvnew=open('newcsv.csv','w')

for i in readcsv:
    csvnew.write(i)