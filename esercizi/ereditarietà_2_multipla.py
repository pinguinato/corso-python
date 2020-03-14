class BClass:
    def funcBClass(self):
        print("Sono un metodo di BClass")
    def xFunc(self):
        print("Sono xFunc di BClass")

class CClass:
    def funcCClass(self):
        print("Son un metodo di CClass")
    def xFunc(self):
        print("Sono xFunc di CClass")

class AClass(BClass, CClass):
    pass


istanzaAClass = AClass()
istanzaAClass.funcBClass()
istanzaAClass.funcCClass()
istanzaAClass.xFunc()


