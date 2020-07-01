import sys




while(True):

 print "1-Initialize, \n2-Show, \n3-Reload, \n4-Exit\n"
 inp = int(raw_input())
 print inp, ' is the input'

 try:
  if(inp==1):
   print 'Importing library var_file as v'
   import var_file as v
   print 'Library imported \n'

  elif(inp==2):
   print 'Finding the value of control variable'
   con = v.a+(10*v.b*v.c)-((5*v.d)/v.e)
   print 'Value of control variable is ', con, '\n'

  elif(inp==3):
   print 'Reloading v module'
   reload(v)
   print 'v module reloaded \n'

  elif(inp==0):
   print 'Terminating  program \n'
   break

  else:
   print 'Invalid input'

 except:
  print('\n Please import library first \n')
