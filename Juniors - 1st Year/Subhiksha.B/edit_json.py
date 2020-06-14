import json
def append_json(data):
    with open ('student_detail.json','w') as file:
        json.dump(data, file , indent = 4)
def edit(json_object):
    R_no = int(input("\nEnter roll number of the student to edit the details of that student:"))
    for i in json_object["student_Id"]:
        if R_no == i["Roll_no"]:
            print("\nEnter any option to edit\n")
            ch = int(input("Enter \n 1.Roll no\n 2.Name \n 3.Class \n 4. School\n 5.Exit:"))
            if ch == 1:
                i["Roll_no"] = int(input("\nEnter  roll number of the student:"))
            elif ch == 2:
                i["Name"] = input("\nEnter name of the student:")
            elif ch == 3:
                i["Class"] = input("\nEnter class of the student:")
            elif ch == 4:
                i["School"] = input("\nEnter school name of the student:")
            else:
                print("Exit")
            print("\ncontent in student detail file:")
            for detail in json_object["student_Id"]:
                print(detail)
            json_object.update()
    return json_object

if __name__ == '__main__':
    with open('student_detail.json','r') as read_file:
        json_object = json.load(read_file)
        print("\ncontent in student detail file:")
        for detail in json_object["student_Id"]:
            print(detail)
    op =int(input("\nEnter:\n 1.To append student detail to json file \n 2. To edit the content of the existing json file \n 3.Exit:"))
    while op != 3 :
        if op == 1 :
            with open ('student_detail.json') as json_file:
                data = json.load(json_file)
                temp = data["student_Id"]
                A = {
                "Roll_no" : int(input("\nEnter roll number of the student to add in json file:")),
                "Name" : input("\nEnter name of the student to add in json file:"),
                "Class" : input("\nEnter class of the student to add in json file:"),
                "School" : input("\n Enter school of the student to add in json file:")
                }
                temp.append(A)   
                append_json(data)
                

        elif op == 2 :
            with open('student_detail.json','w') as write_file:
                write_content = edit(json_object)
                json.dump(write_content,write_file,indent = 4)
        op =int(input("\nEnter:\n 1.To append student detail to json file \n 2. To edit the content of the existing json file \n 3.Exit:"))
    print("Exited")
    