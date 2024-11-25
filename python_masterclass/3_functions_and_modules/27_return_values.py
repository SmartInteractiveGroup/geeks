# return values
# def square(x):
#     return x*x

# result = square(5)
# print(result)

#returning multiple values

# def get_coords():
#     x = 25.3
#     y = 48.2
#     return x,y   #just names - those could be different

# x,b = get_coords()
# print(x,b)  # '*' - unpack from tuples

#using return to break out of a function

age = 15

def do_something():
    if age <20:
        return
    print(age)

result = do_something()
print(result)

