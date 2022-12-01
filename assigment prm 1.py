size=int(input("Enter the number of element: "))
lst1=[]
for i in range(size):
    num= input("Enter the number: ")
    lst1.append(num)

print(lst1)
res=sorted(lst1, key = lambda sub : sub[-2])

print("sorted list :" + str(res))



#Taking sides for triangle
side1 = int(input("Enter the side1 value of triangle :" ))
side2 = int(input("Enter the side2 value of triangle :" ))
side3 = int(input("Enter the side3 value of triangle :" ))
#Taking sides for rectangle
num1 = int(input("Enter the side1 value of the Rectangle: "))
num2 = int(input("Enter the side2 value of the Rectangle: "))
num3 = int(input("Enter the side3 value of the Rectangle: "))
num4 = int(input("Enter the side4 value of the Rectangle: "))

def checkingvalidation(side1,side2,side3,num1,num2,num3,num4):
    if (side1 + side2 > side3) and (side3 + side2 >side1) and (side1 + side3 > side2):
        print("valid triangle")
    else:
        print("invalid triangle")
    
    if (num1 == num3) and (num2 == num4):
        print("valid rectangle")
    else:
        print("invalid rectangle")

checkingvalidation(side1,side2,side3,num1,num2,num3,num4)