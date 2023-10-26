# Artem Antonian
def decode(to_decode):
    new_password = ""
    for i in to_decode:
        if int(i) > 2:
            decoded_num = str(int(i) - 3)
        elif int(i) == 0:
            decoded_num = "7"
        elif int(i) == 1:
            decoded_num = "8"
        elif int(i) == 2:
            decoded_num = "9"
        new_password += decoded_num
        return new_password
