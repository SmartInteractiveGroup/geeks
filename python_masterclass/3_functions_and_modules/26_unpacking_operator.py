# use *args to accept any number of positional arguments
# '*' stands for the uncompact


# def print_total(*args):
#     print(*args)

#     total = 0
#     for number in args:
#         total+=number
#     print(f'the total is:{total}')

# print_total(50,75)
#print_total(24,35,79,100,15)


#print(50,75)
#print(24,35,79,100,1112)

#use kwargs to accept any number of keyword arguments

def print_ninja(**kwargs):
    #print(kwargs.items())

    for key,value in kwargs.items():
        print(f"{key} -- {value}")
    return

print_ninja(name="yoshi",age=25)
print_ninja(first_name="mario",belt_color="white")