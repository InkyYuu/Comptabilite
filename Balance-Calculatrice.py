type = input("Souhaitez vous une balance :\n1 - Une balance classique\n2 - Une balance par sommes et par soldes\nVotre choix : ")

if (type == '1') :
    balance = {}
    compte = input("Entrez votre numéro de compte (Mettre 0 pour arrêter) : ")
    if (compte != '0') :
        valeur = int(input("Entrez votre valeur : "))
    total_débit = 0
    total_crédit = 0
    while (compte != '0'):
        if valeur > 0 :
            if compte not in balance.keys():
                balance[compte] = [valeur,0]
            else : 
                balance[compte][0] += valeur
            total_débit += abs(valeur)
        else :
            if compte not in balance.keys():
                balance[compte] = [0,valeur]
            else : 
                balance[compte][1] -= valeur
            total_crédit += abs(valeur)
        compte = input("Entrez votre numéro de compte (Mettre 0 pour arrêter) : ")
        if (compte != '0') :
            valeur = int(input("Entrez votre valeur : "))
    balance = sorted(balance.items(), key=lambda t: t[0])
    print("|  N°  |    Débit     |    Crédit    |")
    print("--------------------------------------")

    for compte, valeur in balance :
        print("| ",int(compte)," | ",valeur[0]," | ",abs(valeur[1])," |")


    if total_débit > total_crédit :
        print("|  SD  |    ////    | ",abs(total_débit-total_crédit)," |")
        total_crédit += total_débit-total_crédit
    elif total_débit < total_crédit :
        print("|  SC  | ",abs(total_crédit-total_débit)," |    ////    |")
        total_débit += total_crédit-total_débit
    print("|Totaux| ",total_débit," | ",total_crédit," |")
else :
    balance = {}
    compte = input("Entrez votre numéro de compte (Mettre 0 pour arrêter) : ")
    if (compte != '0') :
        valeur = int(input("Entrez votre valeur : "))
    somme_débit = 0
    somme_crédit = 0
    while (compte != '0'):
        if valeur > 0 :
            if compte not in balance.keys():
                balance[compte] = [[valeur,0],[0,0]]
            else : 
                balance[compte][0][0] += valeur
            somme_débit += abs(valeur)
        else :
            if compte not in balance.keys():
                balance[compte] = [[0,valeur],[0,0]]
            else : 
                balance[compte][0][1] -= valeur
            somme_crédit += abs(valeur)
        compte = input("Entrez votre numéro de compte (Mettre 0 pour arrêter) : ")
        if (compte != '0') :
            valeur = int(input("Entrez votre valeur : "))
    solde_débit = 0
    solde_crédit = 0
    for compte, valeur in balance.items() :
        solde = valeur[0][0] - valeur[0][1]
        if solde > 0 :
            balance[compte][1][0] = solde
            solde_débit += abs(solde)
        else :
            balance[compte][1][1] = solde
            solde_crédit += abs(solde)
    balance = sorted(balance.items(), key=lambda t: t[0])
    print("|  N°  |     Somme     |     Solde     |")
    print("|//////|   D   |   C   |   D   |   C   |")
    print("----------------------------------------")
    for compte, valeur in balance :
        print("| ",int(compte)," | ",valeur[0][0]," | ",abs(valeur[0][1])," | ",valeur[1][0]," | ",abs(valeur[1][1])," |")
    
    somme_sd = 0
    somme_sc = 0
    solde_sd = 0
    solde_sc = 0

    if somme_débit > somme_crédit :
        somme_sd = somme_débit-somme_crédit
        somme_crédit += somme_débit-somme_crédit
    elif somme_débit < somme_crédit :
        somme_sc = somme_crédit-somme_débit
        somme_débit += somme_crédit-somme_débit

    if solde_débit > solde_crédit :
        solde_sd = solde_débit-solde_crédit
        solde_crédit += solde_débit-solde_crédit
    elif solde_débit < solde_crédit :
        solde_sc = solde_crédit-solde_débit
        solde_débit += solde_crédit-solde_débit
    if somme_sc != 0 or somme_sd != 0 or solde_sc != 0 or solde_sd != 0:
        print("| SD/SC | ",somme_sc," | ",somme_sd," | ",solde_sc," | ",solde_sd," |")
    print("|Totaux| ",somme_débit," | ",somme_crédit," | ",solde_débit," | ",solde_crédit," |")