import abc

class Vehicle:
 from datetime import datetime
 c_yr = datetime.now().year
 
 __metaclass__=abc.ABCMeta
 def __init__(self, name, veh_no, no_wheels, y_o_make, b_price):
  self.name = name
  self.veh_no = veh_no
  self.no_wheels = no_wheels
  self.year_of_make = y_o_make
  self.buying_price = b_price

class Car(Vehicle):
 @abc.abstractmethod
 def __init__(self, name, veh_no, no_wheels, year_of_make, buying_price):
  super(Car, self).__init__(name, veh_no, no_wheels, year_of_make, buying_price)
  self.pres_value =  self.buying_price-(self.c_yr-self.year_of_make)*5000

class Bus(Vehicle):
 @abc.abstractmethod
 def __init__(self, name, veh_no, no_wheels, year_of_make, buying_price):
  super(Bus, self).__init__(name, veh_no, no_wheels, year_of_make, buying_price)
  self.pres_value =  self.buying_price-(self.c_yr-self.year_of_make)*1000

class Truck(Vehicle):
 @abc.abstractmethod
 def __init__(self, name, veh_no, no_wheels, year_of_make, buying_price):
  super(Truck, self).__init__(name, veh_no, no_wheels, year_of_make, buying_price)
  self.pres_value =  self.buying_price-(self.c_yr-self.year_of_make)*12000

alto = Car('alto', 1234, 4, 2009, 100000)
print(alto.name)
print(alto.pres_value)

tata = Bus('tata', 3489, 6, 2017, 1000000)
print(tata.name)
print(tata.pres_value)

asok = Truck('asok', 9345, 8, 2014, 800000)
print(asok.name)
print(asok.pres_value)

