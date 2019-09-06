import math

meno = input("Ahoj ako sa volas?\n")
vlastnost = input("Aky si?\n")
print(meno + " je " + vlastnost)

cislo = int(input("Zadaj cele cislo k umocneniu"))
print("vysledok je : ", math.pow(cislo,2))

polomerKruhu = float(input("Zadaj polomer kruhu"))
print("Jeho obvod je :" , round((2*math.pi * polomerKruhu), 3), "cm^2")
print("Jeho obsah je :" , round((math.pi * math.pow(polomerKruhu,2)),4) , "cm^2")


