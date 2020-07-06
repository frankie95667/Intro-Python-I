import sys
import datetime

def is_prime(num, pow = 1):
    for i in [j + 1 for j in range(1, num**pow - 1)]:
        if(num % i == 0):
            return False
    return True


num = int(sys.argv[1])
pow = int(sys.argv[2])
date = datetime.datetime
start = date.now().timestamp()

print(is_prime(num, pow))

end = date.now().timestamp()
total = end - start
print("Total time is %ds" % total)
