try:
    x=int(input("Enter a number: "))
    result = 10/x
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except TypeError:
    print("Error: Invalid type. Please enter a valid number.")
else:
    print('Result:', result)
finally:
    print("Execution completed...")