word = raw_input('Please enter the word: ')
v=0
for i in word:
 if i in ('a','e','i','o','u'):
  v=v+1
if(v>=2):
 print("There are more than two alpahets in "+word)
else:
 print("No. There is less than two alphabets in "+word)   
