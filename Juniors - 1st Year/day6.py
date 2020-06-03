class Employee:
    
    id=''
    name=''
    design=''
    allowance=''
    salary=0

    def __init__(self,id,name,design,alllowance,salary):
        self.id=id
        self.name=name
        self.design=design
        self.allowance=allowance
        self.salary=salary

    def search(self,no):
        if(self.id==no):
            print("ID:/t/t",self.id)
            print("NAME:/t/t",self.name)
            print("DESIGNATION:/t/t",self.degign)
            print("ALLOWANCE:/t/t",self.allowance)
            print("BASIC SALARY:/t/t",self.salary)

    def addEmployee(self):
        self.id=int(input("\nenter no.: "))
        self.name=str(input("\nenter name: "))
	self.design=str(input("\ndesignation: "))
	self.salary=int(input("\nbasic pay: "))
	self.allowance=int(input("\nallowance:"))
	
    def computeNetSalary(self,no):
        if(no==self.id):
            self.allowance=int(input("\nallowance"))
            ns=self.salary+self.allowance
            print("net salary",ns)

    def update(self,no):

	if(self.id==no):
            self.salray=int(input("enter basic pay"))

    def display(self):
        print("ID:/t/t",self.id)
        print("NAME:/t/t",self.name)
        print("DESIGNATION:/t/t",self.degign)
        print("ALLOWANCE:/t/t",self.allowance)
        print("BASIC SALARY:/t/t",self.salary)


if __name__="___main___":
    emp[10] = Employee()
    ch=1
    while(ch!=6):
        count=0
        print("\nMenu\n1.Add\n2.compute\n3.seach\n4.update\n5.display\n6.exit\n")
        ch=int(input())
        ch:{
            1:
                e[count].addEmployee();
		count+=1;
		break

	    2:
                no=int(input("enter employee no.\n"))
                for i in range(0,count):
                             e[i].computeNetSalary()
                             break

	    3:
		no=int(input("enter employee no.\n"))
		for i in range(0,count):
                             e[i].search()
                             break

	    4:
                no=int(input("enter employee no.\n"))
		for i in range(0,count):
                             e[i].update()
                             break

	    5:
                for i in range(0,count):
                             e[i].display()
                             break

	    6:
                exit(0)
        }

















