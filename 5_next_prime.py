# Next Prime Number
# Have the program find prime numbers until the user
# chooses to stop asking for the next one.

x = 0

# checking if a number is a prime factor
def check_if_prime(n):
    if n == 0 or n == 1:
        return False
    div = [x for x in range(2, n) if n % x == 0]
    return len(div) == 0


# returns next prime number
def get_next_prime(number):
    global x
    while not check_if_prime(number):
        number += 1
    x = number + 1
    return number


# get user input
def ask_user_input():
    print_primes = None
    while print_primes != 'y' and print_primes != 'n':
        print_primes = input('Print next prime number? Y/N? ').lower()
        if print_primes != 'y' and print_primes != 'n':
            print('Enter "Y" to see next prime number or "N" to quit.')
    return print_primes


# have the program find prime numbers until the user chooses to stop asking for the next one
while True:
    user_request = ask_user_input()
    if user_request == 'y':
        print(get_next_prime(x))
        print('\n')
        continue
    else:
        break