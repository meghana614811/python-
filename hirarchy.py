class Alpha:
    def fun1(self):
        print("I am an Alpha")
class Beta(Alpha):
    def fun2(self):
        print("I am Beta")
class gamma(Alpha):
    def fun3(self):
        print("I am Gamma")
b=Beta()
b.fun1()
b.fun2()

