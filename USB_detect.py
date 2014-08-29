#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:      ZWW
#
# Created:     28/12/2013
# Copyright:   (c) ZWW 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# -*- coding: utf-8 -*-
import wx
from ctypes import *
from ctypes.wintypes import *
import win32gui

NULL = 0
INVALID_HANDLE_VALUE = -1
DBT_DEVTYP_DEVICEINTERFACE = 5
DEVICE_NOTIFY_WINDOW_HANDLE = 0x00000000
DBT_DEVICEREMOVECOMPLETE = 0x8004
DBT_DEVICEARRIVAL = 0x8000
WM_DEVICECHANGE = 0x0219

RegisterDeviceNotification = windll.user32.RegisterDeviceNotificationW
UnregisterDeviceNotification = windll.user32.UnregisterDeviceNotification

class GUID(Structure):
    _pack_ = 1
    _fields_ = [("Data1", c_ulong),
                ("Data2", c_ushort),
                ("Data3", c_ushort),
                ("Data4", c_ubyte * 8)]

class DEV_BROADCAST_DEVICEINTERFACE(Structure):
    _pack_ = 1
    _fields_ = [("dbcc_size",       DWORD),
                ("dbcc_devicetype", DWORD),
                ("dbcc_reserved",   DWORD),
                ("dbcc_classguid",  GUID),
                ("dbcc_name",       c_wchar*260)]

class DEV_BROADCAST_HDR(Structure):
    _fields_ = [("dbch_size",       DWORD),
                ("dbch_devicetype", DWORD),
                ("dbch_reserved",   DWORD)]

GUID_DEVCLASS_PORTS = GUID(0x4D36E978, 0xE325, 0x11CE, (c_ubyte*8)(0xBF, 0xC1, 0x08, 0x00, 0x2B, 0xE1, 0x03, 0x18))
GUID_DEVINTERFACE_USB_DEVICE = GUID(0xA5DCBF10L, 0x6530,0x11D2, (c_ubyte*8)(0x90, 0x1F, 0x00,0xC0, 0x4F, 0xB9, 0x51, 0xED))


class Example(wx.Frame):
    def __init__(self,parent,title):
        super(Example,self).__init__(parent,title=title,size=(300,250))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(3,2,9,25)

        title = wx.StaticText(panel,label='Title:')
        author = wx.StaticText(panel,label='Author:')
        review = wx.StaticText(panel,label='Review')

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        fgs.AddMany([(title),(tc1,1,wx.EXPAND),(author),
                     (tc2,1,wx.EXPAND),(review,1,wx.EXPAND),(tc3,1,wx.EXPAND)])

        fgs.AddGrowableRow(2,1)
        fgs.AddGrowableCol(1,1)

        hbox.Add(fgs,proportion=1,flag=wx.ALL|wx.EXPAND,border=15)
        panel.SetSizer(hbox)

    def setupNotification(self):
        dbh = DEV_BROADCAST_DEVICEINTERFACE()
        dbh.dbcc_size = sizeof(DEV_BROADCAST_DEVICEINTERFACE)
        dbh.dbcc_devicetype = DBT_DEVTYP_DEVICEINTERFACE
        dbh.dbcc_classguid = GUID_DEVINTERFACE_USB_DEVICE #GUID_DEVCLASS_PORTS
        #self.hNofity = RegisterDeviceNotification(int(self.winId()), byref(dbh), DEVICE_NOTIFY_WINDOW_HANDLE)
        self.hNofity = RegisterDeviceNotification(win32gui.GetForegroundWindow(), byref(dbh), DEVICE_NOTIFY_WINDOW_HANDLE)
        if self.hNofity == NULL:
            print 'RegisterDeviceNotification failed!'
            self.statusBar().showMessage('RegisterDeviceNotification failed!')

    def winEvent(self, message):
        if message.message == WM_DEVICECHANGE:
            self.onDeviceChanged(message.wParam, message.lParam)
            return True, id(message)
        return False, id(message)

    def OnDeviceChange(self, message):
        print "shit"
        pass

if __name__ == '__main__':
    app = wx.App()
    example = Example(None,title="FlexGridSizer.py")
    example.setupNotification()
    app.MainLoop()