#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:      ZWW
#
# Created:     17/12/2013
# Copyright:   (c) ZWW 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import wx
class AboutFrame(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, 'About Dual Miner', size=(500,400))
        panel = wx.Panel(self, -1)
        OSver=wx._misc.GetOsVersion()
        Text1 = wx.StaticText(panel, -1, str(OSver))

class ToolbarFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"Simple",size=(300,200))
        statusBar=self.CreateStatusBar()
        menuBar= wx.MenuBar()
        menu1=wx.Menu()
        menuBar.Append(menu1,"&File")
        menu2=wx.Menu()
        menu2.Append(wx.NewId(),"&Copy","status information")
        menu2.Append(wx.NewId(),"C&ut","")
        menu2.Append(wx.NewId(),"Paste","")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(),"&Options","Display Options")
        menuBar.Append(menu2,"&Edit")
        menu3=wx.Menu()
        menuItem=menu3.Append(wx.NewId(),"&About","About this software")
        self.Bind(wx.EVT_MENU, self.OnAbout, menuItem)
        menuBar.Append(menu3,"&Help")
        self.SetMenuBar(menuBar)

        splitter = wx.SplitterWindow(self, -1, style=wx.SP_LIVE_UPDATE)
        sty = wx.BORDER_SUNKEN
        p1 = wx.Window(splitter, style=sty)
        p1.SetBackgroundColour("pink")
        wx.StaticText(p1, -1, "Panel One", (5,5))

        p2 = wx.Window(splitter, style=sty)
        p2.SetBackgroundColour("sky blue")
        wx.StaticText(p2, -1, "Panel Two", (5,5))

        splitter.SetMinimumPaneSize(20)
        splitter.SplitVertically(p1, p2, -100)

        toolbar = self.CreateToolBar(wx.TB_TEXT|wx.TB_HORZ_LAYOUT|wx.TB_NO_TOOLTIPS)

    def OnAbout(self, evt):
        sf = AboutFrame(self)
        sf.ShowModal()

class MySplitter(wx.SplitterWindow):
    def __init__(self, parent, ID, log):
        wx.SplitterWindow.__init__(self,parent,ID,style = wx.SP_LIVE_UPDATE)

app = wx.PySimpleApp()
frame=ToolbarFrame(parent=None,id=-1)
frame.Show(True)
app.MainLoop()