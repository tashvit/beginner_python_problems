# Develop a converter to convert a decimal number to binary
# or a binary number to its decimal equivalent.

def get_input():
    x = None
    while x != "a" and x != "b":
        x = input("Decimal to Binary -> enter 'a'\nBinary to Decimal -> enter 'b'\n ").lower()
    return x


def dec_to_bin():
    number = int(input("Enter decimal number: "))
    binary = []
    while number // 2 != 0:
        binary.append(str(number % 2))
        number = number // 2
    binary.append(str(number % 2))
    binary.reverse()
    print(''.join(binary))


def check_if_binary():
    number = int(input("Enter binary number: "))
    for i in str(number):
        if i in '10':
            is_binary = True
        else:
            is_binary = False
            break
    if is_binary:
        return number
    print("Not a binary number")


def bin_to_dec(number):
    bin_list = [int(x) for x in str(number)]
    bin_list.reverse()
    total = 0
    for (i, x) in enumerate(bin_list):
        total += pow(2,i) * x
    print(total)


user_input = get_input()
if user_input == "a":
    dec_to_bin()
else:
    bin_num = check_if_binary()
    bin_to_dec(bin_num)