#!/usr/bin/env python
# ­­*­­ coding: UTF­8 ­­*­­
import sys, urllib2
req=urllib2.Request(sys.argv[1])
fd=urllib2.urlopen(req)
while 1:
    data=fd.read(1024)
    if not len(data):
        break
    print data
