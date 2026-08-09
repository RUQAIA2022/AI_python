# fruits = ["banana", "apple", "orange"]

# for fruit in fruits:
#     print(fruit)

# for x in "banana":
#     print(x)

fruits = ["banana", "apple", "orange"]

for fruit in fruits:
    print(fruit)
    if fruit == "apple":
        break  # exits the loop when fruit is apple

# for x in fruits:
#     if x != "apple":
#         newlist.append(x)

newlist = [x for x in fruits if x != "apple"]
print(newlist)



# for i in range(5):
#     print(i)   



adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)



newlist = [x for x in range(10) if x < 5]
print(newlist)     