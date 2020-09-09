

def reverse(word):
    i= -1
    while i>=-(len(word)):
          print (word[i] ,end =" ")
          i-=1


str = input("Enter a string to reverse")
reverse(str)