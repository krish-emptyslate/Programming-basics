import array
#creating an array
arr = array.array('i',[1,2,3,4])

#accessing elements
print(arr[3])

#modifying
arr[1] = 10

arr.append(6)
arr.remove(1)
print(arr)


