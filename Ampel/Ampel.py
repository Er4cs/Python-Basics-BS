"""
Ampel
"""
from tkinter import *
from threading import Timer

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
            
class Ampel(Frame):
    phase=0
    x=150
    y=160
    
    def __init__(self, container):
        super().__init__(container,  borderwidth = 3, relief="raised", width=self.x, height=self.y)
        self.canvas=Canvas(self,width=self.x,height=self.y)
        self.canvas.pack()
        self.canvas.create_oval(5,5+0*52,50,50+0*52,fill="red")
        self.canvas.create_oval(5,5+1*52,50,50+1*52,fill="black")
        self.canvas.create_oval(5,5+2*52,50,50+2*52,fill="black")
         
    def nextPhase(self):
        self.phase+=1
        if self.phase==1:    
            self.canvas.create_oval(5,5+0*52,50,50+0*52,fill="red")
            self.canvas.create_oval(5,5+1*52,50,50+1*52,fill="black")
            self.canvas.create_oval(5,5+2*52,50,50+2*52,fill="black")
        elif self.phase==2:
            self.canvas.create_oval(5,5+0*52,50,50+0*52,fill="red")
            self.canvas.create_oval(5,5+1*52,50,50+1*52,fill="yellow")
            self.canvas.create_oval(5,5+2*52,50,50+2*52,fill="black")
        elif self.phase==3:
            self.canvas.create_oval(5,5+0*52,50,50+0*52,fill="black")
            self.canvas.create_oval(5,5+1*52,50,50+1*52,fill="black")
            self.canvas.create_oval(5,5+2*52,50,50+2*52,fill="green")
        elif self.phase==4:
            self.canvas.create_oval(5,5+0*52,50,50+0*52,fill="black")
            self.canvas.create_oval(5,5+1*52,50,50+1*52,fill="yellow")
            self.canvas.create_oval(5,5+2*52,50,50+2*52,fill="black")
            self.phase=0

    def start(self):
        self.timer = RepeatTimer(1, self.nextPhase)
        self.timer.start()

    def stop(self):
        self.timer.cancel()

def starte():
   global nr
   if nr==0:
      ampel.start()
   elif nr==1:
     ampel2.start()
   elif nr==2:
      ampel3.start()
   elif nr==3:
      ampel4.start()
   nr+=1
    
    
def stoppe():
    ampel.stop()
    ampel2.stop()
    ampel3.stop()
    ampel4.stop()

window = Tk()
window.geometry("600x380")
window.title("Ampel")
nr=0

ampel = Ampel(window)
ampel2 = Ampel(window)
ampel3 = Ampel(window)
ampel4 = Ampel(window)

start_button = Button(window, text="Start", command=lambda:starte(),width = 15)
stop_button = Button(window, text="Stopp", command=stoppe,width = 15)
exit_button = Button(window, text="Beenden", command=window.destroy, width = 15)

ampel.grid(row = 0, column = 0,  padx=10, pady=10)
ampel2.grid(row = 0, column = 1,  padx=10, pady=10)
ampel3.grid(row = 0, column = 2,  padx=10, pady=10)
ampel4.grid(row = 0, column = 3,  padx=10, pady=10)
start_button.grid(row = 1, column = 0, columnspan=2, padx=10, pady=10,sticky=W)
stop_button.grid(row = 2, column = 0, columnspan=2, padx=10, pady=10,sticky=W) 
exit_button.grid(row = 3, column = 0, columnspan=2, padx=10, pady=10,sticky=W) 

mainloop()