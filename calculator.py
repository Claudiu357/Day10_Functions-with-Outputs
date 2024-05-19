from art import logo
print(logo)
operations = ["+", "-", "/", "*"]
calculator_running = True
number_1 = float(input("What is your first number?:"))
for operation in operations:
    print(operation)
while calculator_running:
    operation = input("Pick your operation:")
    if operation in operations:
        number_2 = float(input("What is your next number?:"))
        if operation == "+":
            new_number = number_1 + number_2
        if operation == "-":
            new_number = number_1 - number_2
        if operation == "/":
            new_number = number_1 / number_2
        if operation == "*":
            new_number = number_1 * number_2
        print(f"Result:{new_number}")
        number_1 = new_number
    else:
        print("Wrong operation please type again!")
    resume_calcuator = input("Continue operations with result? Type y or n:")
    if resume_calcuator == "n":
        calculator_running = False