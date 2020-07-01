class acc:
 no_of_acc = 0

 def __init__(self, no, bal, acc_type, name, add):
  self.no = no
  self.bal = bal
  self.acc_type = acc_type
  self.name = name
  self.add = add
  acc.no_of_acc = acc.no_of_acc+1

 def deposit(self, amount):
  print('Your current balance is '+ str(self.bal))
  print('You are depositing ' + str(amount))
  self.bal = self.bal + amount
  print('Your balance after depositing ' + str(amount) + ' is ' + str(self.bal)+ '\n' )

 def withdraw(self, amount):
  print('Your current balance is '+ str(self.bal))
  print('You are withdrawing ' + str(amount))
  self.bal = self.bal - amount
  print('Your balance after withdrawing ' + str(amount) + ' is ' + str(self.bal) + '\n')

 def set_details(self, no, acc_type, name, add):
  print('Changing details ... ')
  self.name = name
  self.acc_type = acc_type
  self.no = no
  self.add = add
  print('Details changed \n')

 def get_details(self):
  print('Name : ' + self.name + '\nAddress : ' + self.add + '\nAccount Type : ' + self.acc_type + '\nAccount No. : ' + str(self.no) + '\n')

ram = acc(1234, 10000, 'Personal', 'Ram', 'NIT, Calicut')
ram.deposit(2000)
ram.withdraw(1000)
ram.get_details()
ram.set_details(1425, 'Joint', 'Ram Gopal', 'NIELIT, Calicut')
ram.get_details()
