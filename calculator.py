# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

from colorama import Fore, Style

def get_integer_input(prompt):
    while True:
        try:
            return int(input(Fore.BLUE + prompt + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter an integer e.g. 10, 5, 34 etc." + Style.RESET_ALL)

# get operator input
def get_operator_input():
    while True:
        operator = input(Fore.BLUE + "Enter the operator: (+, -, *, /) " + Style.RESET_ALL)
        if operator in ['+', '-', '*', '/']: #Check whether the operator is valid
            return operator
        else:
            print(Fore.RED + "Invalid operator. Please use either +, -, * /" + Style.RESET_ALL)


print(f"Welcome to the myCalculator!")

while True:
    num1 = get_integer_input("Enter your first number: ")
    num2 = get_integer_input("Enter your second number: ")
    operator = get_operator_input()

    # Perform the operation based on the user's input and print the result
    if operator == '+':
        result = num1 + num2
        print(Fore.GREEN + f"{num1} + {num2} = {result}" + Style.RESET_ALL)

    elif operator == '-':
        result = num1 - num2
        print(Fore.GREEN + f"{num1} - {num2} = {result}" + Style.RESET_ALL)

    elif operator == '*':
        result = num1 * num2
        print(Fore.GREEN + f"{num1} * {num2} = {result}" + Style.RESET_ALL)

    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
            print(Fore.GREEN + f"{num1} / {num2} = {result}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Error: Division by 0 is not allowed" + Style.RESET_ALL)

# Ask if the user wants to perform another calculation
    continue_prompt = input(Fore.BLUE + "Do you want to do other calculations? (yes/no) " + Style.RESET_ALL).strip().lower()
    if continue_prompt != 'yes':
        print(Fore.YELLOW + "Goodbye! Thanks for using myCalculator!" + Style.RESET_ALL)
        break