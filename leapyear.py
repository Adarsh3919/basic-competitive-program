a=int(input("enter your year= "))
if a%4==0 and (a%100!=0 or a%400==0):
    print("leap year")
else:
    print("it is not a leap year")