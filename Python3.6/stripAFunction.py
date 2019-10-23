def simple():
    print("I'm a function")

simple()

def gbp_to_usd(gbp):
    usd = gbp*1.5
    print(usd)

gbp_to_usd(5)

def printname(name):
    print(name)

printname("Roberto")

def printname(*name):
    print(name)

printname("Roberto", "Gianotto")