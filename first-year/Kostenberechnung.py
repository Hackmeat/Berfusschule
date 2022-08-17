#Loup - if input to low
bezugspreis = 0
while bezugspreis <= 0:

    #Input
    bezugspreis = float (input("Gebe Bezugspreis ein: "))

    #Calculation
    if bezugspreis > 0:
        handelskosten = (bezugspreis / 100 * 125)
        gewinn = (handelskosten / 100 * 120)
        verkaufskonto = (gewinn / 98 * 100)
        verkaufsrabatt = (verkaufskonto / 95 * 100)
        listenpreisBrutto = (verkaufsrabatt / 100 * 119)

    #Output
        print("\nDer Bezugspreis liegt bei " + str(format(bezugspreis, ".2f")) + "€")
        print("Der Listenverkaufspreis in Brutto beträgt " + str(f'{listenpreisBrutto:.2f}') + "€")
    else:
        print("\nGebe Bezugspreis größer 0 ein!\n")