print("Vitajte v kalkulacke")
print()
prveCislo=float(input("Zadajte prve cislo"))
druheCislo = float(input("Zadajte druhe cislo"))

cisloOperacie = int(input("Zadajte cislo operacie,1234"))
if cisloOperacie == 1:
	print("sucet je" , prveCislo + druheCislo )
elif cisloOperacie == 2:
	print("rozdil je" , prveCislo - druheCislo )
elif cisloOperacie == 3:
	print("sucin je" , prveCislo * druheCislo )
elif cisloOperacie == 4:
	print("podiel je" , prveCislo / druheCislo)