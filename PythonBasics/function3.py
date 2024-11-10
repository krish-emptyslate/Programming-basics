#function with arbitrary arguments
#positonal argument
def add(*numbers):
    return sum(numbers)

print(add(1,2,3))

#keyword arguments
def personal_info(**info):
    print(info)

personal_info(name="krish" ,age=20 , city="chennai")
