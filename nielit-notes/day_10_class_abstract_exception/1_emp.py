from abc import ABC, abstractmethod

class Emp(ABC):
 no = 0
 @abstractmethod
 def __init__(self, name, bsal):
  Emp.no = Emp.no+1
  self.name = name
  self.bsal = bsal
  self.da = 0.3
  self.hra = 0.1

class Engineer(Emp):
 @abstractmethod
 def __init__(self, name, bsal):
  super(Engineer, self).__init__(name, bsal)
  self.sp = 0.2

class Officer(Emp):
 def __init__(self, name, bsal):
  super(Officer, self).__init__(name, bsal)
  self.sp = 0.1

 def __str__(self):
  return 'Officer {}  with id {}  has a salary of {}'.format(self.name, self.no, self.bsal + (self.bsal*self.da) + self.bsal*self.hra)

class Jr_Eng(Engineer):
 def __init__(self, name, bsal):
  super(Jr_Eng, self).__init__(name, bsal)
  self.ad = 500
 def __str__(self):
  return 'Jr. Engineer {} with id {} has a salary of {}'.format(self.name, self.no, self.bsal + (self.bsal*self.da) + (self.bsal*self.hra) + (self.bsal*self.sp) + self.ad)

class Sr_Eng(Engineer):
 def __init__(self, name, bsal):
  super(Sr_Eng, self).__init__(name, bsal)
  self.ad = 1000
 def __str__(self):
  return 'Sr. Engineer {} with id {} has a salary of {}'.format(self.name, self.no, self.bsal + (self.bsal*self.da) + (self.bsal*self.hra) + (self.bsal*self.sp) + self.ad)

ram = Officer('Ram', 10000)
print(ram)

bill = Jr_Eng('Bill', 10000)
print(bill)

jobs = Sr_Eng('Jobs', 10000)
print(jobs)

bing = Emp('Bing', 10000)
print(bing)
