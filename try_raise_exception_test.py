try:
    age = input("Enter your age: ")
    age = int(age)
    if age < 0 or age > 150:
        raise ValueError("Error Age Range is not valid")
except ValueError as ve:
    print(ve)
else:
    print(f"Your age is {age}")
finally:
    print("Execution completed")

