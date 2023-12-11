class KFZ:
    _geschwindigkeit=0
    _maxGeschwindigkeit=0
    
    def __init__(self,geschwindigkeit=0,maxGeschwindigkeit=180):
        self._geschwindigkeit=geschwindigkeit
        self._maxGeschwindigkeit=maxGeschwindigkeit
    
    def beschleunigen(self):
        if self._geschwindigkeit < self._maxGeschwindigkeit:
            self._geschwindigkeit+=10
                
    def bremsen(self):
        if self._geschwindigkeit>=10:
            self._geschwindigkeit-=10
                
    def getGeschwindigkeit(self):
        return self._geschwindigkeit


#---------------------------------------------------------------------------------------------------------
class LKW(KFZ):
    ladung=0
    maxLadung=16
    
    def __init__(self,ladung=0,maxLadung=18):
        super().__init__()
        self._maxGeschwindigkeit=90
        self.ladung=ladung
        self.maxLadung=maxLadung
        
    def beladen(self):
        if self.ladung < self.maxLadung and self._geschwindigkeit==0:
            self.ladung+=1
                
    def entladen(self):
        if self.ladung>0 and self._geschwindigkeit==0:
            self.ladung-=1
                
    def getLadung(self):
        return self.ladung
    

#-------------------------------------------------------------------------------------------------------------

class Flugzeug(KFZ):
    def __init__(self, geschwindigkeit=0, flughoehe=0):
        super().__init__(geschwindigkeit, 950, 0, 11000)  
        self.flughoehe = flughoehe
        self.maxFlughoehe = 12000

    def steigen(self):
        if self.flughoehe < self.maxFlughoehe and self._geschwindigkeit >= 250:
            self.flughoehe += 20

    def sinken(self):
        if self.flughoehe > 0:
            self.flughoehe -= 20

    def beladen(self):
        if self.ladung < self.maxLadung and self.flughoehe == 0:
            self.ladung += 1

    def entladen(self):
        if self.ladung > 0 and self.flughoehe == 0:
            self.ladung -= 1

    def getFlughoehe(self):
        return self.flughoehe

    def getMaxFlughoehe(self):
        return self.maxFlughoehe
