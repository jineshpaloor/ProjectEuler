"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def largest_prime_factor(n):
    # divide number by smallest prime
    # if we can divide perfectly it is a prime factor.
    # divide the result again starting from smallest prime factor
    # else divide the number by next smallest prime number

    prime_numbers = primes(7000)
    i = 0 # prime number index
    factors = []
    while n != 1:
        if n % prime_numbers[i] == 0:
            n = n / prime_numbers[i]
            factors.append(prime_numbers[i])
        else:
            i += 1
    return factors

def main():
    print max(largest_prime_factor(600851475143))

if __name__ == "__main__":
    main()
