user_input = ""
while user_input != "exit":
    user_input = input("Please input heads or tails: ")
    if user_input == "exit":
        break
    with open("coins.txt", "r") as file:
        lines = file.readlines()
    lines.append(user_input+"\n")
    with open("coins.txt", "w") as file:
        file.writelines(lines)
        chance = 0
        counter = 0
        for line in lines:
            counter += 1
            if line.strip("\n") == "heads":
                chance += 1
        chance /= counter
        chance *= 100
        chance = round(chance, 2)
        print(f"\nHeads: {chance}%\n")
