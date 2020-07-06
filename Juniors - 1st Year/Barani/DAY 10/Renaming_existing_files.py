import os,sys

def rename_single(directory, old_name, new_name, extension):
    for file in os.listdir():
        src=file
        if src == old_name:
               dst = new_name + extension
               os.rename(src,dst)
          
def rename_limit(directory, limit, new_name, extension):
    count = 1
    for file in os.listdir():
        if(count <= limit):
            src = file
            dst = new_name + str(count) + extension
            os.rename(src,dst) 
            count+=1

def rename_all(directory, new_name, extension):
    count = 1
    for file in os.listdir():
        src = file
        dst = new_name + str(count) + extension
        os.rename(src,dst)
        count+=1
        
if __name__ == '__main__' :
    
    directory = input("Enter the directory : ")
    os.chdir(directory)
    print(f"List of files in given directory:\n{os.listdir()}")
    print("\nCHOOSE THE OPTION TO RENAME FILES IN GIVEN DIRECTORY:")
    print(" 1. Renaming Single file\n 2. Renaming from first upto required limit\n 3. Renaming all the files")
    ch = int(input())
    
    if ch == 1:
        old_name = input("Enter old name(WITH EXTENSION): ")
        new_name = input("Enter new name(WITHOUT EXTENSION): ")
        extension = input("Enter the extension: ")
        rename_single(directory, old_name, new_name, extension)
        
    elif ch == 2:
        limit = int(input("Enter the limit: "))
        new_name = input("Enter new name(WITHOUT EXTENSION) for all file to change: ")
        extension = input("Enter the extension: ")
        rename_limit(directory, limit, new_name, extension,)
        
    elif ch == 3:
        new_name = input("Enter new name(WITHOUT EXTENSION) for all file to change: ")
        extension = input("Enter the extension: ")
        rename_all(directory, new_name, extension)
    else:
        print("INVALID OPTION")
        print("EXIT")

        
