dauer = input("Gebe Dauer des Umsatzrückganges an: ")

fi_umsatz = float(100000000) #100 Mio
on_umsatz = float(30000000) # 30 Mio

fi_verlust = float(0.92)
on_gewinn = float(1.1)

for x in dauer:
    fi_umsatz = fi_umsatz * fi_verlust
    
print("\nUmsatz in Filale in " + str(dauer) + " Jahren liegt bei " + str(fi_umsatz))

fi_umsatz = float(100000000) #100 Mio
on_umsatz = float(30000000) # 30 Mio

fi_verlust = float(0.92)
on_gewinn = float(1.1)

dauer = 0

while(fi_umsatz > on_umsatz):
    dauer += 1
    fi_umsatz = fi_umsatz * fi_verlust
    on_umsatz = on_umsatz * on_gewinn
    
print("\nOnline Handel hat nach " + str(dauer) + " Jahren den Filal Handel überhollt!")

fi_umsatz = float(100000000) #100 Mio
on_umsatz = float(30000000) # 30 Mio

fi_verlust = float(0.92)
on_gewinn = float(1.1)

dauer = 5

while(fi_umsatz > on_umsatz):
    on_gewinn += 0.01
    fi_umsatz = float(100000000)
    on_umsatz = float(30000000)
    dauer = 5
    while(dauer != 0):
        fi_umsatz = fi_umsatz * fi_verlust
        on_umsatz = on_umsatz * on_gewinn
        dauer -= 1
        
print("\nOnline Handel muss " + str(format(on_gewinn, ".2f")) + "%" + " hoch sein um nach 5 Jahren besser da zu stehen")