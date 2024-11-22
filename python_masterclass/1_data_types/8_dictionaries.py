#collection of key-value pairs
#dictionary view not a regular list of values
#immutable
#don't have acces to list 
#we can loop 
#we can perform checking

#dicrionaries
person = {
    "name": "yoshi",
    "age":30,
    "job":"egg collector"
}

#print(person)
#print(person["name"])
#print(person["age"])

#methods

print(person.get("name"))
print(person.keys())
print(person.values())
print("age" in person.keys())


#copy
copied_person = person.copy()
print("copied person", copied_person)

#update
person.update({"name":"mario", "age":36})
print(person)

#clear all
person.clear()

print(person)
