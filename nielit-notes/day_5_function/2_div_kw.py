dn=int(input('Please enter the divident : '))
ds=int(input('Please enter the divisor : '))

def div_f(**kwargs):
 a, b= kwargs.values()
 return divmod(a,b)

q, r = div_f(a=dn, b=ds)

print 'The quotient is ', q, ' and the remainder is ', r
