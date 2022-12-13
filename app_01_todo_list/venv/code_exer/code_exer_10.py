print("Exer 1 and 2\n")
total_value = input("Enter total value: ")
user_value = input("Enter value: ")
try:
    percent = int(user_value) / int(total_value) * 100
    print(f"That is {round(percent, 2)}%.")
except ValueError:
    print("You need to enter a number.")
except ZeroDivisionError:
    print("Total value cannot be zero. Division by zero is not possible.")
