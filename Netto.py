#Input
brutto = float (input("Gebe Bruttolohn ein: "))
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

#Output
print("Von Brutto " + str(format(brutto, ".2f")) + "€ bleiben " + str(format(netto, ".2f")) + "€ Netto übrig")