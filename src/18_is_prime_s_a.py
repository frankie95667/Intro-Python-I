import sys
import datetime

def SieveOfAtkin(limit):
    if limit > 2:
        print(2, end = " ")
    if limit > 3:
        print(3, end = " ")

    sieve = [False] * limit

    x = 1
    while x * x < limit:
        y = 1
        while y * y < limit:
            n = (4 * x * x) + (y * y)
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^- True
            n = (3 * x * x) - (y * y)
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = True
            y += 1
        x += 1
    
    r = 5
    while r * r < limit:
        if sieve[r]:
            for i in range(r * r, limit, r * r):
                sieve[i] = False

    for a in range(5, limit):
        if sieve[a]:
            print(a, end = " ")

num = int(sys.argv[1])
date = datetime.datetime
start = date.now().timestamp()

SieveOfAtkin(num)

end = date.now().timestamp()
total = end - start
print("Total time is %ds" % total)