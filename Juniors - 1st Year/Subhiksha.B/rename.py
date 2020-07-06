import os
def  rename_single_file(old_name,new_name, file_type):
    for file in os.listdir():
        source = file + file_type
        old_name2=old_name + file_type
        if source == old_name2:
            destination = input("Enter new name to the file:") + file_type
            os.rename(source,destination)
def rename_all_file(old_name,new_name, file_type):
    print("choose option to rename\n")
    opt = input("Enter 1. rename all the files in contiguous manner by using numbers like photo1,photo2 etc\n 2. Rename all the files by getting user input:")
    if opt == 1:
        i = 1
        for file in os.listdir():
            source = file + file_type
            destination = file + str(0+i) + file_type
            os.rename(source,destination)
            i += 1
    if opt == 2:
        for file in os.listdir():
            source = file + file_type
            destination = input("Enter new name to your file")+ file_type
            os.rename(source,destination)
def  rename_certain_limits(old_name,new_name, file_type):
    limit = input("Enter number of pictures to rename in your folder")
    op = input("Enter 1. Renaming files from initial to certain limit in the folder\n 2. Renaming file from a particular file to certain limit in the folder:")
    if op == 1:
        count = 1
        for  file in os.listdir():
            source = file +file_type
            destination = file +str(count) + file_type
            os.rename(source, destination)
            count += 1
    if op == 2:
        starting_file = input("Enter name of the file where you have to start renaming files")
        for starting_file  in os.listdir():
            source = file + file_type
            destination = input("Enter new name to your file") + file_type
            os.rename(source,destination)
if __name__ == '__main__' :
    path = input("Enter the path where your folder/directory present")
    os.chdir(path)
    old_name = input("Enter your existing file name to rename it")
    new_name = input("Enter name to rename the corresponding file ")
    file_type = input("Enter file type of your file")
    print("Choose the option to rename your files in the given folder/dictionary")
    ch = input("Enter 1.Renaming single file\n 2. Renaming all files in a folder\n 3.Renaming upto certain limit\n 4.Exit")
    while ch != 4:
        if ch == 1:
            rename_single_file(old_name,new_name, file_type)
        if ch == 2:
            rename_all_file(old_name,new_name, file_type)
        if ch == 3:
            rename_certain_limits(old_name,new_name, file_type)
        if ch == 4:
            print("Exit")


