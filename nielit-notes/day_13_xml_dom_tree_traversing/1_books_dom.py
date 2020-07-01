import xml.dom.minidom as dm
dtree = dm.parse('book.xml')

rnode = dtree.documentElement
bns = rnode.getElementsByTagName('book')

for bn in  bns:
 
  if bn.hasAttribute('category'):
    cat = bn.getAttribute('category')

  tns = bn.getElementsByTagName('title')
  for tn in tns:
    print(tn.nodeName, ' : ', tn.childNodes[0].nodeValue)

  ats = bn.getElementsByTagName('author')
  for tn in ats:
    print(tn.nodeName, ' : ', tn.childNodes[0].nodeValue)

  yrs = bn.getElementsByTagName('year')
  for tn in yrs:
    print(tn.nodeName, ' : ', tn.childNodes[0].nodeValue)

  prs = bn.getElementsByTagName('price')
  for tn in prs:
    print(tn.nodeName, ' : ', tn.childNodes[0].nodeValue)



