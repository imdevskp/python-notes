class Emp:
 no = 0
 def __init__(self, name, bsal):
  Emp.no = Emp.no+1
  self.name = name
  self.bsal = bsal
 def details(self):
  return 'The name of the Employee is ' + str(self.name) + ' with a base salery of ' + str(self.bsal)

class Sci(Emp):
 def __init__(self, name, bsal, t_all, cat):
  super(Sci, self).__init__(name, bsal)
  self.t_all = t_all
  self.cat = cat

class Officer(Emp):
 def __init__(self, name, bsal, grade, dept):
  super(Officer, self).__init__(name, bsal)
  self.grade = grade
  self.dept = dept

ram = Emp('Ram', 10000)
print(ram)
print(ram.name)
print(ram.details())

raj = Sci('Raj', 10000, 100, 'Junior')
print(raj)
print(raj.cat)
print(raj.details())

jobs = Officer('Jobs', 20000, 'B', 'IT')
print(jobs)
print(jobs.grade)
print(jobs.details())
