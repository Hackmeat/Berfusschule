class Datum():
    tagImMonat = [ -1, 
                  31, #1
                  28, 
                  31, 
                  30, 
                  31, 
                  30, 
                  30, 
                  31, 
                  30, 
                  31, 
                  30, 
                  31] #12
    def __init__(self, tag: int, monat: int, jahr: int):
        self.tag = tag
        self.monat = monat
        self.jahr = jahr
        
    def getString(self):
        return str(self.tag) + "." + str(self.monat) + "." + str(self.jahr)

class Anschrift():
    def __init__(self):
        self.vorname = "Max"
        self.nachname = "Mustermann"
        self.strasse = "Musterstrasse"
        self.hausnummer = "3"
        self.plz = 12345
        self.stadt = "Musterstadt"
        self.land = "Musterland"
        
    def getPLZAsString(self):
        return str(self.plz.zfill(5))
    
    def gebeAnschriftAus(self):
        return "Vorname: " + self.vorname + "\nNachname: " + self.nachname + "\nAdresse: " + self.strasse + " " + self.hausnummer + "\nOrt: " + self.stadt + ", " + str(self.plz) + "\nLand: " + self.land

class Sendung():
    def __init__(self, sendungsnummer: str):
        self.sendungsnummer = sendungsnummer
        self.__absender = Anschrift()
        
    def getAbsenderString(self):
        return self.__absender.gebeAnschriftAus()
    
    def getAbsenderValues(self):
        return self.__absender
    
    def setAbsender(self, newObject: Anschrift):
        self.__absender = newObject
        
class Paket(Sendung):
    def __init__(self, sendungsnummer: str):
        super().__init__(sendungsnummer)
        self.gewichtInKG = 0.0
        self.groesse = Abmessung(2, 4, 6)
        
class Abmessung():
    def __init__(self, laenge: float, breite: float, hoehe: float):
        self.laenge = laenge
        self.breite = breite
        self.hoehe = hoehe
        
    def getVolume(self):
        return self.laenge * self.breite * self.hoehe
    
class Brief(Sendung):
    def __init__(self, sendungsnummer: str):
        super().__init__(sendungsnummer)
        self.gewichtInGramm = 0
        self.istInPost = False 
        
class ExpressPaket(Paket):
    hoechsterMaximalwert = 7
    def __init__(self, sendungsnummer: str):
        super().__init__(sendungsnummer)
        self.__maximaleLieferFirst = 4
        
    def setMaximaleLieferfristInTagen(self, wert: int):
        if(wert >= 0 and wert <= self.hoechsterMaximalwert):
            self.__maximaleLieferFirst = wert
        else: 
            print("Ungueltiger Wert!")
        
    def getMaximaleLieferfristInTagen(self):
        return self.__maximaleLieferFirst
    
    def spaetesterZustellTag(self, datum: Datum):
        maxTag = datum.tag + self.__maximaleLieferFirst 
        if(maxTag <= datum.tagImMonat[datum.monat]):
            return Datum(maxTag, datum.monat, datum.jahr).getString()
        elif(datum.monat < 12):
            tmp = maxTag - datum.tagImMonat[datum.monat]
            return Datum(tmp, datum.monat + 1, datum.jahr).getString()
        else:
            if(datum.monat == 12):
                tmp = maxTag - datum.tagImMonat[datum.monat]
                return Datum(tmp, 1, datum.jahr + 1).getString()
         
class ExpressManager():
    def __init__(self):
        self.expressPaketListe = []
        
    def aendereSpaetesteZustellungeInTagen(self, neuerWert: int):
        return False
      
test = ExpressPaket("kdsflkafhd")        
print(test.getAbsenderString())
print(test.spaetesterZustellTag(Datum(2, 2, 2022)))