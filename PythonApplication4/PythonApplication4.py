#print("Program vypise vsetky parne cisla")
#maximum = int(input("Zadajte macimalne cislo"))
#cislo = 0
#while cislo <= maximum:
#	if cislo % 2 == 0:
#		print(cislo)
#	cislo = cislo + 1
#input("Program ukoncite stlacenim lôubovolneho tlacidla")

#---------------------------------------------------------------
print("Program vypise pocet hlasok, samohlasok , cisel a ostatnych znakov v zadanom retazci")
slovo = input("Zadajte retazec ktory ideme skumat\n")
samohlasky =0
spoluhlasky =0
cisla =0
ostatneZnaky = 0
spoluZnaky = 0

for znak in slovo:
	if znak in "aáeéěiíoóuúůyý":
		samohlasky = samohlasky +1
	elif znak in "bcčdďfghjklmnňpqrřsštťvwxzž":
		spoluhlasky = spoluhlasky +1
	elif znak in "0123456789":
		cisla = cisla +1
	else:
		ostatneZnaky = ostatneZnaky +1
spoluZnaky = samohlasky + spoluhlasky + cisla + ostatneZnaky
print("Slovo ma dokopy: ", spoluZnaky, "znakov\n")
print(samohlasky, "samohlasok")
print(spoluhlasky, "spoluhlasok")
print(cisla, "cisel")
print(ostatneZnaky, "ostatnych znakov")
print("dakujeme")
