class DClass:
    def xfunc(self):
        print("Sono metodo xFunc definito dentro DClass")


class BClass(DClass):
    pass


class CClass:
    pass


class AClass(CClass, BClass):
    pass


a = AClass()
a.xFunc()