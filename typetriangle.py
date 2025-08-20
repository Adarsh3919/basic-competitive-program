angle1 = int(input("enter the angle= "))
angle2 = int(input("enter the angle= "))
angle3 = int(input("enter the angle= "))
if(angle1==90 or angle2==90 or angle3 == 90):
 print("it is a right triangle")
elif(angle1>=90 or angle2>=90 or angle3 >=90):
    print("it is an obtuse triangle")
else:
    print("it is an acute angle")