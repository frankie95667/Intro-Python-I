import sys
import datetime

def all_prime(num):
    p = 2
    num_list = list(range(p, num + 1))
    for p in num_list:
        for i in range(p, num + 1):
            try:
                num_list.remove(i*p)
            except:
                pass
    return num_list

num = int(sys.argv[1])
date = datetime.datetime
start = date.now().timestamp()

print(all_prime(num))

end = date.now().timestamp()
total = end - start
print("Total time is %ds" % total)
