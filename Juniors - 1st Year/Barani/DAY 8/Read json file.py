import json 
def edit_json(json_object, filename = "Employee.json"):
    ID = int(input("\nEnter the ID - number of the Employee to edit: "))
    for i in json_object['employee']:
        if ID == i['id']:   
            print("\nChoose the optin to edit")
            print(" 1.id number\n 2.Name\n 3.Position\n 4.Email\n 5.Contact\n 6.Salary\n 7.Exit")        
            opt = int(input())
            if opt == 1:
                i['id'] = int(input("Enter ID of Employee \'{)\' to edit: ").format(i['Name']))
            elif opt == 2:
                i['Name'] = input("Enter Name of Employee \'{}\' to edit: ".format(i['Name']))
            elif opt == 3:
                i['Position'] = input("Enter the position of Employee \'{}\' to edit: ".format(i['Name'])) 
            elif opt == 4:
                i['Email'] = input("Enter Email-ID of Employee \'{}\' to edit: ".format(i['Name']))
            elif opt == 5:
                i['Contact'] = input("Enter Contact of Employee \'{}\' to edit: ".format(i['Name']))
            elif opt == 6:
                i['Salary'] = input("Enter Annual salary of Employee \'{}\' in Indian Rupees to edit: ".format(i['Name']))
            elif opt == 7:
                print("EXIT")
                break
            print("Content in \'{}\' after editing".format(filename))
            for i in json_object['employee']:
                print(i)
                print()
            json_object.update()
    return json_object

if __name__ == '__main__':
    with open('Employee.json','r') as json_file:
        json_object = json.load(json_file)
        print("Content in 'Employee.json' file")
        for i in json_object['employee']:
            print(i)
            print()    
    repeat = 'r'
    while repeat == 'r':
        with open('Employee.json', 'w') as write_file:
            new_object = edit_json(json_object)
            json.dump(new_object, write_file, indent = 6)
            repeat = input("Enter \'r\' to repeat editing: ")
        
