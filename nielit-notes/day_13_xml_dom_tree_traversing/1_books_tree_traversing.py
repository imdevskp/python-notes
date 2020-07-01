import xml.dom.minidom as dm
dtree = dm.parse('book.xml')
rnode = dtree.documentElement
for bn in rnode.childNodes:
  if bn.nodeType == 1:
    for k in bn.attributes.keys():
      print(bn.attributes[k].name, ' : ', bn.attributes[k].value)
  for chn in bn.childNodes:
    for tn in chn.childNodes:
      print(tn.nodeType)
      print(tn.parentNode.nodeName, ' : ', tn.nodeValue)
