import csv
print("writing in a csv file")
with open("students.csv","w",newline='')as csv_file:
    write_content = csv.writer(csv_file)
    num=int(input("enter any number"))
    while num!= 0:
        print("enter the student details")
        name=str(input("enter the students name"))
        rollno=int(input("enter the roll number"))
        mark=int(input("enter the marrk of the student"))
        write_content.writerow((rollno,name,mark))
        print("if you want to continue print any number or to quit print 0")
        num = int(input("enter any number"))
    print(" you have pressed 0 to quit")
with open ("students.csv","r")as read_file:
    Read_content=csv.reader(read_file)
    for i in Read_content:
        print(i)
read_file.close()
csv_file.close()