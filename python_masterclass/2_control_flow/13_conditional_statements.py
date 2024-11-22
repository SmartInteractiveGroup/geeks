score = 7
print(f"The score is: {score}")
# if statements
if score > 5:
    print('The score is greater that 5')

# if/else statements
if score > 10:
    print('The score is greater that 10')
else:
    print("The score is not greater than 10")

# if/elif/else statements
if score > 10:
    print('The score is greater than 10')
elif score > 5:
    print('The scocre is greater than 5')
else:
    print('The score is equal or less than 5')

# AND, OR, NOT, IS NOT
age = 3
if age > 10 and age < 20:
    print('OK')

authenticated = False

if authenticated:
    print('authenticated')

if not authenticated:
    print("not authenticated")

if authenticated is not False:
    print('authenticated is not False')

if authenticated is False:
    print('authenticated is False')