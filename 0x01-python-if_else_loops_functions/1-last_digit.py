#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberx = abs(number) % 10
if number < 0:
	number = -number
print(f"Last digit of {} is {} and is ", end='')
if numberx == 0:
    print(f"0")
elif numberx > 6:
   print(f"greater than 5")
else:
    print(f"less than 6 and not 0")
