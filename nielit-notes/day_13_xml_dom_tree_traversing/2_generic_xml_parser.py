import xml.dom.minidom as dm

dtree = dm.parse('book.xml')
rnode = dtree.documentElement

def fn(n):

 if n.nodeType == 3:
  if(not(n.nodeValue.isspace())):
     print(n.parentNode.nodeName, ' : ', n.nodeValue)

 else:
   for cn in n.childNodes:
     if cn.nodeType == 1:
       for k in cn.attributes.keys():
         print(cn.attributes[k].name, ' : ', cn.attributes[k].value)  
     fn(cn)

fn(rnode)

#        for chn in bn.childNodes:
#          for tn in chn.childNodes:
#           print(tn.parentNode.nodeName, ' : ', tn.nodeValue)
