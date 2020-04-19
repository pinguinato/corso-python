def get_doppio_gen():
    e = 2
    while (e < 300):
        yield e
        e *= 2


testgen = get_doppio_gen()
print(testgen)
print(next(testgen))
print(next(testgen))
print(next(testgen))
print(next(testgen))
print(next(testgen))
print(next(testgen))
print(next(testgen))
print(next(testgen))

testgen2 = get_doppio_gen()
print(testgen2)
print(testgen2.__next__())
print(testgen2.__next__())
print(testgen2.__next__())
print(testgen2.__next__())
print(testgen2.__next__())
print(testgen2.__next__())
print(testgen2.__next__())
print(testgen2.__next__())


def get_doppio_gen2():
    e = 2
    while (True):
        yield e
        e *= 2
        if (e >= 300):
            return


testgen3 = get_doppio_gen2()
for el in testgen3:
    print(el)
