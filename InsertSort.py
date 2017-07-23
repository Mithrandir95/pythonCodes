def InsertSort(k):
    for i in range(1,len(k)):
        j = i
        while j > 0 and k[j] < k[j-1]:
            temp = k[j]
            k[j] = k[j - 1]
            k[j - 1] = temp
            j=j-1
    return k
my_list=[4,5,10,4,56,11,23,1,2,3]
print("the sorted list is:")
InsertSort(my_list)
print(my_list)
