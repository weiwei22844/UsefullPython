#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:      ZWW
#
# Created:     08/02/2014
# Copyright:   (c) ZWW 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import wx
import threading
import os
import subprocess

class mainFrame(wx.Frame):
    def __init__(self,id):
        wx.Frame.__init__(self,None,title="TestMe")
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.startExe=wx.Button(self,-1,"start")
        self.Bind(wx.EVT_BUTTON, self.OnStart, self.startExe)
        self.handle=None

    def OnStart(self,evt):
        self.handle = subprocess.Popen("ping www.baidu.com -t", shell=False, creationflags=subprocess.CREATE_NEW_CONSOLE)
        print self.handle.pid

    def OnCloseWindow(self,evt):
        self.Destroy()

if __name__ == '__main__':
    app = wx.App(False)

    mainFrm = mainFrame(1)
    mainFrm.Show()
    print "mainFame will show"
    app.MainLoop()
