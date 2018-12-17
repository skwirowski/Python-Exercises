# Write a program that is:
#   - printing request for name and surname,
#   - getting these two texts from user,
#   - printing welcome message using received values.
# Input your first name:
# Paweł
# Input your second name:
# Skwirowski
# Welcome Paweł Skwirowski


def main():
    get_first_name = input("Input your first name: ")
    get_last_name = input("Input your last name: ")
    print("Welcome " + get_first_name + " " + get_last_name)


if __name__ == "__main__":
    main()
