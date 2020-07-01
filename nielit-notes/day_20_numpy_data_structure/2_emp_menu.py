import numpy as np

while(True):

  print('''
  a) Initialize
  b) Add new record
  c) Delete a record
  d) Display details by no. & name
  e) Display summary
  f) Save All
  g) Exit\n ''')

  inp = raw_input()
  print('You entered option : {}'.format(inp))

  if(inp=='a'):
    fo = open('emp.csv', 'r').readlines()
    print('File imported')

    recs = [tuple(i[:-1].split(',')) for i in fo]

    dt = np.dtype([('ename', 'U20'), ('eno', 'int'), ('edesignation', 'U20'), ('esal', 'f8'), ('ephone', 'U20')])
    emp_data = np.array(recs[1:], dtype=dt)
    print('File added to numpy array \n')  

    print(emp_data)    

  elif(inp=='b'):
    name = raw_input('Please enter the name : ')
    no = int(raw_input('Please enter the employee no : '))
    des = raw_input('Please enter the designation : ')
    sal = int(raw_input('Please enter the salary : '))
    phone = raw_input('Please enter the phone no. : ')
    
    new_data =  np.array([(name, no, des, sal, phone)], dtype=dt)
    print('New data : {}'.format(new_data))
   
    emp_data = np.concatenate((emp_data, new_data), axis=0)
    print('{}\'s Employee data added'.format(name))
    print(emp_data)

  elif(inp=='c'):
    no = int(raw_input('Please enter the Employee no. that you want to remove : '))
    emp_data = emp_data[emp_data['eno']!=no]
    print('Updated Data')
    print(emp_data)

  elif(inp=='d'):
    no = int(raw_input('Please enter the Employee No. : '))
    name = raw_input('Please enter the Employee name. : ')
    print(emp_data[np.logical_and(emp_data['eno']==no, emp_data['ename']==name)])

  elif(inp=='e'):
    print('Number of Employees')
    print(emp_data.shape[0])
    print('Sum of salary')
    print(np.sum(emp_data['esal']))
    
  elif(inp=='f'):
    print('Saving the numpy arry')
    data = np.asarray(emp_data)
    print(data)
    np.savetxt('emp_updated.csv', data, delimiter=',', fmt='%s, %s, %s, %s, %s')
    print('Saved to csv file')

  elif(inp=='g'):
    print('Exiting Program')
    break

  else:
    print('Invalid Input')    
