fruits = ["apple", "banana", "mango", "orange"]

print(fruits)
print(fruits[0])
print(fruits[-1])

fruits.append("grape")
print(fruits)

fruits.remove("banana")
print(fruits)

print(len(fruits))

for fruit in fruits:
    print("I like", fruit)
