from __main__ import *
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

fo1=open("receipt.txt","r")
list1=fo1.readlines()

del list1[1]
del list1[2]
del list1[3]
del list1[4]
del list1[5]
list1[0]=list1[0][:-1]
list1[1]=list1[1][:-1]
list1[2]=list1[2][:-1]
list1[3]=list1[3][:-1]
list1[4]=list1[4][:-1]

p='''
------------- Mini Project --------------
--------------- MIT SoE  ---------------
NAME-%s
ADDRESS-%s
MOBILE NO.-%s
YOUR TOTAL BILL IS Rs.-%s
YOUR ROOM NUMBER IS %s    
     
     
     
'''%(list1[0],list1[1],list1[2],list1[4],list1[3])

        





class receipt:
    def __init__(self):
        root=Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#FFEBCD'  # X11 color: 'blanchedalmond'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#FFEBCD' # X11 color: 'blanchedalmond'
        _ana1color = '#FFEBCD' # X11 color: 'blanchedalmond'
        _ana2color = '#FFEBCD' # X11 color: 'blanchedalmond'

        root.geometry("800x800")
        root.title("receipt")
        root.configure(background="#FFEBCD")



        self.Label1 = Label(root)
        self.Label1.configure(background="#FFEBCD")
        self.Label1.place(relx=0, rely=0, height=800, width=800)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text=p)
        self.Label1.configure(anchor=N)

        self.Label1.configure(wraplength=1000)
        self.Label1.configure(justify =LEFT)

        self.Label1.configure(width=582)
        root.mainloop()


if __name__ == '__main__':
    receipt1=receipt()


