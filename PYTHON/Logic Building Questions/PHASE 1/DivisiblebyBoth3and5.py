num = int(input("Enter the number : "))
if num%3==0 and num%5==0 :
    print(num , "is Divisible by both 3 and 5 number")
elif num%3==0 and num%5!=0 :
    print(num , "is Divisible by 3 but not by 5 number")
elif num%3!=0 and num%5==0 :
    print(num , "is not Divisible by 3 but by 5 number")
else:
    print(num,"is not divisible by any of the number")