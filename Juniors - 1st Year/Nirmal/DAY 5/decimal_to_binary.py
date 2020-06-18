def decimal(dec):
    if dec > 1:
	    decimal(dec//2)
    print (dec%2, end =" ")
dec=int(input("Enter the Decimal number to be converted into Binary: ")) 
print ("Binary equivalent of {}: ". format (dec)) 
decimal(dec)
