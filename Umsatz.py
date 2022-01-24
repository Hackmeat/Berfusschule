#Income after 5 years
dauer = 5
fi_umsatz = float(100000000) #100 Mio
on_umsatz = float(30000000) # 30 Mio

fi_verlust = float(0.92)
on_gewinn = float(1.1)

while(dauer > 0):
    fi_umsatz = fi_umsatz * fi_verlust
    dauer -= 1
    
print("\nUmsatz in Filale in 5 Jahren liegt bei " + str(fi_umsatz))

#When online shop brings in more money
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

#How much faster online shopping has to increase
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