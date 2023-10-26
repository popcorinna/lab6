from decoder import decode


def encode(to_encode):
    s = ""
    for digit in to_encode:
        if int(digit) < 7:
            s = s + str(int(digit) + 3)
        elif int(digit) == 7:
            s = s + "0"
        elif int(digit) == 8:
            s = s + "1"
        else:
            s = s + "2"
    return s


continue_program = True

while continue_program:
    print("Menu\n-------------")
    print("1. Encode\n2. Decode\n3. Quit\n")
    option = int(input("Please enter an option: "))

    if option == 1:
        password = input("Please enter your password to encode: ")
        new_password = encode(password)
        print("Your password has been encoded and stored!\n")
    elif option == 2:
        print(f"The encoded password is {new_password}, and the original password is {decode(new_password)}.\n")
    elif option == 3:
        continue_program = False

