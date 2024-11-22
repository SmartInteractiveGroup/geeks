#joining lists
ages_one = [25,30,39]
ages_two = [14,15,15]

joined_ages = ages_one + ages_two
print(ages_one)
print("joined ages",joined_ages )

ages_one.extend(ages_two)
print(ages_one)
print("joined ages_2:",ages_one)

# slincing lists
scores = [25, 30, 39, 14, 15, 15]
print("from start to index 2:",scores[0:3])
print("from index 3 to end:",scores[3:])
print("from index 1 to 4:",scores[1:4])
print("from index 0 to 4 step 2:",scores[:5:2])
print("from index 0 to end step 2:",scores[::2])
print("reversing the list:",scores[::-1]) # step of -1
