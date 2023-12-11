from tkinter import *

class Element():
    x1=0
    y1=0

    def __init__(self,x1=0,y1=0):
        self.x1=x1
        self.y1=y1
        pass
    
    def zeichne(self,c):
        pass
                
    def writeXML(self,doc):
        pass
                

#---------------------------------------------------------------------------------------------------------
class Linie(Element):
    x2=0
    y2=0
    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        super().__init__()
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        
    def zeichne(self,c):
        c.create_line(self.x1,self.y1,self.x2,self.y2)
      
    def writeXML(self,doc):
        x1Elem = doc.createElement("X1")
        x1Elem.appendChild(doc.createTextNode(str(self.x1)))
      
        y1Elem = doc.createElement("Y1")
        y1Elem.appendChild( doc.createTextNode(str(self.y1)))

        x2Elem = doc.createElement("X2")
        x2Elem.appendChild( doc.createTextNode(str(self.x2)))
        
        y2Elem = doc.createElement("Y2")
        y2Elem.appendChild( doc.createTextNode(str(self.y2)))
        
        kundeElem = doc.createElement("Linie")
        kundeElem.appendChild(x1Elem)
        kundeElem.appendChild(y1Elem)
        kundeElem.appendChild(x2Elem)
        kundeElem.appendChild(y2Elem)
        doc.documentElement.appendChild(kundeElem)
                

#---------------------------------------------------------------------------------------------------------
class Kreis(Element):
    x2=0
    y2=0
    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        super().__init__()
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

    def zeichne(self,c):
        c.create_oval(self.x1,self.y1,self.x2,self.y2)
        
      
    def writeXML(self,doc):
        x1Elem = doc.createElement("X1")
        x1Elem.appendChild(doc.createTextNode(str(self.x1)))
      
        y1Elem = doc.createElement("Y1")
        y1Elem.appendChild( doc.createTextNode(str(self.y1)))

        x2Elem = doc.createElement("X2")
        x2Elem.appendChild( doc.createTextNode(str(self.x2)))
        
        y2Elem = doc.createElement("Y2")
        y2Elem.appendChild( doc.createTextNode(str(self.y2)))
        
        Elem = doc.createElement("Kreis")
        Elem.appendChild(x1Elem)
        Elem.appendChild(y1Elem)
        Elem.appendChild(x2Elem)
        Elem.appendChild(y2Elem)
        doc.documentElement.appendChild(Elem)
