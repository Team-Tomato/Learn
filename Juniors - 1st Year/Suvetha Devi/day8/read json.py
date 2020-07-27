import json
def edit_json(json_object,filename = "Student.json"):
    rollno:int(input("Enter the rollno to edit"))
    for i in json_object['Student']:
        if rollno==i['rollno']:
            p=int(input("Choose to edit 1.name,2.rollno,3.course,4.cgpa,5.exit"))
            if p==1:
                i['name'] = input("Enter name to change\'{}\'").format(i['name'])
            elif p==2:
                i['rollno'] = int(input("Enter the rolno to modify\'{}\'").format(i['name']))
            elif p==3:
                i['course']=input("Enter the course of the student\'{}\'").format(i['name'])
            elif p==4:
                i['cgpa'] = int(input("Enter the cgpa \'{}\'").format(i['name']))
            else:
                print("EXIT")
                break
    print("After editing\'{}\'".format(filename))
    for i in json_object['Student']:
                print(i)
                print()
    json_object.update()
    return json_object

with open('Student.json','r') as json_file:
    json_object = json.load(json_file)
    print("Content in the file")
    for i in json_object['Student']:
        print(i)
        print()
s=1
if(s==1):
    with open('Student.json''w')as write_file:
        new_object = edit_json(json_object)
        json.dump(new_object,write_file,indent=6)
        s = int(input("Enter 1.to continue,2.to exit"))







