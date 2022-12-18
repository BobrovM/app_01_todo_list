import random


print("Use keyword exit to exit.")
while True:
    user_lower = input("Enter the lower bound: ")
    if user_lower == "exit":
        break
    user_upper = input("Enter the upper bound: ")
    if user_upper == "exit":
        break
    result = random.randint(int(user_lower), int(user_upper))
    print(result)
print("Bye!")