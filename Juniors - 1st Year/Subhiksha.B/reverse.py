def reverse(s):
    ch = ""
    for c in s:
        ch = c + ch
    return ch
str = input("Enter the string to be reversed:")
print(reverse(str))