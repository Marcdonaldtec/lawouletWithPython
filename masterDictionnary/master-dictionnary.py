
def rekipere_vale_gras_ak_kle(diksyone):
    lis_vale = list(diksyone.values())
    return lis_vale

def afiche_tout_kle(diksyone):
    kle = diksyone.keys()
    print(list(kle))

def afiche_tout_vale(diksyone):
    vale = diksyone.values()
    print(list(vale))

def kreye_kopi_diksyone(diksyone):
    nouvo_diksyone = dict(diksyone)
    return nouvo_diksyone

def ajoute_underscore(diksyone):
    nouvo_diksyone = {}
    for kle, vale in diksyone.items():
        if isinstance(vale, str):
            nouvo_diksyone[kle] = f"_{vale}_"
        else:
            nouvo_diksyone[kle] = vale
    return nouvo_diksyone

def seleksyone_vale_oubyen_tout_dijit(diksyone):
    nouvo_diksyone = {k: v for k, v in diksyone.items() if all(c.isdigit() for c in v)}
    return nouvo_diksyone

def mete_sou_fòm_lis(diksyone):
    lis_kle_vale = [(k, v) for k, v in diksyone.items()]
    return lis_kle_vale

if __name__=="__main__":
    print("\tNou pral manipile diksyone ak python \n")
    print("Creer un dictionnaire vide pour stocker les informations des employes")
    
    employe_dict = {}

    nom = input("Entrez le nom de l'employe : ")
    prenom = input("Entrez le prenom de l'employe : ")
    age = int(input("Entrez l'age de l'employe : "))
    poste = input("Entrez le poste de l'employe : ")
    
   
    employe_dict["Nom"] = nom
    employe_dict["Prenom"] = prenom
    employe_dict["Age"] = age
    employe_dict["Poste"] = poste
    
    print("\nInformations de l'employe :")
    for cle, valeur in employe_dict.items():
       print(f"{cle}: {valeur}")

    while True:

        print("\t=====Manipulation of the dictionnary======")
        print("1. Rekipere tout vale yo:")
        print("2. Afiche tout kle yo:")
        print("3. Afiche tout vale yo:")
        print("4. Kreye kopi (nouvo) sou diksyone a:")
        print("5. Ajoute underscore devan ak deye tout vale ki se chenn:")
        print("6. Seleksyone vale ki dijit selman:")
        print("7. Mete sou fòm lis:")
        print("8. Exit\n")
        choice = input("\t==========Your choice=======\n")
        if choice =='1':
            dik = rekipere_vale_gras_ak_kle(employe_dict)
            print(dik)
        elif choice =='2':
            dik1 = afiche_tout_kle(employe_dict)
            print(dik1)
        elif choice =='3':
            dik3 = afiche_tout_vale(employe_dict)
            print(dik3)
        elif choice =='4':
            dik4 = kreye_kopi_diksyone(employe_dict)
            print(dik4)
        elif choice =='5':
            dik5 = ajoute_underscore(employe_dict)
            print(dik5)
        elif choice =='6':
            dik6 = seleksyone_vale_oubyen_tout_dijit(employe_dict)
            print(dik6)
        elif choice =='7':
            dik7 = mete_sou_fòm_lis(employe_dict)
            print(dik7)
        elif choice == '8':
            break
        else:
            print("You're wrong")