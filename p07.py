"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def main():
#    n = 6
#    p = 13
#    while n < 10001:
#        p = p + 2
#        is_prime = True
#        for i in range(2,p/2 + 1):
#            if p % i == 0:
#                is_prime = False
#                break
#        if is_prime:
#            n = n + 1
#
#    print p

    MAX = 105000
    numbers = [True] * MAX
    numbers[0] = numbers[1] = False
    primes = []

    for number,is_prime in enumerate(numbers):
        if is_prime:
            primes.append(number)
            if len(primes) == 10001:
                break
            for i in range(number+number, MAX, number):
                numbers[i] = False
    print primes[10000]

if __name__ == "__main__":
    main()
