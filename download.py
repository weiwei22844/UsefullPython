#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:      ZWW
#
# Created:     17/02/2014
# Copyright:   (c) ZWW 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib
import os
def Schedule(a,b,c):
    '''''
    '''
    per =100.0*a *b /c
    if per > 100:
        per =100
    print'a: %d b: %d c: %d %.2f%%'%(a,b,c,per)

#url ='http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
#url = 'http://support.dualminer.com/wp-content/uploads/2014/01/DualMinerSetup-1.0.0.6.zip'
url = "http://support.dualminer.com/update/"
local =os.path.join('d:','tmp')
#urllib.urlretrieve(url,local,Schedule)

fileName=urllib.urlopen("http://support.dualminer.com/update/newVersion.txt").read()
print fileName
urllib.urlretrieve("http://support.dualminer.com/update/a"+fileName,"GuiSetup.exe",Schedule)