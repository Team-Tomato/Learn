import csv
print("***WRITING TO A FILE & READING FROM THE FILE***")
with open("Student.csv", 'w',newline = '') as write_file:
    writer = csv.writer(write_file)
    ans= 'y'
    while (ans == 'y'):
        print("Enter The following data:")
        name = input("Name: ")
        course= input("Course: ")
        cgpa = input("CGPA: ")
        writer.writerow([name, course, cgpa])
        ans=input("Do you want to enter more y/n?: ")

read_file=open('Student.csv', 'r')
reader = csv.reader(read_file)
for row in reader:
    print(row)
read_file.close()
write_file.close()
