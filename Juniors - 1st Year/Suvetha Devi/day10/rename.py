import os,sys
def single_renaming(direct,old,new,extn):
    for file in os.listdir():
        source = file
        if source == old:
            dst = new+extn
            os.rename(source,dst)

def limit_renaming(direct,limit,new,extn):
    flag=1
    for file in os.listdir():
        if(flag<=limit):
            source = file
            dst = new+str(flag) + extn
            os.rename(source,dst)
            flag+=1

def all_renaming(direct,new,extn):
    flag=1
    for file in os.listdir():
        source = file
        dst = new + str(flag) +extn
        os.rename(source,dst)
        flag+=1











repeat='r'
while repeat=='r':
      direct = input("Enter the directory in which you want to rename your  files")
      os.chdir(direct)
      print(f"List of files found in your directory : \n{os.listdir()}")
      x = int(input("Enter 1.to rename a single file,2.to rename the files upto the given limit,3.to rename all the files"))
      if(x==1):
           old = input("Enter your file's old name with extn")
           new =input("Enter new filename without extn")
           extn=input("Enter the extension")
           single_renaming(direct,old,new,extn)
      elif x==2:
          limit = int(input("Enter the limit"))
          new = input("Enter the new name for your  without extn for all files to change")
          extn = input("Enter the extension")
          limit_renaming(direct,limit,new,extn)
      elif x==3:
         new= input("Enter new name with extn for all files u want to change")
         extn = input("enter the extension")
         all_renaming(direct,new,extn)
      else:
        print("EXIT, u choosed a invalid option")
      repeat = input("Enter 'r' to  repeat the process")
