import sys

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

 def set_details(self, name, add):
  print('Changing details ... ')
  self.name = name
  self.add = add
  print('Details changed \n')

 def get_details(self):
  print('Name : ' + self.name + '\nAddress : ' + self.add + '\nAccount Type : ' + self.acc_type + '\nAccount No. : ' + str(self.no) + '\n')

list_of_acc = {}

while(True):

 print("Please enter : ")
 print("1. To set up account")
 print("2. To see the account details")
 print("3. To deposit money")
 print("4. To withdraw money")
 print("5. To change the account details")
 print("6. To exit")

 inp = int(raw_input())
 print('You have entered the option '+str(inp)+'\n') 

 if(inp==1):

  a_name = raw_input("Enter your name : ")
  a_add = raw_input("Enter your address : ")
  a_type = raw_input("Enter the account type : ")
  a_acc_no = raw_input("Enter a account no. :")
  a_balance = 0
    
  acnt = acc(a_acc_no, a_balance, a_type, a_name, a_add)
  list_of_acc[a_acc_no] = acnt

 elif(inp==2):
  a_no = raw_input("Enter your account no : ")
  list_of_acc[a_no].get_details()

 elif(inp==3): 
  a_no = raw_input("Enter your account no : ")
  a_amnt = raw_input("Enter the amount : ")
  list_of_acc[a_no].deposit(int(a_amnt))

 elif(inp==4):
  a_no = raw_input("Enter your account no : ")
  a_amnt = raw_input("Enter the amount : ")
  list_of_acc[a_no].withdraw(int(a_amnt))

 elif(inp==5): 
  a_no = raw_input("Enter your account no : ")
  a_name = raw_input("Enter your new name : ")
  a_add = raw_input("Enter your new address : ")
  list_of_acc[a_no].set_details(a_name, a_add)

 elif(inp==6):
  break

 else:
  pass	
