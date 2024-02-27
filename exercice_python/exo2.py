print("welcom ...")
matier = {}
cpt = 0
nbrMatier = int(input("donner le nombre de matier : \t "))
while nbrMatier <= 0:
    nbrMatier = int(input("donner le nombre de matier : \t "))
for i in range(nbrMatier):
    print(f"***********Matier N°{i}*******************")
    nom = input("Donner le nom de la matier :\t")
    module = input("Donner le nom du module : \t")
    coef = int(input("Donner le coef : \t"))
    while coef < 1 or coef > 8:
        coef = int(input("Donner le coef : \t"))
    sousMat = {"non": nom, "module": module, "coef": coef}
    matier[f"Matier{cpt}"] = sousMat
    cpt += 1
clefs = [c for c in matier.keys()]
print(clefs)
print("\n*************************Menu*************************\n")
while True:
    print("1. Afficher la liste des matières")
    print("2. De modifier le contenu d’une matière")
    print("3. De supprimer une matière")
    print("4. D’ajouter une matière")
    print("Autre chose pour quitter")
    rp = int(input("Que voullez vous faire ? \t"))
    print("\n")
    if rp == 1:
        for i, j in matier.items():
            print(f"{i} ==> {j}")
    if rp == 2:
        index = int(input("Donner l'index que tu veux modifier \t"))
        while index >= len(matier) or index < 0:
            index = int(input("Donner l'index que tu veux modifier \t"))
        nomNew = input("Donner le nom de la matier :\t")
        moduleNew = input("Donner le nom du module : \t")
        coefNew = int(input("Donner le coef : \t"))
        sousMatnew = {"non": nomNew, "module": moduleNew, "coef": coefNew}
        matier[f"Matier{index}"] = sousMatnew
    if rp == 3:
        print("LES clefs possible a supprimer :")
        for i in matier.keys():
            print(i)
        clef = input("Donner la cle a supprimer \t").capitalize()
        if clef not in matier.keys():
            print("La clef ne se trouve pas dans notre dico :")
        else:
            del matier[clef]
    if rp == 4:
        newNom = input("Donner le nom de la matier :\t")
        newModule = input("Donner le nom du module : \t")
        newCoef = int(input("Donner le coef : \t"))
        newSousMat = {"non": newNom, "module": newModule, "coef": newCoef}
        matier[f"matier{cpt + 1}"] = newSousMat
    else:
        break
