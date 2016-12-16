#!/usr/bin/env python3
#import tkinter as tk
#from tkinter import messagebox
import yatzy

from tkinter import *
fields = 'First player', 'Second player', 'Theerd player', 'Fourth player'

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text))
    print(yatzy.rolleDice(6), entries)

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   
   #lbl = root.Label(self, text='Yatzy')
   #lbl = Label(root, _optionsPanel, text = "New Pot Starting Value").pack()

   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Start a game',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
