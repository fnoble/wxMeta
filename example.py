#!/usr/bin/env python
# encoding: utf-8

"""
example.py

A basic example of how to use wxMeta

Copyright (c) 2009 Fergus Noble. All rights reserved.

"""

import wxMeta
import wx

class ExampleApplication(wxMeta.SimpleApp):
    """ My simple wxMeta example application """
    
    def Init(self):   
        """ Initialisation code for my application """
        
        """ wxMeta provides a built-in object called 'controls' which gives you access 
            to the wxPython objects corresponding to controls you specified in the XRC
            file.
            
            self.contols.foo is the object corresponding to the control named 'foo' in the
            XRC file.
            
            You can also bind handlers to events by assigning a function to members of
            controls with names like OnEvent_foo which corresponds to the Event event of
            the foo control.
        """
        
        # This binds the function CloseMain to the close event of main_window
        self.controls.OnClose_main_window = self.CloseMain
        # Likewise this binds ButtonClicked to the click even of example_button
        self.controls.OnClick_example_button = self.ButtonClicked
        
        return True

    def ButtonClicked(self, evt):
        # gets the text entered in the 'example_input' control
        text_input = self.controls.example_input.GetValue()
        # sets the contents of the 'example_input' control to uppercase
        self.controls.example_input.SetValue(text_input.upper())

    def CloseMain(self, evt):
        dlg = wx.MessageDialog(
                self.controls.main_window, 
                "Do you really want to close this awesome application?",
                "Confirm Exit", 
                wx.OK|wx.CANCEL|wx.ICON_QUESTION
              )
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.controls.main_window.Destroy()

if __name__ == '__main__':
    """ Here you should specify the XRC file for your application and the name of
        the main window """
        
    app = ExampleApplication('example.xrc', 'main_window')
    app.MainLoop()

