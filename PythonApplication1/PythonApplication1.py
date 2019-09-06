print("Vitajte v kalkulacke\n")
pokracovat = True

while pokracovat:
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
	else:
		print("neplatna volba")

	nezadane = True
	while nezadane:
		odpoved = input("prajete si opakovat ? y / n")
		if(odpoved == "y" or odpoved == "Y"):
			nezadane = False
		elif odpoved == "n" or odpoved == "N":
			nezadane = False
			pokracovat = False
		else:
			print("zadali ste blbost")
input("stlacte lubovcolnu klavesu")
