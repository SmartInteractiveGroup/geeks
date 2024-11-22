# example without error handling:

# number = int(input("Enter the number: "))

# example with error handling:

    # example nr 1  
# try:
#     number = int(input("Enter the number: "))
#     print("You entered",number)
# except:
#     print('That is not a number')
# finally:
#     print('Completed')

# try:
#     number = int(input("Enter the number: "))
#     print("You entered",number)
# except ValueError as e:
#     print('That is not a number')
#     print(e)
# finally:
#     print('Completed')

     # example nr 2

a = 10
b = 0

try:
    print(a/b)
except ZeroDivisionError as e:
    print('cannot divide a number by 10')
    print('error:',e)

print('end of the file')
