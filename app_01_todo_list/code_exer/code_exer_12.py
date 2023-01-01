def ex1_liters_to_meters(liters):
    return liters / 1000


def check_psswd_strength(psswd):
    output = [False, False, False]
    if len(psswd) > 7:
        output[0] = True
    for letter in psswd:
        if letter.isupper():
            output[1] = True
            break
    for letter in psswd:
        if letter.isdigit():
            output[2] = True
    return output


user_input = int(input("Enter liters: "))
print(f"This is {ex1_liters_to_meters(user_input)} cubic meters.")

user_input = input("Enter new password: ")
result = check_psswd_strength(user_input)
if all(result):
    print("Strong password.")
else:
    print("Weak password.")
