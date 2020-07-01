sent = raw_input("Please input the sentance : ")
sent_split = sent.split()

pal_count = 0
flag = 0

for i in sent_split:
 if(len(i)>2):
  for j in range(int(len(i)/2)):
   if i[j]!=i[-(j+1)]:
    break
  else:
   flag = flag+1
   
print(flag) 

  
