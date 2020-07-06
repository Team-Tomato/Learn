import os,sys
def rename_single(directory, old_name, new_name, extension):
    for file in os.listdir():
        src=file
        if src == old_name:
               dst = new_name + extension
               os.rename(src,dst)
          
if __name__ == '__main__' :
    os.chdir("C:\\Users\\praji\\Desktop")
    
    directory = input("Enter the directory : ")
    os.chdir(directory)
    print(f"List of files in given directory:\n{os.listdir()}")
    
    
    old_name = input("Enter old name(WITH EXTENSION): ")
    new_name = input("Enter new name(WITHOUT EXTENSION): ")
    extension = input("Enter the extension: ")
    rename_single(directory, old_name, new_name, extension)
    
    
