import csv
print("Writing in a csv file")
with open("employee.csv",'w',newline="") as csv_file:
    write_content = csv.writer(csv_file)
    ch = input("Enter any alphabet:")
    while ch != 'q':
        print("Enter the employee info:")
        Name = input("Enter name of the employee:")
        Age = int(input("Enter age of the employee:"))
        Salary = input("Enter the salary of the employee:")
        write_content.writerow((Name,Age,Salary))
        ch = input("Enter any alphabet to continue the process or enter 'q' to quit:")
    print("You entered 'q' to quit")
with open("employee.csv",'r') as read_file:
    Read_content = csv.reader(read_file)
    for line in Read_content:
        print(line)
read_file.close()
csv_file.close()