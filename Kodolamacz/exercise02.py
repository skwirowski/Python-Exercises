# Write a program that is:
#   - a simple calculator
#   - printing request for first number, mathematical operator nad another number,
#   - getting these three arguments from user,
#   - printing calculation result based on inputted arguments.
#   - asking if user wants to perform another operation or not
# Input in separate lines number, mathematical operation: +, -, *, /, %, and another number:
# 50
# /
# 20
# Your result is: 2.5
# Do you want to perform another operation? Type y (yes) or n (not).

# Additionally I added incorrect input values handling:
#   - first and last argument need to be integer type
#   - second argument need to be valid mathematical operator
#   - last argument can't be equal 0 (dividing by 0 not allowed)


def main():
    end = False

    while not end:
        print("Input in separate lines integer, mathematical operation: +, -, *, /, %, and another integer:")
        while True:
            try:
                first_number = int(input())
                break
            except ValueError:
                print("Sorry, I didn't understand that. Try again.")
                continue

        while True:
            math_operator = input()
            math_operators_arr = ["+", "-", "*", "/", "%"]
            if math_operator in math_operators_arr:
                break
            else:
                print("It is incorrect operator. Try again.")
                continue

        while True:
            try:
                second_number = int(input())
            except ValueError:
                print("Sorry, I didn't understand that. Try again.")
                continue
            if second_number == 0:
                print("You can't divide by 0. Try something else.")
            else:
                break

        if math_operator == "+":
            calculation = first_number + second_number
        elif math_operator == "-":
            calculation = first_number - second_number
        elif math_operator == "*":
            calculation = first_number * second_number
        elif math_operator == "/":
            calculation = first_number / second_number
        else:
            calculation = first_number % second_number

        print(f'Your result is: {calculation}')
        print("Do you want to perform another operation? Type y (yes) or n (not).")
        another_operation = input()
        if another_operation == "n":
            end = True
        elif another_operation != "y":
            print("Invalid input")
            break


if __name__ == "__main__":
    main()
