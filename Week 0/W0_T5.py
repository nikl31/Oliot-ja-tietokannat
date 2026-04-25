value = 0.0

while True:
    print(f"Current value {value}")
    user_input = input("Add number(empty stops): ")

    if user_input == "":
        break

    value += float(user_input)

print(f"Final value {value}")