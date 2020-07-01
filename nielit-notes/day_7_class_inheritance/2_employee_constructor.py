class emp:
 no = 0
 def __init__(self, name, salary):
  emp.no = emp.no+1
  self.name = name
  self.salary = salary
 def show_details(self):
  print(emp.no)
  print(self.name)
  print(self.salary)

ram = emp('Ram', '10000')
ram.show_details()

tom = emp('Tom', '20000')
tom.show_details()
