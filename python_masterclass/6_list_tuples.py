#list
names = ["mario","peach","luigi"]
print(names[0])
print(names[2])

print('Length of the list is:', len(names))

#changing list values

names[1] = "toad"
print(names)

#list methods
## append

names.append("bowser")
print(names)

## remove
names.remove("toad")
print(names)

names.sort()
print(names)

#tuples
top_scores = (100,95,92,92,88,85)
print(top_scores)
print(top_scores[0])
print(len(top_scores))

#tuples are immutable
#top_scores[0] = 99

#tuples method  
print(top_scores.count(92))
print(top_scores.index(85))

