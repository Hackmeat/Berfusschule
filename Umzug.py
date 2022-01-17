input = float (input("Geben Sie Ihre Umzugskosten an: "))
rabat = 0.15

if input >= 3000:
    rabat += 0.09
elif input >= 2000:
    rabat += 0.07
elif input >= 1000:
    rabat += 0.05

kostenGesamt = input * (1 - rabat)

print("\nIhre Gesamtkosten belaufen sich auf " + str(format(kostenGesamt, ".2f")) + "€")
