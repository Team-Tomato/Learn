class employee:
    number=0
    name=""
    age=0
    gender=""
    salary=0
    def get_emp_info(self):
        self.member= int(input("enter how many employee details you aregoing to enter"))
        for i in range(self.member):
            print(i +1,end=",,")
            self.number = int(input("enter the number of the employee"))
            self.name=str(input("enter the name of the employee"))
            self.age = int(input("enter the age of the employee"))
            self.gender =str(input("enter the gender of the employee"))
            self.salary = int(input("enter the salary of the employee"))
            print()
    def show_emp_info(self):
        self.member = int(input("enter the emploee to be viewed"))
        for i in range(self.member):
            print(i + 1, end=".")
            print(" number of the employee:", self.number)
            print(" name of the employee:",self.name)
            print(" age of the employee:", self.age)
            print(" gender of the employee:", self.gender)
            print(" salary of the employee:",self.salary)
            print()
if __name__ == '__main__':
    emp=employee()
    n=int(input("1.enter the employee detail\n 2.show the employee detail\n 3.quit\n"))
    while n!=3:
        if n==1:
           emp.get_emp_info()
        else:
           emp.show_emp_info()
        n=int(input("1.enter the employee detail\n 2.show the employee detail\n 3.quit\n"))
    if n==3:
        print("exit")

