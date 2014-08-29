#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:      ZWW
#
# Created:     13/01/2014
# Copyright:   (c) ZWW 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import wx
import wx.animate
from time import time, sleep

class gifFrame(wx.Frame):
    ### Basic Frame,
    def __init__(self, parent, id):
        wx.Frame.__init__(self,parent,id,"FRAME 1 aka Panel, Window",
                          size=(800,600))
        ### EXTRAS ###
        panel=wx.Panel(self)
        b1=wx.Button(panel, label = " STOP ", pos = (380, 500))
        self.Bind(wx.EVT_BUTTON, self.closebutton, b1)
        ## GIF
        ag_fname = wx.FileDialog(self, defaultFile="", style=wx.OPEN)
        if ag_fname.ShowModal() == wx.ID_OK:
            gif = ag_fname.GetPath()

        gif1 = wx.animate.GIFAnimationCtrl(panel, id, gif, pos=(75,10),
                                            size=(200,200))
        gif1.Play()

    ### Funktion Button STOP
    def closebutton(self,event):
        self.Close(True)


# show FRAME
if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=gifFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()