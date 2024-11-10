def divide(num1,num2):
    try:
     result = num1 / num2
    except ZeroDivisionError:
        print("Zero cant be divided")
    except TypeError :
        print("Enter only numbers")
    else :
        return print(result)
    finally:
        print("code is executed successfully")


divide(10,2)
divide(10,0)
divide(10,"hii")


