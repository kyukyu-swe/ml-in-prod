
try:
    first_num = input("Enter your first number : ")
    second_num = input("Enter your second number : ")
    division = int(first_num) / int(second_num)
    print("The sum of the two numbers is ", division)
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide a number by zero")
except ValueError as e:
    print(e)
    print("Invalid input. Please enter numeric values only.")
except Exception:
    print("Something went wrong. Please try again")
else:
    print("Division performed successfully")
finally:
    print("Execution completed")



