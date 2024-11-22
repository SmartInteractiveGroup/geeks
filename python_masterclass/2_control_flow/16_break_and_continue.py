count = 0

#break - breakes the loop completly
# while count < 10:
#     if count == 5:
#         break
#     print(count)
#     count+=1

#continue - skip an iteration
while count < 10:
    count += 1
    if count % 2 != 0:
        continue
    print(count)