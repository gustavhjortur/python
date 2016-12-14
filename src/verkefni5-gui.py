import tkinter as tk
from tkinter import messagebox

def event_generator(widget):
    def event():
        print(widget.row, widget.col)
    return event

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def color_changer(self, event):
        #print(event.widget.row, event.widget.col)
        event.widget['bg'] = 'red'

    def clear_color(self, event):
        event.widget['bg'] = 'white'

    def toggle_color(self, event):
        print('yay')
        if event.widget.on:
            event.widget.create_rectangle(5,5,45,45, fill='#CCCCCC')
        else:
            event.widget.create_rectangle(5,5,45,45, fill='blue')
        event.widget.on = not event.widget.on
        self.lbl['text'] = '(%d, %d)' % ( event.widget.row, event.widget.col )
        messagebox.showinfo('WOW', '{%d, %d}' % ( event.widget.row, event.widget.col) )

    def create_widgets(self):
        self.button = Button(frame, text="QUIT", fg="red", command=quit)
        self.lbl = tk.Label(self, text='Yatzy')
        self.lbl.grid(row=5000, column=0, columnspan=50)
        
        for r in range(19):
            for c in range(3):
                self.btn = tk.Button(self,
                                     text="yay",
                                     bg="white",
                                     command=self.say_hi)
                #can = tk.Canvas(self, width=150, height=50, bg='white')
                #can.grid(row=r, column=c)
                #can.create_rectangle(5,5,45,45, fill='#CCCCCC')
                self.btn['command'] = event_generator(self.btn)
                self.btn.grid(row=r, column=c)
                self.btn.row = r
                self.btn.col = c
                #can.row = r
                #can.col = c
                #can.on = False
                self.btn.grid(row=r, column=c)
                self.btn.bind('<Enter>', self.color_changer)
                self.btn.bind('<Leave>', self.clear_color)
                #can.bind('<Enter>', self.color_changer)
                #can.bind('<Leave>', self.clear_color)
                #can.bind('<Button-1>', self.toggle_color)

####        self.hi_there = tk.Button(self)
####        self.hi_there["text"] = "Hello World\n(click me)"
####        self.hi_there["command"] = self.say_hi
####        self.hi_there.pack(side="top")
####        self.quit = tk.Button(self, text="QUIT", fg="red",
####                              command=root.destroy)
####        self.quit.pack(side="bottom")

    def say_hi(self, widget):
        print(widget.row, widget.col)

root = tk.Tk()
app = Application(master=root)
app.mainloop()