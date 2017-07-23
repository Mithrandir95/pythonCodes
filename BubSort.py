def BubSort(unsorted_list):
    length=len(unsorted_list)-1
    sort=False;
    while not sort:
        sort = True
        for i in range(length):
            if unsorted_list[i]>unsorted_list[i+1]:
                sort=False
                temp= unsorted_list[i + 1]
                unsorted_list[i + 1]= unsorted_list[i]
                unsorted_list[i]=temp
    return
my_list=[2,5,6,3,7,54,112,58454,1212]
print("The sorted array is:")
BubSort(my_list)
print (my_list)