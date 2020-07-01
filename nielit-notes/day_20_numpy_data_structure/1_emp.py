import numpy as np

dt = np.dtype([('ename', 'U20'), ('eno', 'int'), ('edesignation', 'U20'), ('esal', 'f8'), ('ephone', 'U20')])

fo = open('emp.csv', 'r').readlines()

recs = [tuple(i[:-1].split(',')) for i in fo]
# print(recs)

print('\n # 1 - all the records')
emp_data = np.array(recs[1:], dtype=dt)
print(emp_data)

print('\n # 2 - names of the officers')
print(emp_data['ename'])

print('\n # 3 - all the scientist records')
sci_data = emp_data[emp_data['edesignation']=='scientist']
print(sci_data)

print('\n # 4 - total salary')
print(np.sum(emp_data['esal']))

print('\n # 5 - avg engg. salary')
print(np.mean(emp_data[emp_data['edesignation']=='engineer']['esal']))

print('\n # 6 - emp.s in ascending order of the salary')
print(np.sort(emp_data, order='esal'))

print('\n # 7 - emps. in ascending order of designation and salary')
print(np.sort(emp_data, order=['edesignation', 'esal']))

print('\n # 8 - lowest salary for scientist')
min_sci_sal = np.min(emp_data[emp_data['edesignation']=='scientist']['esal'])
print(min_sci_sal)

print('\n # 9 - scientist with lowers salary')
print(sci_data[sci_data['esal']==min_sci_sal]) 
