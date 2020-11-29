import sys
import time

print('FORVER ECHO UP')
while True:
    # time.sleep(1)
    # print('xDDDD', end='xd')
    # continue

    echo = input()
    for c in echo:
        print(c, end='')
        sys.stdout.write(c)
        sys.stdout.flush()
