NumberOne = int(input("Enter First Number : "))
NumberTwo = int(input("Enter Second Number :"))
NumberThird = int(input("Enter Third Number : "))
# if NumberOne > NumberTwo :
if NumberOne > NumberTwo:
    if NumberOne > NumberThird :
        print(NumberOne," is the largest number")
    else :
        print(NumberThird," is the largest number")
else:
    if NumberTwo > NumberThird :
        print(NumberTwo," is the Largest Number")
    else :
        print(NumberThird," is the Largest Number")