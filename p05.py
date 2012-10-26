"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

divisible = True
n = 2520
while divisible:
    for i in range(11,20):
#    for i in [11,13,15,17,19]:
        if n % i != 0:
            divisible = False
    if divisible:
        print n
        exit(0)
    else:
        n = n + 2520
    divisible = True

