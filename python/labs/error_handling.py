try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result is:", result)
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("Something went wrong:", e)
finally:
    print("This always runs.")
