Year = int(input("Enter the Year to check if the year is Leap year or not :"))
if (Year%400==0 ) or (Year!=100==0 and Year%4==0):
    print(Year,"Year is Leap Year")
else :
    print(Year, "Year is not Leap Year")
