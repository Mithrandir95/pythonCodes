def LinearSearch(x,y):
    n=len(x)
    for i in range (n):
        if target[i]==y:
            return num[i]
        return False
num=input("Enter the numbers:")
target=input("Enter the element to be searched:")
res=LinearSearch(num,target)
print("The element is found at position",res)