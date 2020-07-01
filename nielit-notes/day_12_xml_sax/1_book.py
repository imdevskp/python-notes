import xml.sax
open('book.txt', 'w').write('')

class myh(xml.sax.ContentHandler):
 n = 0
 def __init__(self):
  self.curtag = ''
  self.cat = ''
  self.title = ''
  self.author = ''
  self.year = ''
  self.price = ''
  myh.n = myh.n+1

 def startElement(self, tag, attrs):
  self.curtag = tag
  if tag == 'book':
   print(attrs['category'])
   self.cat = attrs['category']

 def characters(self, content):
  if self.curtag == 'title':
   self.title = content
  if self.curtag == 'author':
   self.author = content
  if self.curtag == 'year':
   self.year = content
  if self.curtag == 'price':
   self.price = content

 def endElement(self, tag):
  
  f = open('book.txt', 'a')
     
  if self.curtag == 'title':
   print('Title : '+self.title)
   f.write(str(self.n) + '.The book '+ self.title + ' category : '+self.cat + ' belongs to '+ self.cat) 
  if self.curtag == 'author':
   print('Author : '+self.author)
   f.write(' category and is written by ' + self.author) 
  if self.curtag == 'year':
   print('Year : '+self.year)
   f.write( '. This book is published in the year '+ str(self.year))
  if self.curtag == 'price':
   print('Price : '+ self.price)
   f.write(' with price of '+ str(self.price)+'\n')

po = xml.sax.make_parser()
po.setContentHandler(myh())
f = po.parse('book.xml')

