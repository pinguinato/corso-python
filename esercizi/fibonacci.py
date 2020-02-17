def Fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return Fib(n -1) + Fib(n - 2)


print("Serie Fibonacci del numero 6:\n")
print(Fib(6))