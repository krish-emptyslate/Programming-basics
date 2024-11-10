numbers = [1,2,3,4,5,2,4]
print(numbers)
#prints 3rd element of the list
print("this is 3rd element",numbers[2])
#modifying the element
print("number[2] is modified as 20")
numbers[2]=20
print(numbers)

#adding an element
numbers.append("hello")
print(numbers)
#deleting an element
numbers.remove(4)
print(numbers)