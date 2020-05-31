print("***EMPLOYEE DETAILS***")
class Employee:
    __Name = []
    __Number = []
    __Position = []
    __Annual_salary = []

    def getdata(self):
        self.num = int(input("Enter no. of employees data needs to be stored: "))
        for i in range(self.num):
            self.__Name.append(str(input("\nEnter Employee-"+str(i+1)+" Name: ")))
            self.__Number.append(int(input("Enter Employee-"+str(i+1)+" Number: ")))
            self.__Position.append(str(input("Enter Employee-"+str(i+1)+" Position: ")))
            self.__Annual_salary.append(int(input("Enter Employee-"+str(i+1)+" Annual salary: ")))

    def display(self):
        print("Employee Details\n")
        print("EMPLOYEE NAME \t EMPLOYEE NUMBER \t EMPLOYEE POSITION \t EMPLOYEE ANNUAL SALARY\n")
        for i in range(self.num):
            print(self.__Name[i],"\t\t",self.__Number[i],"\t\t\t",self.__Position[i],"\t\t\t",self.__Annual_salary[i],"\n")

if __name__ == '__main__':
    E = Employee()
    ch = 'r'
    while ch == 'r':
        print("Enter\n 1 for Add Employee details\n 2 for Displaying Employee details\n")
        opt = int(input("Enter the option: "))
        if opt == 1:
            E.getdata()
        elif opt == 2:
            E.display()
        ch = str(input("\n Enter \'r\' to repeat the process: "))
    print('EXIT')
