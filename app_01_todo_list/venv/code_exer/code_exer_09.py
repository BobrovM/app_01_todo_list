user_input = input("Enter new password: ")
if len(user_input) < 7:
    print("Weak password.")
elif len(user_input) == 7:
    print("Password is OK, but not strong.")
else:
    print("Strong password.")