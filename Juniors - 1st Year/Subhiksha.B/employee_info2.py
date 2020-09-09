class Employee:
    Member = 0
    Name = ""
    Age = 0
    Gender = ""
    Salary = 0
    def get_info(self):
        self.Member = int(input("Enter the number of employee detail to be entered:"))
        for i in range(self.Member):
            print(i +1,end =".")
            self.Name = input("Enter  employee name :")
            self.Age = int(input("Enter  employee  age :"))
            self.Gender = (input("Enter  employee  gender :"))
            self.Salary = int(input("Enter employee's salary:"))
            print("\n")
    def show_info(self):
        self.Member = int(input("Enter the number of employee detail to be viewed:"))
        for i in range(self.Member):
            print(i +1,end =".")
            print("Name of the Employee:",self.Name)
            print("Age of the Employee:",self.Age)
            print("Gender of the Employee:",self.Gender)
            print("Salary of the Employee:",self.Salary)
            print("\n")
if __name__== '__main__':
    emp = Employee()
    ch =int(input("\nEnter 1.get the info of employees\nEnter 2.Show the info of employees\nEnter 3.Exit\n"))
    while ch != 3:
        if ch == 1:
            emp.get_info()
        else:
            emp.show_info()
        ch =int(input("\nEnter 1.get the info of employees\nEnter 2.Show the info of employees\nEnter 3.Exit\n"))
    if ch == 3:
        print("You entered choice 3 to Exit")