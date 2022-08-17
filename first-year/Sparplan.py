jahre = float(input("Wie lange Sparen Sie in Jahren?\n"))
kapital = float(input("\nWas ist ihr Budget?\n"))

betrag = kapital
temp = 0
zinsen = 1.02

#Budget after set years
while(temp < jahre):
    betrag *= zinsen
    temp += 1
    
print("\nIhr Kapital beträgt nach " + str(format(jahre, ".0f")) + " Jahren " + str(format(betrag, ".2f")) + "€")

#After how many years budget is doubled
while(kapital * 2 > betrag):
    betrag *= zinsen
    jahre += 1
    
print("\nNach " + str(jahre) + " Jahren hat sich ihr Kapital verdoppelt und Beträgt " + str(format(betrag, ".2f")) + "€")

#Budget doubled after how many years? 
jahre = float(input("\nNach wie viel Jahren soll ich Ihr Kapital verdoppeln?\n"))

betrag = kapital
zinsen = 0.1

while(kapital * 2 > betrag):
    betrag = kapital
    zinsen += 0.1
    jahreTemp = jahre
    while(kapital * 2 > betrag and jahreTemp > 0):
        betrag *= zinsen / 100 + 1
        jahreTemp -= 1
    
print("\nNach " + str(jahre) + " Jahren und einem Zinsatz von " + str(format(zinsen, ".1f")) + "%" + " hat sich Ihr Kapital verdoppelt: " + str(format(betrag, ".2f")) + "€")
    