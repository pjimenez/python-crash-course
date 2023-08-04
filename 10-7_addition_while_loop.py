print(f"Give me two numbers and I will add them")

while True:
    try:

        fist_number = input("Enter your first number: ")
        if fist_number ==  "q":
            break

        fist_number = int(fist_number)

        second_number = input("Enter your second number: ")
        if second_number == "q":
            break

        second_number = int(second_number)

    except ValueError:
        print(f"Sorry, please enter a valid number")

    else:
        total = fist_number + second_number

        print(f"Your total is: {total}")