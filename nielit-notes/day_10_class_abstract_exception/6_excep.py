def ex(cls, no = 0):
 print(no*'-', cls.__name__)
 for cl in cls.__subclasses__():
  ex(cl, no+2)

ex(BaseException)
