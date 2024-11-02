import string
import sys


char_list = list(string.ascii_lowercase + string.punctuation)
number_list = list(string.digits)

def main():
    try:
        plate = input("Plate: ")
    except KeyboardInterrupt:
        print("Terminated by user")
        sys.exit()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(sentence):
    if not sentence[0:2].isalpha():
        return False

    for char in sentence:
        if char in char_list:
            return False

    if (len(sentence) > 6):
        return False
    elif (len(sentence) < 2):
        return False
    
    seen_number = False
    for char in sentence:
        if char.isdigit():
            if not seen_number and char == "0":
                return False
            seen_number = True

        elif seen_number:
            return False
    
    return True


if __name__ == "__main__":
    main()