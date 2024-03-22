"""
CAD
"""
from __future__ import annotations
from CadKlassen import Element
from CadKlassen import Linie
from CadKlassen import Kreis
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import tkinter.messagebox
import xml.dom
from xml.dom import minidom

          #Halllooossss
def NewFile():
    w.delete("all")
    Objekte.clear()
    
def OpenFile():
    loadXML()

def SaveFile():
    writeXML()

def About():
    tkinter.messagebox.showinfo("CAD", "Ver: 0.0001")

def loadXML():
    w.delete("all")
    Objekte.clear()
    dateiname = filedialog.askopenfilename()
    doc = minidom.parse(dateiname)
    root = doc.documentElement
    nodes = root.getElementsByTagName("Linie")
    for node in nodes:
        x1=node.getElementsByTagName("X1")[0].childNodes[0].nodeValue
        y1=node.getElementsByTagName("Y1")[0].childNodes[0].nodeValue
        x2=node.getElementsByTagName("X2")[0].childNodes[0].nodeValue
        y2=node.getElementsByTagName("Y2")[0].childNodes[0].nodeValue
        Objekte.append(Linie(x1,y1,x2,y2))
        
    nodes = root.getElementsByTagName("Kreis")
    for node in nodes:
        x1=node.getElementsByTagName("X1")[0].childNodes[0].nodeValue
        y1=node.getElementsByTagName("Y1")[0].childNodes[0].nodeValue
        x2=node.getElementsByTagName("X2")[0].childNodes[0].nodeValue
        y2=node.getElementsByTagName("Y2")[0].childNodes[0].nodeValue
        Objekte.append(Kreis(x1,y1,x2,y2))
      
    for x in Objekte:
        x.zeichne(w)

def writeXML():
    files = [('All Files', '*.*'),('xml Files', '*.xml')]
    dateiname = asksaveasfilename(filetypes = files, defaultextension = ".xml")
    if len(dateiname)>0:
        domImpl = xml.dom.getDOMImplementation()
        doc = domImpl.createDocument("test", "Elemente", None)
        for e in Objekte:
            e.writeXML(doc)
        datei = open(dateiname, "w", encoding="utf8")
        doc.writexml(datei, "\n", "  ")
        datei.close()
    
def motion(event):
    x, y = event.x, event.y
    # print('{}, {}'.format(x, y))
    if buttonKlick==1:
        w.delete("all")
        if Objekt=="Linie":
            w.create_line(pX1,pY1,x,y)
        else:
            w.create_oval(pX1,pY1,x,y)
        for x in Objekte:
            x.zeichne(w)

def onLinie():
    global Objekt
    window.title("CAD - Zeichne Linie")
    Objekt="Linie"

def onKreis():
    global Objekt
    window.title("CAD - Zeichne Kreis")
    Objekt="Kreis"

def mouseClick( event ):
    global buttonKlick
    global pX1
    global pY1
    if buttonKlick==0:
        pX1=event.x
        pY1=event.y
        buttonKlick+=1
    else:
        buttonKlick=0
        pX2=event.x
        pY2=event.y
        if Objekt=="Linie":
            Objekte.append(Linie(pX1,pY1,pX2,pY2))
        else:
            Objekte.append(Kreis(pX1,pY1,pX2,pY2))
            
        for x in Objekte:
            x.zeichne(w)   
   
Objekte: list[Element] = []

buttonKlick=0
Objekt="Linie"
pX1=0
pY1=0
window = Tk()
window.geometry("1024x800")
window.title("CAD")
window.bind('<Motion>', motion)
MainMenu = Menu(window)
window.config(menu=MainMenu)

filemenu = Menu(MainMenu, tearoff=False)
MainMenu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_command(label="Save...", command=SaveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.destroy)

elementmenu = Menu(MainMenu, tearoff=False)
MainMenu.add_cascade(label="Element", menu=elementmenu)
elementmenu.add_command(label="Linie", command=onLinie)
elementmenu.add_command(label="Kreis", command=onKreis)

helpmenu = Menu(MainMenu, tearoff=False)
MainMenu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

canvas_width = 1024
canvas_height = 800

w = Canvas(window,width=canvas_width,height=canvas_height)
w.bind('<Button-1>', mouseClick) 
w.pack()

mainloop()