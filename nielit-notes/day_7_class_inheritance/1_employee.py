class emp:
 no = 0
 def store_details(self):
  emp.no = emp.no+1
  self.name = raw_input('Enter the name : ')
  self.salary = raw_input('Enter the salary : ')
 def show_details(self):
  print(emp.no)
  print(self.name)
  print(self.salary)

ram = emp()
ram.store_details() 
ram.show_details()

tom = emp()
tom.store_details()
tom.show_details()
