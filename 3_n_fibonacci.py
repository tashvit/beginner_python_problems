# Fibonacci Sequence
# Enter a number and have the program generate the Fibonacci sequence
# to that number or to the Nth number


def compute_f(n):
    a = 0
    b = 1
    fibonacci = []
    for i in range(n):
        fibonacci.append(str(a))
        a, b = b, a + b
        i += 1
    output = ','.join(fibonacci)
    print(output)


while True:
    try:
        number = int(input("How many digits do you need?  "))
        if number > 500:
            print("Enter a number smaller than 500")
            continue
    except:
        print("Input must be a number")
        continue
    else:
        compute_f(number)
        break
