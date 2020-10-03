# Prime Factorization
# Have the user enter a number and find all Prime Factors
# (if there are any) and display them.


# checking if a number is a prime factor
def check_if_prime(n):
    if n == 0 or n == 1:
        return False
    div = [x for x in range(2, n) if n % x == 0]
    return len(div) == 0

# finding all prime factors
def find_primes(n):
    primes = [str(y) for y in range(2, n+1) if check_if_prime(y) == True]
    print(','.join(primes))


while True:
    try:
        number = int(input("Enter a number to see all prime factors: "))
    except ValueError:
        print("Input must be an integer")
    except:
        print("Input must be a positive integer")
    else:
        find_primes(number)
        break