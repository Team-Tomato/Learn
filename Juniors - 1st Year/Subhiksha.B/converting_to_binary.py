def convert_to_binary(d):
    if d > 1 :
      convert_to_binary(d // 2)
    print(d % 2,end = "")
dec = int(input("Enter the decimal number to be converted to binary:"))
convert_to_binary(dec)