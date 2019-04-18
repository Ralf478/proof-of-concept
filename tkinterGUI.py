import simulate_terminal as si
import os

from Tkinter import *

        
class tkGUI():

    t="" # class variable for terminal /dev/pts/x

    def __init__(self, master):
        self.master = master
        master.title("GUI")
        listbox = Listbox(master)
        listbox.pack()

        for item in ["ls -t", "ls -a", "uname -r", "ls -v"]:
           listbox.insert(END, item)

        listbox.bind('<Double-Button-1>', self.OnDouble)   # on double click on item in listbox ...

    def OnDouble(self,event):
        widget = event.widget
        selection=widget.curselection()
        cmd = widget.get(selection[0])
        si.simulate_terminal(self.t,cmd)          # ... the value of the listbox item is extracted and passed to the simulate_terminal function, where t is the least recently used terminal 

    def bind_terminal(self):
        str_tty = os.popen('ls -t /dev/pts').read()      # this determines the terminal that was least recently used before this program was started ( 2nd number in output of 'ls -t /dev/pts' )
        ntty=[s for s in str_tty.split() if s.isdigit()]  # in this recently used terminal the commands are executed 
        if len(ntty) > 1:
            self.t='/dev/pts/'+ntty[1]
        else:
            print("no open terminal")



tk = Tk()

gui=tkGUI(tk)
gui.bind_terminal()

mainloop()





