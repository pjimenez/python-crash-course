# print(f'Give me two numbers and I will add them')
#
# try:
#     first_number = int(input("First number: "))
#     second_number = int(input("Second number: "))
#
# except ValueError:
#     print(f"Sorry, please enter a number")
#
# else:
#     total = first_number + second_number
#     print(f"The total is {total}")

# Make it into a function
def adding_machine():
    """ This is the same code as above, only made into a function called adding_machine"""
    print(f'Give me two numbers and I will add them')

    try:
        first_number = int(input("First number: "))
        second_number = int(input("Second number: "))

    except ValueError:
        print(f"Sorry, please enter a number")

    else:
        total = first_number + second_number
        print(f"The total is {total}")


adding_machine()