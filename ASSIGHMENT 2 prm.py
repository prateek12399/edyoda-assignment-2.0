#ANSWER 1
list1=[1,2,3,4,5,6]
def find_len(list1):
    lst = []
    length = len(list1)
    lst.append(list1[length-1])
    lst.append(list1[0])
    lst.append(list1[length-2])
    lst.append(list1[1])
    lst.append(list1[length-3])
    lst.append(list1[2])

    print(lst)

largest = find_len(list1)


#ANSWER 2

num = int(input("enter a nth o. of fibonacci"))

def fibonacci(num):
    a = 0
    b = 1
    if num < 0:
        print("Incorrect input")
    elif num == 0:
        print("Incorrect input")
    elif num == 1:
        return b
    else:
        for i in range(2,num+1):
            c = a + b
            a = b
            b = c
        return b
    
print(fibonacci(num))
