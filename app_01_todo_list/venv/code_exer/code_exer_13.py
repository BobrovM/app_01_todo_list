# ex. 1-3
def age_calculator(year_of_birth, current_year=2022):
    return current_year - year_of_birth


user_input = int(input("What is your year of birth? "))
user_age = age_calculator(user_input)

if user_age > 120:
    print(f"You are too old for this world. Your age is {user_age}.")

else:
    print(user_age)


# ex. 4
def separate(names):
    return names.split(" ")


def count(names_list):
    return len(names_list)


user_input = input("\nEnter names separated by spaces: ")
user_names = separate(user_input)
print(count(user_names))
