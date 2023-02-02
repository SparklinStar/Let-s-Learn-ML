import numpy as np
mylist = [1, 2, 34, 5, 6, 7]
arr = np.array(mylist)
print(arr)
print(type(arr))
mylist1 = [45, 56, 78, 34]
mylist2 = [4, 6, 8, 56]
mylist3 = [65, 36, 69, 788]
arr = np.array([mylist1, mylist2, mylist3])
# used for reshaping arr.reshape(6, 2)
print(arr[1:3, 2:4])  # used for traversing
arr = np.arange(0, 11, 3)
print(arr)
