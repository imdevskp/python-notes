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
mdt1=dt.datetime(2019,12,20,17,5,tzinfo=dt.timezone.utc)
mdt2=dt.datetime(2019,12,20,17,5,tzinfo=mtzo)
print('mdt1=',mdt1.ctime())
print('mdt2=',mdt2.ctime())
print(mdt1.utcoffset())
print(mdt2.utcoffset())
nmdt1=dt.timezone.utc.fromutc(mdt1)
nmdt2=mtzo.fromutc(mdt2)
print('nmdt1=',nmdt1.ctime())
print('nmdt2=',nmdt2.ctime())
print('nmdt1==nmdt2:',nmdt1==nmdt2)
