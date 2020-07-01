import abc

class Vehicle:
 from datetime import datetime
 c_yr = datetime.now().year
 
 def __init__(self, name, veh_no, no_wheels, y_o_make, b_price):
  self.name = name
  self.veh_no = veh_no
  self.no_wheels = no_wheels
  self.year_of_make = y_o_make
  self.buying_price = b_price
  self.pres_value = 0

 __metaclass__=abc.ABCMeta
 def pres_val(self): 
  pass


class Car(Vehicle):
 def __init__(self, name, veh_no, no_wheels, year_of_make, buying_price):
  super(Car, self).__init__(name, veh_no, no_wheels, year_of_make, buying_price)
  
 @abc.abstractmethod
 def pres_val(self): 
  self.pres_value =  self.buying_price-(self.c_yr-self.year_of_make)*5000
  return  self.pres_value


class Bus(Vehicle):
 def __init__(self, name, veh_no, no_wheels, year_of_make, buying_price):
  super(Bus, self).__init__(name, veh_no, no_wheels, year_of_make, buying_price)
 
 @abc.abstractmethod
 def pres_val(self): 
  self.pres_value =  self.buying_price-(self.c_yr-self.year_of_make)*1000
  return  self.pres_value


class Truck(Vehicle):
 def __init__(self, name, veh_no, no_wheels, year_of_make, buying_price):
  super(Truck, self).__init__(name, veh_no, no_wheels, year_of_make, buying_price)
 
 @abc.abstractmethod
 def pres_val(self): 
  self.pres_value =  self.buying_price-(self.c_yr-self.year_of_make)*1000
  return  self.pres_value



alto = Car('alto', 1234, 4, 2009, 100000)
print(alto.name)
print(alto.pres_val())

tata = Bus('tata', 3489, 6, 2017, 1000000)
print(tata.name)
print(tata.pres_val())

asok = Truck('asok', 9345, 8, 2014, 800000)
print(asok.name)
print(asok.pres_val())

