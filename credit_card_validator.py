# Credit Card Validator - Takes in a credit card number
# from a common credit card vendor
# (Visa, MasterCard, American Express, Discover)
# and validates it to make sure that it is a valid number

# Issuer Identification Numbers (IIN) from https://www.iinbase.com/
# Example credit card numbers for testing --> https://www.validcreditcardnumber.com/

import re


def getnum():
    """
    Function to get card number
    """
    while True:
        try:
            card_num = input("Enter credit card number: ")
            # pattern = r"[^\s]+"
            num = re.findall(r"[^\s]+", card_num)
            number = int("".join(num))
        except ValueError:
            print("Not a number. Try again!")
        else:
            return number


def check_sum(number):
    """
    Checks the number to see if it's valid.
    Returns a boolean
    """
    if len(str(number)) in range(12, 20):
        # Using Luhn's algorithm
        num_reverse = (str(number))[::-1]
        even_nums_doubled = [int(x)*2 for x in num_reverse[1::2]]
        odd_nums = [int(x) for x in num_reverse[0::2]]

        # Adding together any double digits in even_nums_doubled list
        for index, digit in enumerate(even_nums_doubled):
            if digit >= 10:
                even_nums_doubled[index] = (digit // 10) + (digit % 10)

        # Adding together numbers in n1 and n2 lists
        result = sum(even_nums_doubled) + sum(odd_nums)
        return result % 10 == 0
    return False


def find_card_issuer(number):
    if (str(number))[0:2] in ["34", "37"]:
        return "American Express"
    elif int((str(number))[0:3]) in range(300, 306):
        return "Diner's Club Carte Blanche"
    elif (str(number))[0:2] == "36":
        return "Diner's Club International"
    elif (str(number))[0:4] == "6011":
        return "Discover Card"
    elif int((str(number))[0:6]) in range(622126, 622926):
        return "Discover Card"
    elif int((str(number))[0:3]) in range(644, 650):
        return "Discover Card"
    elif (str(number))[0:2] == "65":
        return "Discover Card"
    elif (str(number))[0:3] in ["637", "640"]:
        return "InstaPayment"
    elif int((str(number))[0:4]) in range(3528, 3589):
        return "JCB"
    elif int((str(number))[0:2]) in range(51, 56):
        return "MasterCard"
    elif (str(number))[0] == "4":
        return "Visa"
    else:
        return "Card issuer unknown"


if __name__ == '__main__':
    n = getnum()
    if check_sum(n):
        print("Card number is valid")
        print(f"Card issued by: {find_card_issuer(n)}")
    else:
        print("Invalid card number")
