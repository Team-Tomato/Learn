print("***Python program to swap 2 numbers, characters***")
def swap(input1,input2):
    input1,input2 = input2,input1
    return input1,input2
if __name__ == '__main__':
    print("Enter 2 numbers to swap")
    input1,input2 = int(input()),int(input())
    print("Numbers before swapping = ",(input1,input2))
    print("Numbers after swapping = ",swap(input1,input2))
    print("Enter 2 characters to swap")
    input1,input2 = input(),input()
    print("characters before swapping = ",(input1,input2))
    print("characters after swapping = ",swap(input1,input2))
    