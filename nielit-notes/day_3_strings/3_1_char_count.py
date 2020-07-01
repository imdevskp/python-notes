word = raw_input('Please enter the word: ')
char = raw_input('Please enter the character: ')
char_count = 0
for i in word:
 if i==char:
  char_count=char_count+1 
print('There are '+str(char_count)+' '+char+' in the word '+word)
