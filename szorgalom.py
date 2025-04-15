jegy = int(input('adj meg egy osztalyzatot\n'))

if jegy == 1:
    osztalyzat = "rossz"
elif jegy == 2:
    osztalyzat = "hanyag"
elif jegy == 3:
    osztalyzat = "változó"
elif jegy == 4:
    osztalyzat = "jó"
elif jegy == 5:
    osztalyzat = "példás"
else:
    print("nincs ilyen osztalyzat")

print("osztalyzat: ", jegy, "szorgalom: ", osztalyzat)