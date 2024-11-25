#arguments
def multiply(a,b):
    return a*b

result = multiply(3,5)
print(result)

#named arguments
def print_score(name,score):
    print(f"{name} has a score of {score}")

print_score(score=50, name="youshi")



#default arguments

def divide(a,b=1):
    return a/b
resulte = divide(20,4)
print(result)

result = divide(2)
print(result)