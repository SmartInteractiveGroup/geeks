#global & local variables

# #global means in a file
# # x=10

# # def print_x():
# #     global x
# #     x = 5 #creates a new local value
# #     print(f"x inside the print_x finction is {x}")

# def print_y():
#     y=20
#     print(f"inside the function is: {y}")

# # print_x()
# # print(f"global value of x is {x}")


# print_y()



#scope within nested functions

def outer():
    age = 25

    def inner():
        nonlocal age
        age=30
        print(f'age inside inner() is: {age}')
    
    inner()
    print(f'age inside outer() is: {age}')

outer()

