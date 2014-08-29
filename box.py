#coding=utf-8
'''
Created on 2013-2-17

@author: Administrator
'''
#!/usr/bin/env python

import wx
#import init

class InsertFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'shit',size=(330, 350))
        self.SetBackgroundColour('White')

        self.Center()
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        bSizer = wx.BoxSizer(wx.VERTICAL)
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"123:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer6.Add( self.m_staticText2, 0, wx.ALL, 5 )
        self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"选择文件", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        self.m_dirPicker1.SetPath("D:\VirtualMachine\share\work\minerUI")
        pButt = self.m_dirPicker1.GetPickerCtrl()
        if pButt is not None:
            pButt.SetLabel('12345')

        bSizer6.Add( self.m_dirPicker1, 0, wx.ALL, 5 )
        bSizer.Add( bSizer6, 0, wx.EXPAND, 5 )
        self.SetSizer(bSizer)
        self.Layout()
        self.Centre( wx.BOTH )


        panel1 = wx.Panel(self)
        self.basicLabel = wx.StaticText(panel1, -1, " 11111:")
        self.basicText = wx.TextCtrl(panel1, -1, "", size=(175, -1))
        self.basicText.SetInsertionPoint(0)


        self.pwdLabel = wx.StaticText(panel1, -1, " 111222:")
        self.pwdText = wx.TextCtrl(panel1, -1, "", size=(175, -1), style=wx.TE_PASSWORD)
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([self.basicLabel, self.basicText, self.pwdLabel, self.pwdText])
        panel1.SetSizer(sizer)
        bSizer.Add(panel1, 0, wx.EXPAND, 5 )
        self.m_dirPicker1.Bind( wx.EVT_DIRPICKER_CHANGED, self.src_dir )



        panel = wx.Panel(self) #创建画板
        button1 = wx.Button(panel, label='登录', pos=(20, 200),
                size=(50, 25)) #将按钮添加到画板
        button2 = wx.Button(panel, label='关闭', pos=(240, 200),
                size=(50, 25)) #将按钮添加到画板
        #绑定按钮的单击事件
        #self.Bind(wx.EVT_BUTTON, self.OnInitDisk, button1)
        #绑定窗口的关闭事件
        self.Bind(wx.EVT_CLOSE, self.OnCloseMe, button2)
        bSizer.Add(panel, 0, wx.EXPAND, 5 )

    def OnCloseMe(self):
        self.Close(True)
        self.Destroy()
    def OnInitDisk(self, event):

        username = self.basicText.GetValue()
        userpass = self.pwdText.GetValue()
        flag = init.verifyUser(username, userpass)
        print flag
        if flag:
            init.SVNPATH = self.m_dirPicker1.GetPath()
            if ':/' in init.SVNPATH:
                print init.SVNPATH
                init.init(init.SVNPATH)

    def src_dir( self, event ):
        event.Skip()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = InsertFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

