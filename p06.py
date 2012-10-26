"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def square_of_sum(n):
    return sum(range(n+1)) * sum(range(n+1))

def sum_of_squares(n):
    return sum([x*x for x in range(n+1)])

def main():
    print square_of_sum(10) - sum_of_squares(10)
    print square_of_sum(100) - sum_of_squares(100)

if __name__ == '__main__':
    main()

