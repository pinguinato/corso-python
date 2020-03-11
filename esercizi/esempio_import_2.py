import math

# definisco una mia fuzione pi(x)
def sin(x):
    if 2 * x == pi:
        return 0.9999999
    else:
        return None

pi = 3.14

# uso il mio namespace
print(sin(pi/2))
# uso il namespace di math
print(math.sin(math.pi/2))
