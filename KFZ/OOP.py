"""
Class KFZ LKW
"""
from Klassen import KFZ
from Klassen import LKW
from Klassen import Flugzeug 
from tkinter import *

#-------------------------------------------------------------------- 
def onButtonBremsenKfz():
    porsche.bremsen()
    labelKfzGeschwindigkeit.config(text=str(porsche.getGeschwindigkeit())+" km/h")

def onButtonBeschleunigenKfz():
    porsche.beschleunigen()
    labelKfzGeschwindigkeit.config(text=str(porsche.getGeschwindigkeit())+" km/h")
#-------------------------------------------------------------------- 
def onButtonBremsenLkw():
    man.bremsen()
    labelLkwGeschwindigkeit.config(text=str(man.getGeschwindigkeit())+" km/h")

def onButtonBeschleunigenLkw():
    man.beschleunigen()
    labelLkwGeschwindigkeit.config(text=str(man.getGeschwindigkeit())+" km/h")

def onButtonBeladenLkw():
    man.beladen()
    labelLkwLadung.config(text=str(man.getLadung())+" t")
    
def onButtonEntladenLkw():
    man.entladen()
    labelLkwLadung.config(text=str(man.getLadung())+" t")
#-------------------------------------------------------------------- 
   
window = Tk()
window.geometry("750x350")
window.option_add( "*font", "Arial 12 bold bold" )
window.title("OOP")

labelKfz = Label(window, text="KFZ")
labelKfzGeschwindigkeit = Label(window, text="0")
labelLkw = Label(window, text="LKW")
labelLkwGeschwindigkeit = Label(window, text="0")
labelLkwLadung = Label(window, text="0")

buttonBremsenKfz = Button(window, text="Bremsen", command=onButtonBremsenKfz,width = 15)
buttonBeschleunigenKfz = Button(window, text="Beschleunigen", command=onButtonBeschleunigenKfz,width = 15)
buttonBremsenLkw = Button(window, text="Bremsen", command=onButtonBremsenLkw,width = 15)
buttonBeschleunigenLkw = Button(window, text="Beschleunigen", command=onButtonBeschleunigenLkw,width = 15)
buttonBeladenLkw = Button(window, text="Beladen", command=onButtonBeladenLkw,width = 15)
buttonEntladenLkw = Button(window, text="Entladen", command=onButtonEntladenLkw,width = 15)
exit_button = Button(window, text="Beenden", command=window.destroy,width = 15)

labelKfz.grid(row = 0, column = 0, padx=10, pady=20)   
labelKfzGeschwindigkeit.grid(row = 1, column = 0) 
buttonBremsenKfz.grid(row = 2, column = 0) 
buttonBeschleunigenKfz.grid(row = 2, column = 1) 

labelLkw.grid(row = 3, column = 0, padx=10, pady=20)  
labelLkwGeschwindigkeit.grid(row = 4, column = 0)
labelLkwLadung.grid(row = 4, column = 1)
buttonBremsenLkw.grid(row = 5, column = 0,padx=10, pady=10) 
buttonBeschleunigenLkw.grid(row = 5, column = 1,padx=10, pady=10) 
buttonEntladenLkw.grid(row = 5, column = 2,padx=10, pady=10) 
buttonBeladenLkw.grid(row = 5, column = 3,padx=10, pady=10) 

exit_button.grid(row = 6, column = 0, columnspan=2, padx=10, pady=20,sticky=W) 

porsche = KFZ()
man=LKW()

labelKfzGeschwindigkeit.config(text=str(porsche.getGeschwindigkeit())+" km/h")
labelLkwGeschwindigkeit.config(text=str(man.getGeschwindigkeit())+" km/h")
labelLkwLadung.config(text=str(man.getLadung())+" t")



mainloop()
