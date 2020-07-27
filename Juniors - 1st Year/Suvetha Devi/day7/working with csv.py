import csv
with open("employee.csv",'w',newline = '')as write_file:
    writer = csv.writer(write_file)
    x = int(input("How many employee details u want to  enter"))
    for i in range(0,x):
             print("Enter the following data")
             name = input("Name of the employee:")
             emp_no= int(input("employee number:"))
             salary = int(input("Salary:"))
             desig = input("Designation:")
             writer.writerow([name,emp_no,salary,desig])


read_file = open('employee.csv','r')
reader = csv.reader(read_file)
for row in reader:
    print(row)
read_file.close()
write_file.close()