#evaluation of comparison to check if is True or False

# booleans
is_authenticated = True
is_authenticated_1 = False

print(is_authenticated)
print(not is_authenticated)

#comparison operators
x = 5
y = 10

a,b = 3,6
print(x>y)
print(x==y)
print(x != y)

#boolean operator & member checking
z,y = True, False
print(z and y) #False
print(z or y) #True

#falsy values --> 0 numbers and empty data structs
print(bool(0))
print(bool(""))
print(bool([]))


# truthy values --> everythin else
print(bool(1))
print(bool("a"))
print(bool([100,90]))

#evaluating strings
name = "mario"

print(name.startswith('m'))
print(name.endswith('t'))


