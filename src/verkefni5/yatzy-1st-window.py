#!/usr/bin/env python3
#import tkinter as tk
#from tkinter import messagebox
##import yatzy

##from tkinter import *
##fields = 'First player', 'Second player', 'Theerd player', 'Fourth player'

##def fetch(entries):
##    for entry in entries:
##        field = entry[0]
##        text  = entry[1].get()
##        print('%s: "%s"' % (field, text))
##    print(yatzy.rolleDice(6), entries)

##def makeform(root, fields):
##   entries = []
##   for field in fields:
##      row = Frame(root)
##      lab = Label(row, width=15, text=field, anchor='w')
##      ent = Entry(row)
##      row.pack(side=TOP, fill=X, padx=5, pady=5)
##      lab.pack(side=LEFT)
##      ent.pack(side=RIGHT, expand=YES, fill=X)
##      entries.append((field, ent))
##   return entries

##if __name__ == '__main__':
##   root = Tk()
##   ents = makeform(root, fields)
   
   #lbl = root.Label(self, text='Yatzy')
   #lbl = Label(root, _optionsPanel, text = "New Pot Starting Value").pack()

##   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
##   b1 = Button(root, text='Start a game',
##          command=(lambda e=ents: fetch(e)))
##   b1.pack(side=LEFT, padx=5, pady=5)
##   b2 = Button(root, text='Quit', command=root.quit)
##   b2.pack(side=LEFT, padx=5, pady=5)
##   root.mainloop()


import gi, sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="- Yatzy Starter -")
        self.set_border_width(5)
        #self.connect("destroy", Gtk.main_quit)
        self.set_size_request(200, 100)

        self.box = Gtk.Box(spacing=10)
        self.add(self.box)


        #self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        #self.add(self.box)

        self.entry1 = Gtk.Entry()
        self.entry1.set_text("Player 1")
        self.entry1.set_position(0.0)
        self.box.pack_start(self.entry1, True, True, 0)


#        self.box = Gtk.Box(spacing=100)
#        self.add(self.box)

        self.entry2 = Gtk.Entry()
        self.entry2.set_text("Player 2")
        self.box.pack_start(self.entry2, True, True, 0)

        self.entry3 = Gtk.Entry()
        self.entry3.set_text("1")
        self.box.pack_start(self.entry3, True, True, 0)

        self.entry4 = Gtk.Entry()
        self.entry4.set_text("2")
        self.box.pack_start(self.entry4, True, True, 0)
        

        #self.hbox = Gtk.Box(spacing=6)
        #self.vbox.pack_start(self.hbox, True, True, 0)


        self.button1 = Gtk.Button(label="Start Game")
#        self.button1 = Gtk.Box()
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Quit")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

    def do_pulse(self, user_data):
        self.entry.progress_pulse()
        return True
        
    def on_button1_clicked(self, widget):
        print("Yay")
        print(self.entry1.get_text(), ',', self.entry2.get_text(), ',',
              self.entry3.get_text(), ',', self.entry4.get_text())

    def on_button2_clicked(self, widget):
        print("Goodby")
        sys.exit()

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

