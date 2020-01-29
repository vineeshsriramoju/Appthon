import os
from tkinter import*
import tkinter as tk
class Application(Frame):


    def __init__(self, master):

        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()
    def create_widget(self):
        self.cal=tk.PhotoImage(file="cal.gif")


        self.button1 = tk.Button(self, text="Calculator",image=self.cal, command= lambda : os.system('py cal.py'))
        self.button1.grid(row=0, column=0)
        self.button1.image=self.cal





        self.music=tk.PhotoImage(file="music.gif")
        self.button4 = tk.Button(self, text="Music",image=self.music, command=lambda: os.system('py music42.py'))
        self.button4.grid(row=0, column=1)
        self.button4.image=self.music



        self.curr=tk.PhotoImage(file="curr.gif")
        self.button6 = tk.Button(self, text="currency",image=self.curr, command=lambda: os.system('py currency.py'))
        self.button6.grid(row=1, column=0)
        self.button6.image=self.curr


        self.guess=tk.PhotoImage(file="guss2.gif")
        self.button7 = tk.Button(self, text="guessing",image=self.guess, command=lambda: os.system('py guess.py'))
        self.button7.grid(row=1, column=1)
        self.button7=self.guess

        self.editor=tk.PhotoImage(file="img.gif")
        self.button8 = tk.Button(self, text="editor",image=self.editor, command=lambda: os.system('py editor.py'))
        self.button8.grid(row=2, column=0)
        self.button8.image=self.editor



        self.main=tk.PhotoImage(file="d3.gif")
        self.button9 = tk.Button(self, text="text",image=self.main, command=lambda: os.system('py main.py'))
        self.button9.grid(row=2, column=1)
        self.button9.image=self.main


window = tk.Tk()
app = Application(window)
window.title("APPThon")
window.mainloop()
