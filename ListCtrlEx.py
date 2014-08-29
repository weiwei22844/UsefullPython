#! /usr/bin/env python
#coding=utf-8

import wx
import sys

packages = [('jessica alba', 'pomona', '1981'), ('sigourney weaver', 'new york', '1949'),
    ('angelina jolie', 'los angeles', '1975'), ('natalie portman', 'jerusalem', '1981'),
    ('rachel weiss', 'london', '1971'), ('scarlett johansson', 'new york', '1984' )]

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title, size):
        wx.Frame.__init__(self, parent, id, title, size, style = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
        print wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel = wx.Panel(self, -1)

        self.list = wx.ListCtrl(panel, -1, style=wx.LC_REPORT)
        self.list.InsertColumn(0, 'name', width=140)
        self.list.InsertColumn(1, 'place', width=130)
        self.list.InsertColumn(2, 'year', wx.LIST_FORMAT_RIGHT, 90)

        for i in packages:
            index = self.list.InsertStringItem(sys.maxint, i[0])
            self.list.SetStringItem(index, 1, i[1])
            self.list.SetStringItem(index, 2, i[2])

        self.list.Select(1)
        self.list.SetItemBackgroundColour(1, wx.Colour(255,255,0))

        self.testBtn=wx.Button(panel,-1,"cgminer path")
        self.Bind(wx.EVT_BUTTON, self.OnButtonTest, self.testBtn)
        hbox.Add(self.list, 1, wx.EXPAND)
        hbox.Add(self.testBtn, 0, wx.RIGHT)
        panel.SetSizer(hbox)

        self.Centre()

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnDevSelected, self.list)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.OnDevDeselected, self.list)

    def OnDevSelected(self, evt):
        print "select"

    def OnDevDeselected(self, evt):
        print "deselect"

    def OnButtonTest(self, evt):
        #self.list.Select(-1)
        #nSelect = self.list.GetSelectedItemCount()
        nSelect = self.list.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
        print nSelect
        #self.list.SetItemState(nSelect, 0, -1)
        self.list.Select(nSelect, on=0)
        #self.Hide()
        style = self.GetWindowStyle()
        print style
        #self.SetWindowStyle(style & (~wx.CLOSE_BOX))
        #print self.GetWindowStyle()
        #self.SetWindowStyle(wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN)
        self.ToggleWindowStyle(wx.CLOSE_BOX)
        pass

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, id=-1, title="DownThemAll", size=(800,600))
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()

