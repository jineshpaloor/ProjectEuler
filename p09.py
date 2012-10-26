"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

#pyth_triples = [(a, b, c) for a in xrange(1, 1001) for b in xrange(a, 1001) for c in xrange(b, 1001) if a*a + b*b == c*c]
#
#for i in pyth_triples:
#    if sum(i) == 1000:
#        print i[0] * i[1] * i[2]
#        break

def main():
    s = 1000
    for a in range(3, (s-3)/3 + 1):
        for b in range(a+1, (s-1-a)/2 + 1):
            c = s-a-b
            if c*c == a*a + b*b:
                print (a,b,c)
                print a*b*c

if __name__ == '__main__':
    main()

