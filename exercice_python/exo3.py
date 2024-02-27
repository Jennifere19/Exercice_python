print("welcom...")
equipe = {}
cpt = 0
for i in range(3):
    print(f"*********Equipe N° {i + 1}************\n")
    equipe_domicile = input("Donner l'equipe domicile :\t")
    equipe_visiteur = input("Donner l'equipe visiteur :\t")
    but_domicile = int(input("Donner le nombre de but domicile :\t"))
    while but_domicile < 0:
        but_domicile = int(input("Donner le nombre de but domicile :\t"))
    but_visiteur = int(input("Donner le nombre de but visiteur :\t"))
    while but_visiteur < 0:
        but_visiteur = int(input("Donner le nombre de but visiteur :\t"))
    sousMat = {"equipe_domicile": equipe_domicile, "equipe_visiteur": equipe_visiteur, "but_domicile": but_domicile,
               "but_visiteur": but_visiteur}
    equipe[f"rencontre{cpt}"] = sousMat
    cpt += 1
while True:
    print("\n*************************Menu*************************\n")
    print("1.  Affiche les rencontres")
    print("2. Affiche les rencontres qui ont le plus de buts")
    print("3. Affiche les rencontres aux scores nul est vierge")
    print("4.  Affiche les rencontres remportées à domicile")
    rp = int(input("Que voullez vous faire ? \t"))
    print("\n")
    if rp == 1:
        print("\n")
        for i, j in equipe.items():
            print(f"{i} ==> {j}")
    if rp == 2:
        Max = 0
        pDB = []
        print("\n")
        for i, j in equipe.items():
            if j["but_domicile"] + j["but_visiteur"] > Max:
                Max = j["but_domicile"] + j["but_visiteur"]
                pDB.clear()
                pDB.append({i: j})
            if j["but_domicile"] + j["but_visiteur"] == Max:
                pDB.append({i: j})
        print(pDB)
    if rp == 3:
        for i, j in equipe.items():
            if j["but_domicile"] == 0 and j["but_visiteur"] == 0:
                print("\n")
                print(f"{i} ==> {j}")
    if rp == 4:
        for i, j in equipe.items():
            if j["but_domicile"] > j["but_visiteur"]:
                print(f"{i} ==> {j}")
    if rp != 1 and rp != 2 and rp != 3 and rp != 4 and rp != 5:
        print("votre choix est hors menu :")
    if rp == 5:
        print("Fin ...")
        break
