"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
def main():
    MAX = 2000001
    numbers = [True] * MAX
    numbers[0] = numbers[1] = False
    primes = []

    for number,is_prime in enumerate(numbers):
        if is_prime:
            primes.append(number)
            for i in range(number+number, MAX, number):
                numbers[i] = False
    print sum(primes)

if __name__ == "__main__":
    main()
