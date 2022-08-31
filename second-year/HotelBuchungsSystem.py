#Aufgabe 1
class HottelKette():   
    def __init__(self, name):
        self.name = name
        self.hotelList = []       

class Hotel():    
    def __init__(self, name):
        self.name = name
        self.zimmerList = []
        self.buchungList = []
        
    def pruefebuchung(self, zimmerid, anTag, anMonat, anJahr, abTag, abMonat, abJahr):
        status = True
        i = 0
        anfahrt = Datum(anTag, anMonat, anJahr)
        abfahrt = Datum(abTag, abMonat, abJahr)
        while (i < self.buchungList.length):
            if (self.buchungList[i].zimmerid == zimmerid):
                #if(self.buchungList[i].anreise.tag >= anTag or self.buchungList[i].abreise.tag )
            i += 1
        return status
        
    def neueBuchung(self, zimmerid, anTag, anMonat, anJahr, abTag, abMonat, abJahr):
        ankunft = Datum(anTag, anMonat, anJahr)
        abfahrt = Datum(abTag, abMonat, abJahr)
        buchung = Buchung(ankunft, abfahrt, zimmerid)
        self.buchungList.append(buchung)
        
class Buchung():   
    def __init__(self, anreise, abreise, zimmerid):
        self.anreise = anreise
        self.abreise = abreise
        self.zimmerid = zimmerid
        
    def getBuchung(self):
        return "anreise: " + str(self.anreise) + ", abreise: " + str(self.abreise) + ", zimmmerNr: " + str(self.zimmerid)
        
class Datum():    
    def __init__(self, tag, monat, jahr):
        self.tag = tag
        self.monat = monat
        self.jahr = jahr
        
    def returnDatum(self):
        return str(self.tag) + "." + str(self.monat) + "." + str(self.jahr)
        
class Zimmer():   
    def __init__(self, id, typ, kategorie):
        self.id = id
        self.typ = typ #Doppel / Einzel
        self.kategorie = kategorie #Standard, Premium, Deluxe
        self.preis = -1

#Aufgabe 2
hotelAmSee = Hotel("Hotel am See")
parkHotel = Hotel("Parkhotel")

hotelAmSee.neueBuchung(2, 23, 2, 2020, 25, 2, 2020)
print(hotelAmSee.buchungList[0].getBuchung())

hotelAmSee.zimmerList.append(Zimmer(1, "Einzel", "Standard"))
parkHotel.zimmerList.append(Zimmer(1, "Einzel", "Standard"))
hotelAmSee.zimmerList.append(Zimmer(2, "Doppel", "Standard"))
hotelAmSee.zimmerList.append(Zimmer(3, "Doppel", "Premium"))
hotelAmSee.zimmerList.append(Zimmer(4, "Doppel", "Deluxe"))
parkHotel.zimmerList.append(Zimmer(2, "Doppel", "Standard"))
parkHotel.zimmerList.append(Zimmer(3, "Doppel", "Premium"))
parkHotel.zimmerList.append(Zimmer(4, "Doppel", "Deluxe"))

