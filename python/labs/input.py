name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello", name)
print("You are", age, "years old")
print(type(age))          # age is string by default

age = int(age)            # convert to integer
print("Next year you will be", age + 1)
