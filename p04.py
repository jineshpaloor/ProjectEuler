"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# def is_palindrome(number):
    # n = number
    # pal = 0
    # while n > 0:
        # rem = n % 10
        # pal = pal * 10 + rem
        # n = n / 10
#
    # if pal == number:
        # return True
    # else:
        # return False

def is_palindrome(number):
    # http://www.stealthcopter.com/blog/2009/09/python-palindrome-checking-function/
    num_str = str(number)
    num_len = len(num_str) / 2
    if num_str[:num_len] == num_str[num_len:][::-1]:
        return True
    return False

def main():
    palindroms = []
    for i in reversed(xrange(111,999)):
        for j in reversed(xrange(111,999)):
            product = i * j
            if is_palindrome(product):
                palindroms.append(product)

    print max(palindroms)

if __name__ == '__main__':
    main()
