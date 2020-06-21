import os
previous_file_name=input("enter the file name you want to change with filetype")
new_file_name=input("enter the newfile name with filetype")
os.rename(previous_file_name,new_file_name)
print("process finished")