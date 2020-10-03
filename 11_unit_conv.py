# Converts various units between one another.
# The user enters the type of unit being entered,
# the type of unit they want to convert to and then the value.
# The program will then make the conversion.
# temp, currency, volume


# List of units
units = ["temperature", "currency", "volume"]


def get_user_input():
    """Function to get user input"""
    print("Convert units between one another.")
    input_unit = None
    while input_unit not in units:
        input_unit = input("Pick type of unit to convert.\n"
                           "(Temperature, Currency, Volume, Mass, Length)\n : ").lower()
    return input_unit


def temperature():
    """
    Function to convert temperature units
    Celsius/Fahrenheit
    """

    temp_unit = None
    while (temp_unit != "1") and (temp_unit != "2"):
        temp_unit = input("Celsius -> Fahrenheit. Enter 1.\n"
                          "Fahrenheit -> Celsius. Enter 2.\n : ")
    while True:
        try:
            temp_value = int(input("Enter value to be converted: "))
        except ValueError:
            print("Input must be a number")
        else:
            break
    if temp_unit == "1":
        return f"{temp_value} Celsius = {(temp_value * 9/5) + 32} Fahrenheit"
    else:
        return f"{temp_value} Fahrenheit = {(temp_value - 32) * 5/9} Celsius"


def currency():
    """
    Function to convert currency units
    USD/GBP
    """
    currency_unit = None
    while (currency_unit != "1") and (currency_unit != "2"):
        currency_unit = input("Dollar -> Pound. Enter 1.\n"
                              "Pound -> Dollar. Enter 2.\n : ")
    while True:
        try:
            currency_value = int(input("Enter value to be converted: "))
        except ValueError:
            print("Input must be a number")
        else:
            break
    if currency_unit == "1":
        return f"{currency_value} dollars = {currency_value * 0.78} pounds"
    else:
        return f"{currency_value} pounds = {currency_value * 1.28} dollars"


def volume():
    """
    Function to convert volume units
    Litres/Millilitres
    """
    volume_unit = None
    while (volume_unit != "1") and (volume_unit != "2"):
        volume_unit = input("Litres -> Millilitres. Enter 1.\n"
                            "Millilitres -> Litres. Enter 2.\n : ")
    while True:
        try:
            volume_value = int(input("Enter value to be converted: "))
        except ValueError:
            print("Input must be a number")
        else:
            break
    if volume_unit == "1":
        return f"{volume_value} Litres = {volume_value * 1000} Millilitres"
    else:
        return f"{volume_value} Millilitres = {volume_value / 1000} Litres"


user_unit = get_user_input()
if user_unit == units[0]:
    print(temperature())
if user_unit == units[1]:
    print(currency())
if user_unit == units[2]:
    print(volume())
