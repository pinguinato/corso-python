# un iteratore ha sempre metodo iter e metodo next

class MyIterator:
    def __iter__(self):
        self.myattr = 2
        return self

    def __next__(self):
        if self.myattr < 300:
            n = self.myattr
            self.myattr *= 2
            return n
        else:
            raise StopIteration


iteratore = MyIterator()
testIter = iter(iteratore)

# usando print se ne metto ancora una ottengo l'eccezione StopIteration
print(next(testIter))
print(next(testIter))
print(next(testIter))
print(next(testIter))
print(next(testIter))
print(next(testIter))
print(next(testIter))
print(next(testIter))

# con il for l'eccezione è controllata e non si presenta
for i in testIter:
    print(i)
