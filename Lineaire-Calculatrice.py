#Calcul amortissement linéraire pour le cours de gestion de projets de But Informatique 1eme année
date = input("Entrez votre date sous forme : jj mm ")
prix = int(input("Entrez votre prix : "))
tva = int(input("Entrez le montant de la TVA : "))
durée = int(input("Entre votre durée d'amortissement : "))

data = date.split(" ")
pro_rata = (30 - int(data[0])) + (12 - int(data[1])) * 30
HT = prix / (1 + (tva / 100))
pr_annuité = HT * (100 / durée / 100) * (pro_rata / 360)
pourcent = 100 / durée / 100

print("|   N   |   VNC Début   |   Amortissement   |   Amortissement cumulé   |   VNC Fin   |")
print("-" * 86)

for N in range(durée + 1):
    if N == 0:
        VNC_Début = HT
        VNC_Fin = HT - pr_annuité
        Amort_Cumulé = pr_annuité
        print("|   ", N, "\n|   ", round(VNC_Début, 2), "\n|   ", round(pr_annuité, 2), "\n|   ", round(Amort_Cumulé, 2), "\n|   ", round(VNC_Fin, 2))
        input("Suite ?")
    elif N == durée:
        VNC_Début = VNC_Fin
        Amort_Cumulé += HT * pourcent - pr_annuité
        Amort = HT * pourcent - pr_annuité
        VNC_Fin = VNC_Début - Amort
        print("|   ", N, "\n|   ", round(VNC_Début, 2), "\n|   ", round(Amort, 2), "\n|   ", round(Amort_Cumulé, 2), "\n|   ", round(VNC_Fin, 2))
    else:
        VNC_Début = VNC_Fin
        Amort_Cumulé += HT * pourcent
        Amort = HT * pourcent
        VNC_Fin = VNC_Début - Amort
        print("|   ", N, "\n|   ", round(VNC_Début, 2), "\n|   ", round(Amort, 2), "\n|   ", round(Amort_Cumulé, 2), "\n|   ", round(VNC_Fin, 2))
        input("Suite ?")
