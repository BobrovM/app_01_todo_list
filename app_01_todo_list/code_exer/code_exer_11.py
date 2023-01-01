def get_max():
    grades = [9.6, 9.2, 9.7]
    prompt = f"Max: {max(grades)}, Min: {min(grades)}"
    return prompt


print(get_max())