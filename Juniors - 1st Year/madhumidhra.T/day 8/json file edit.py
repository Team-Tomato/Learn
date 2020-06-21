import json
def edit_json_file(json_object, filename = "snew.json"):
    roll_no= int(input("\nEnter the roll number to edit: "))
    for i in json_object['student']:
        if roll_no == i['roll_no']:
            print("\nChoose the option to edit")
            print(" 1.roll_no\n 2.Name\n 3.eng_mark\n 4.maths_mark\n 5.sci_mark\n 6.exit")
            option = int(input("enter the option which you want to change"))
            if option == 1:
                i['roll_no'] = int(input("Enter roll number of student \'{}\' to edit: ").format(i['Name']))
            elif option == 2:
                i['Name'] = input("Enter Name of student \'{}\' to edit: ".format(i['Name']))
            elif option == 3:
                i['eng_mark'] = input("Enter the english mark of  the student \'{}\' to edit: ".format(i['Name']))
            elif option == 4:
                i['maths_mark'] = input("Enter the maths mark of the student \'{}\' to edit: ".format(i['Name']))
            elif option == 5:
                i['sci_mark'] = input("Enter the science mark of the student \'{}\' to edit: ".format(i['Name']))
            elif option == 6:
                print("EXIT")
                break
            print("Content in \'{}\' after editing".format(filename))
            for i in json_object['student']:
                print(i)
                print()
            json_object.update()
    return json_object

if __name__ == '__main__':
    with open('snew.json','r') as json_read_file:
        json_object = json.load(json_read_file)
        print(" prints the Content in 'snew.json' file")
        for i in json_object['student']:
            print(i)
            print()
    repeat = 'r'
    while repeat == 'r':
        with open('snew.json', 'w') as json_write_file:
            new_object = edit_json_file(json_object)
            json.dump(new_object,json_write_file , indent = 4)
            repeat = input("Enter \'r\' to repeat editing: ")