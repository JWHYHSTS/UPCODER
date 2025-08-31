import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
n = int(data[0]); length = int(data[1])

print(n ** length)

def gen(rem, prefix):
    if rem == 0:
        print(prefix)
        return
    for i in range(1, n + 1):
        gen(rem - 1, prefix + str(i))

gen(length, "")