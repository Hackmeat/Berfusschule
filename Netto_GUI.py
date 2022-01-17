#Imports
from tkinter import *

window = Tk()
window.title("Netto Rechner")

#Check an Item for FLoat status
def isFloat(x):
    try:
        float(x)
    except ValueError:
        return False
    else:
        return True

#Making the whole cal
def cal_Netto():    
    if(isFloat(brutto_textentry.get()) == True):
        brutto = float(brutto_textentry.get())
        if (brutto <= 0):
            noti_label.config(text="Positive Zahl eingeben!")
            netto_label.config(text="")
        else:
            temp = 0
            #Kranken, Renten, Arbeitslosen und Pflegeversicherung
            temp += brutto / 100 * 7.1
            temp += brutto / 100 * 9.75
            temp += brutto / 100 * 3.25
            temp += brutto / 100 * 0.85

            #Lohnsteuer
            if brutto <= 3000:
                lohnsteuer = brutto / 100 * 20
            if brutto > 3000 and brutto <= 4000:
                lohnsteuer = brutto / 100 * 25 
            if brutto > 4000 and brutto <= 5000:
                lohnsteuer = brutto / 100 * 30
            if brutto > 5000:
                lohnsteuer = brutto / 100 * 35

            temp += lohnsteuer

            #Kirchensteuer und Soli abhängig von Lohnsteuer
            temp += lohnsteuer / 100 * 8
            temp += lohnsteuer / 100 * 5.5

            netto = brutto - temp

            noti_label.config(text="Erfolgreich")
            netto_label.config(text=str(netto) + "€")
    else:
        noti_label.config(text="Keine Zahl!")


#UI Objects
noti_label = Label(window, text="Gebe Brutto ein!")
info_label = Label(window, text="Brutto: ")
result_label = Label(window, text="Netto: ")
netto_label = Label(window, text="")
brutto_textentry = Entry(window, bd=8, width = 15)
cal_button = Button(window, text="Berechne Netto", command = cal_Netto)

#Making order
noti_label.grid(row = 0, column = 1)
info_label.grid(row = 1, column = 0, pady = 20)
brutto_textentry.grid(row = 1, column = 1)
cal_button.grid(row = 2, column = 1)
result_label.grid(row = 3, column = 0, pady = 20)
netto_label.grid(row = 3, column = 1)

#Loop for the window
window.mainloop()