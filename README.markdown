wxMeta
======

wxMeta is a really simple wrapper for wxPython that makes doing simple things.. simpler. The hope is that it will help get small GUI projects off the ground quicker by eliminating some boilerplate code and providing a more pythonic and natural interface to your GUI elements.

Installation
------------

Not really much to speak of, just copy the wxMeta.py file into the same folder as your project.

Usage
-----

wxMeta is desigend to work with XRC files to define the look of the GUI. There are a few XRC editors around, I tend to use xrced which comes with wxPython. Its a bit quirky but quite quick and easy to use when you get the hang of it.

Next have a look at example.py which is quite self explanatory. The basic idea is that you should subclass wxMeta.SimpleApp which provides you with a 'controls' object allowing you get the wxPython objects corresponding to your GUI controls more easily and also to bind event handlers to events.

You can (and should) overload the Init function to provide your own initialisation code for your application e.g. specifying event handlers.

The controls object provides two basic mechanisms, the first is that the wxPython objects corresponding to your controls are mapped to members of the controls object, e.g.

    self.controls.foo

gives you the object of the control named 'foo' in your XRC file.

The second is that you can bind event handlers to events by assigning functions to members of the form OnEvent_foo e.g.

    self.controls.OnEvent_foo = self.MyEventHandler

This binds the function MyEventHandler to the Event event of the foo control.

Currently not every possible wx event is specified in wxMeta, to add ones that I havn't included have a look at adding to the event_handlers dict in wxMeta.py and it should be clear what to do. If you do add some more things to this list then let me know and I'll add them to the repo version too.



