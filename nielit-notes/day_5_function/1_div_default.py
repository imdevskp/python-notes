dn=int(input('Please enter the divident : '))
ds=int(input('Please enter the divisor : '))

def div_f(divident, divisor=2):
 return divmod(divident, divisor)

q, r = div_f(dn, ds)
print "Quotient is : ", q, " and the reminder is ", r
