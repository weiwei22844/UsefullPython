#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      ZWW
#
# Created:     11/02/2014
# Copyright:   (c) ZWW 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import wx

#now not use
class AbstractList(wx.ListCtrl):#,
    #listmix.ListCtrlAutoWidthMixin,
    #listmix.ColumnSorterMixin):
    def __init__(self, parent,columes,editlabel=False):
        """list 控件封装 提供表头排序功能，建议使用"""
        wx.ListCtrl.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT |\
                                                                                   wx.SUNKEN_BORDER)
        #listmix.ListCtrlAutoWidthMixin.__init__(self)
        #listmix.ColumnSorterMixin.__init__(self, len(columes))
        self.SetColumns(columes)
        self.ImageList = wx.ImageList(32,32,True)
        self.AssignImageList(self.ImageList, wx.IMAGE_LIST_SMALL)
        if editlabel:
            self.Bind(wx.EVT_LIST_BEGIN_LABEL_EDIT,self.EvtBeginEditLabel)
            self.Bind(wx.EVT_LIST_END_LABEL_EDIT,self.EvtEndEditLabel)

    def EvtContextMenu(self,evt):
        pMenu=self.InitPopuMenu()
        assert pMenu
        self.PopupMenu(pMenu)
        pMenu.Destroy()

    def InitPopuMenu(self):
        """init poup menu"""

    def EvtEndEditLabel(self,evt):
        """end edit label"""

    def EvtBeginEditLabel(self,evt):
        """begein edit label"""
        evt.Allow()

    def SetColumns(self, columes):
        """添加表头信息"""
        i = 0
        for name, width in columes:
            self.InsertColumn(i, name)
            if width:
                self.SetColumnWidth(i, width)
            else:
                self.setResizeColumn(i)
            i += 1

    def GetListCtrl(self):
        """这个方法只是为了表头排序"""
        return self

    def NotImplemented(self, str):
        print str

    def RawIconAndRow(self, item):
        """格式化对象，添加到每一列中去"""
        NotImplemented('RawIconAndRow')

    def AddRow(self, item, idx=sys.maxint):
        icon, row = self.RawIconAndRow(item)
        idx = self.InsertImageStringItem(idx, row[0], icon)
        cols_num=len(row)
        for i in xrange(cols_num):
            self.SetStringItem(idx, i, row[i])
        self.pyData[idx] = item
        self.itemDataMap[idx] = row
        return idx

########################################################################

class AbstractControlList(AbstractList):
    def __init__(self, parent,columes,editlabel=False):
        AbstractList.__init__(self, parent,columes,editlabel)
        #self.Bind(wx.EVT_PAINT,self.PaintControl)
        self.Bind(wx.EVT_LIST_COL_DRAGGING, self.PaintControl)
        self.Bind(wx.EVT_LIST_COL_END_DRAG, self.PaintControl)
        self.Bind(wx.EVT_SCROLLWIN_THUMBRELEASE, self.PaintControl)
        for i in range(10):
            index = self.InsertStringItem(sys.maxint, "test")
            for j in range(2):
                self.SetStringItem(i, j, "shit %d"%i)
                j+=1
            i+=1

    def GetControlColNum(self):
        NotImplemented('GetControlColNum')

    def GetControlItem(self,item,col):
        NotImplemented('GetCellControl')

    def RefreshColumText(self,rowidx):
        """refreshText of the list"""

    def PaintControl(self,evt):
        if evt.GetOrientation() == wx.VERTICAL:
            print "vertical %d"%self.GetScrollPos(wx.VERTICAL)
            self.topIndex = self.GetTopItem() - 1
        elif evt.GetOrientation() == wx.HORIZONTAL:
            print "horizontal %d"%self.GetScrollPos(wx.HORIZONTAL)
            self.EnsureVisible(self.topIndex)
        #self.SetScrollPos(wx.VERTICAL, 0)
        #print "vertical %d"%self.GetScrollPos(wx.VERTICAL)
        #self.Refresh()
        #self.EnsureVisible(2)

    def DeleteItem(self, idx):
        control_cols=self.GetControlColNum()
        pyData=self.GetPyData(idx)
        assert pyData
        for col in control_cols:
            control=self.GetControlItem(pyData,col)
            control.Hide()
            control=None
        self.RemovePyData(idx)
        AbstractList.DeleteItem(self,idx)

    def DeleteAllItems(self):
        control_cols=self.GetControlColNum()
        for pyData in self.pyData.values():
            for col in control_cols:
                control=self.GetControlItem(pyData,col)
            control.Destory()
        self.pyData.clear()
        AbstractList.DeleteAllItems(self)

    def RawIconAndRow(self, item):
        """格式化对象，添加到每一列中去"""
        NotImplemented('RawIconAndRow')

    def AddRow(self, item, idx=sys.maxint):
        icon, row = self.RawIconAndRow(item)
        idx = self.InsertImageStringItem(idx, row[0], icon)
        row_cout=len(row)
        control_cols=self.GetControlColNum()
        for i in xrange(row_cout):
            if i in control_cols:
                row[i]=''
            else:
                self.SetStringItem(idx, i, row[i])
        self.pyData[idx] = item
        self.itemDataMap[idx] = row
        return idx

    def _GetColumnWidthExtent(self, col):
        col_locs,loc = [0],0
        num_cols = min(col+1, self.GetColumnCount())
        for n in xrange(num_cols):
            loc += self.GetColumnWidth(n)
            col_locs.append(loc)
        x0 = col_locs[col]
        x1 = col_locs[col+1] - 1
        return x0, x1

    def GetColumnRect(self, col):
        x0, x1 = self._GetColumnWidthExtent(col)
        r = self.GetItemRect(0)
        y0 = r.y
        y1 = self.GetClientSize()[1]
        x_scroll = self.GetScrollPos(wx.HORIZONTAL)
        return wx.RectPP(wx.Point(x0 - x_scroll, y0),wx.Point(x1 - x_scroll, y1))


    def GetCellRect(self, row, col):
        x0, x1 = self._GetColumnWidthExtent(col)
        r = self.GetItemRect(row)
        y0 = r.y
        y1 = r.GetBottom()
        x_scroll = self.GetScrollPos(wx.HORIZONTAL)
        return wx.RectPP(wx.Point(x0 - x_scroll, y0),wx.Point(x1 - x_scroll, y1))

class mainFrame(wx.Frame):
    def __init__(self,id):
        wx.Frame.__init__(self,None,title="DualMiner GUI")
        #self.listchild=AbstractList(self, [("wei", 100), ("zhao", 100)])
        self.list = AbstractControlList(self, [("wei", 100), ("zhao", 100)])

if __name__ == '__main__':
    app = wx.App(False)
    mainFrm = mainFrame(0)
    mainFrm.Show()
    print "mainFame will show"
    app.MainLoop()

