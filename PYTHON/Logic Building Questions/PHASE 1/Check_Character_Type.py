character = input("Enter the character : ")
if character >= 'A' and character <='Z':
    print("UpperCase")
elif character >='a' and character <='z':
    print("LowerCase")
elif character >= '1' and character <= '9':
    print("Digit")
else :
    print("Special Character")
