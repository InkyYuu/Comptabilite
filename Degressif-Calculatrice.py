date = input("Entrez votre date sous forme : jj mm ")
prix = int(input("Entrez votre prix : "))
tva = int(input("Entrez le montant de la TVA : "))
durée = int(input("Entre votre durée d'amortissement : "))

if durée < 5 and durée > 3:
    coeff = 1.25
elif durée > 4 and durée < 7:
    coeff = 1.75
elif durée > 6:
    coeff = 2.25

data = date.split(" ")
pro_rata = (12 - int(data[1]) + 1) / 12
HT = prix / (1 + (tva / 100))
pourcent = 100 / durée / 100
taux = pourcent * coeff
TL = 100 / durée
pr_annuité = HT * taux * pro_rata

print("|   N   |   VNC Début   |   Amortissement   |   Amortissement cumulé   |   VNC Fin   |   Taux Linéaire   |")
print("-" * 106)

for N in range(1, durée + 1):
    TL = 100 / (durée + 1 - N)
    if N == 1:
        VNC_Début = HT
        VNC_Fin = HT - pr_annuité
        Amort_Cumulé = pr_annuité
        print("|   ", N, "\n|   ", round(VNC_Début, 2), "\n|   ", round(pr_annuité, 2), "\n|   ", round(Amort_Cumulé, 2), "\n|   ", round(VNC_Fin, 2), "\n|   ", round(TL, 2), "%")
        input("Suite ?")
    elif TL > taux * 100:
        VNC_Début = VNC_Fin
        Amort = VNC_Début * (TL / 100)
        Amort_Cumulé += Amort
        VNC_Fin = VNC_Début - Amort
        print("|   ", N, "\n|   ", round(VNC_Début, 2), "\n|   ", round(Amort, 2), "\n|   ", round(Amort_Cumulé, 2), "\n|   ", round(VNC_Fin, 2), "\n|   ", round(TL, 2), "%")
        input("Suite ?")
    else:
        VNC_Début = VNC_Fin
        Amort = VNC_Début * taux
        Amort_Cumulé += Amort
        VNC_Fin = VNC_Début - Amort
        print("|   ", N, "\n|   ", round(VNC_Début, 2), "\n|   ", round(Amort, 2), "\n|   ", round(Amort_Cumulé, 2), "\n|   ", round(VNC_Fin, 2), "\n|   ", round(TL, 2), "%")
        input("Suite ?")
