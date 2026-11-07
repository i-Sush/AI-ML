SideA = int(input("Enter Side A : "))
SideB = int(input("Enter Side B : "))
SideC = int(input("Enter Side C : "))

if SideA + SideB > SideC and SideB + SideC > SideA and SideA + SideC > SideB:
    print("The Triangle is a Valid Triangle!")
else:
    print("It's Not a Valid Triangle!")