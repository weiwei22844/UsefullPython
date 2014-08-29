#!/usr/bin/env python
# -*- coding: gb2312 -*-
import win32process
import win32api
import win32con
import os
from ctypes import *

#-----------------------------获取当前进程信息模块---------------------------------

class _PROCESS_MEMORY_COUNTERS(Structure):
    _fields_ = [("cb", c_long),
                ("PageFaultCount", c_long),
                ("PeakWorkingSetSize", c_long),
                ("WorkingSetSize", c_long),
                ("QuotaPeakPagedPoolUsage", c_long),
                ("QuotaPagedPoolUsage", c_long),
                ("QuotaPeakNonPagedPoolUsage", c_long),
                ("QuotaNonPagedPoolUsage", c_long),
                ("PagefileUsage", c_long),
                ("PeakPagefileUsage", c_long)]
    def __init__(self, *args, **kw):
        super(_PROCESS_MEMORY_COUNTERS, self).__init__(*args, **kw)
        self.cb = sizeof(self)

def GetProcessInfo():
    print "查询进程"
    arr = c_ulong * 256
    lpidProcess= arr()
    cb = sizeof(lpidProcess)
    cbNeeded = c_ulong()
    cbNeeded = c_ulong()
    hModule = c_ulong()
    count = c_ulong()

    #PSAPI.DLL
    psapi = windll.psapi
    #Kernel32.DLL
    kernel = windll.kernel32
    modname = c_buffer(30)
    PROCESS_QUERY_INFORMATION = 0x0400
    PROCESS_VM_READ = 0x0010

    #Call Enumprocesses to get hold of process id's
    psapi.EnumProcesses(byref(lpidProcess), cb, byref(cbNeeded))

    #Number of processes returned
    nReturned = cbNeeded.value/sizeof(c_ulong())

    pid = [i for i in lpidProcess][:nReturned]
    counters = _PROCESS_MEMORY_COUNTERS()
    for id in pid:
        #Get handle to the process based on PID
        hProcess = kernel.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, id)
        if hProcess:
            psapi.EnumProcessModules(hProcess, byref(hModule), sizeof(hModule), byref(count))
            psapi.GetModuleBaseNameA(hProcess, hModule.value, modname, sizeof(modname))
            b = "".join( [ i for i in modname if i != '\x00'] )
            print b
            b0 = (b.lower()).split('.')
            if b0[0] == "qq":
                print "qq"
                #AppInfo.app_pid['GPRS数据传输'] = id
            kernel.CloseHandle(hProcess)
    return pid

#结束进程函数（参数说明：进程ID） added by LIHF 090830
def CloseProcess( pid ):
    handle   = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid )
    exitcode = win32process.GetExitCodeProcess( handle )
    win32api.TerminateProcess(handle, exitcode)
    win32api.CloseHandle(handle)

#-------------------------------------运行程序------------------------------------

if __name__ == '__main__':
    GetProcessInfo()






