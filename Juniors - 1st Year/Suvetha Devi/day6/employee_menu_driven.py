class Employee:
    name = []
    emp_no= []
    salary = []
    designation = []

    def get_data(self):
        self.num= int(input("Enter the no of employee details going to be entered"))
        for i in range(0,self.num):
                self.name.append(str(input("Enter the name of employee")))
                self.emp_no.append(int(input("Enter the employee no")))
                self.salary.append(int(input("Enter the salary")))
                self.designation.append(str(input("Enter the designation")))
    def display(self):
        for i in range(0,self.num):
               print (self.name[i],self.emp_no[i],self.salary[i],self.designation[i])

e = Employee()
e.get_data()
e.display()
