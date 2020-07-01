#!/usr/bin/env python4
import datetime as dt
class my_tz(dt.tzinfo):
 def utcoffset(self,pdt):
  return dt.timedelta(hours=5,minutes=30)
 def fromutc(self,pdt):
  return pdt+dt.timedelta(hours=5,minutes=30)
 def dst(self,pdt):
  return dt.timedelta(0)
 def tzname(self,pdt):
  return '+05:30'
mtzo=my_tz()
#mdt1=dt.datetime(2019,12,20,17,5)
#mdt2=dt.datetime(2019,12,20,17,5,tzinfo=mtzo)
#print('mdt1=',mdt1.ctime())
#print('mdt2=',mdt2.ctime())
#print(mdt1.utcoffset())
#print(mdt2.utcoffset())
#print(mtzo.fromutc(mdt2).ctime())
##dt1=dt.datetime.now()
##dt2=dt.datetime.utcnow()
##print('dt1ts:',dt1.timestamp())
##print('dt2ts:',dt2.timestamp())
dt1=dt.datetime.now(tz=dt.timezone.utc)
dt2=dt.datetime.now(tz=mtzo)
print('dt1',dt1.ctime())
print('dt2',dt1.ctime()) 
print('dt1ts:',dt1.timestamp())
print('dt2ts:',dt2.timestamp())
mdt1=dt1.tzinfo.fromutc(dt1)
mdt2=dt2.tzinfo.fromutc(dt2)
print('mdt1',dt1.ctime())
print('mdt2',dt1.ctime()) 
print('mdt1ts:',mdt1.timestamp())
print('mdt2ts:',mdt2.timestamp())

