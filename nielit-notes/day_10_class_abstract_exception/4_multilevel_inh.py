class Base1():
 val1 = 1

class Base2(Base1):
 val2 = 2

class Derived(Base2):
 pass

val = Derived()
print(val.val1)
print(val.val2)
