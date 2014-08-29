#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:        test
# Purpose:
#
# Author:      ZWW
#
# Created:     28/12/2013
# Copyright:   (c) ZWW 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import psutil
import os
import types

def is_process_running(pid):
    if type(pid) is types.IntType:
        resultStr = os.popen('tasklist /FI "PID eq %d"'%pid)
    elif type(pid) is types.StringType:
        resultStr = os.popen('tasklist /FI "PID eq %s"'%pid)
    else:
        return False
    #for line in os.popen("ps xa"):
    for line in resultStr:
        #fields = line.split()
        #pid = fields[0]
        #process = fields[4]
        #if process.find(processname) > 0:
        print line
        print line.find(str(pid))
        if line.find(str(pid)) > 0:
            return True
    return False

for i in psutil.get_process_list():
    print i.name,i.pid

##p = psutil.Process(7055)
##print p.pid
##print p.name
##print p.get_cpu_percent()

res=is_process_running(15944)
print "find result:"
print res

res=is_process_running("123")
print "find result2:"
print res

print type(123)
if type(123) is types.IntType:
    print "haha"