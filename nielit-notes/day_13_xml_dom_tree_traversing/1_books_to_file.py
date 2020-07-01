import xml.dom.minidom as dm

dtree=dm.parse('book.xml')

rnode=dtree.documentElement
f=open('book1.txt','a')

bns=rnode.getElementsByTagName('book')
for bn in bns:
 if bn.hasAttribute('category'):
  cat=bn.getAttribute('category')

 tns=bn.getElementsByTagName('title')
 for tn in tns:
  f.write('The book '+tn.childNodes[0].nodeValue+' belongs to '+cat+' category')

 ats= bn.getElementsByTagName('author')
 for tn in ats:
  f.write(' and is written by '+tn.childNodes[0].nodeValue)

 year= bn.getElementsByTagName('year')
 for tn in year:
  f.write('. This book is published in the year '+tn.childNodes[0].nodeValue)

 prc= bn.getElementsByTagName('price')
 for tn in prc:
  f.write(' with a price of '+tn.childNodes[0].nodeValue+'.\n')
