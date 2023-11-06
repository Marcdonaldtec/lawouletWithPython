
def exercice1():
    n = int(input("How many integer do you want to enter\n"))
    lis_divizib_pa_2 = [x for x in range(n+1) if x % 2 == 0]
    print(f" La liste d'element divisible par 2 de 0 a {n} est :",lis_divizib_pa_2)

def exercice2():
    lis_antye = []
    listInt = int(input("How many integer do you want to enter\n"))
    for i in range(listInt):
        antye = int(input(f"Atre antye {i+1} \n"))
        lis_antye +=[antye,]
        lis_chenn = [str(x) for x in lis_antye]
        print(lis_chenn)

def exercice3():
    lis_chenn_miniskil = []
    lis_min = int(input("Konbyen eleman ou vle mete nan lis la\n"))
    for i in range(lis_min):
        min1 = input(f"Atre eleman {i+1} \n")
        lis_chenn_miniskil += [min1,]
        lis_chenn_majiskil = [min.upper() for min in lis_chenn_miniskil]
        print(lis_chenn_majiskil)

def exercice4():
    lis = []
    listInt = int(input("Konbyen eleman ou vle mete nan lis la\n"))
    for i in range(listInt):
        listEl = int(input(f"Antre eleman {i+1} \n"))
        lis += [listEl,]
    print("Anyen lis : ",lis)
    nouvo_lis = [lis[i] for i in range(len(lis)) if i % 3 == 0]
    print(" Nouvo lis : ",nouvo_lis)
def exercice5():
    lis1 = []
    lis = []
    li = 6
    listInt = int(input("Konbyen eleman ou vle mete nan lis la\n"))
    while listInt < li:
        listInt = int(input(f"Ou pa dwe antre pititi ke {li} eleman\n"))
        li +=1
    for i in range():
        listEl = int(input(f"Antre eleman {i+1} \n"))
        lis1 += [listEl,]
    lis = lis1
    print("Anyen lis : ",lis)
    nouvo_lis = [(lis[i], lis[i + 1], lis[i + 2]) for i in range(0, len(lis), 3)]
    print(" Nouvo lis : ",nouvo_lis)
def exercice6():
    lis = []
    listInt = int(input("Konbyen eleman ou vle mete nan lis la\n"))
    for i in range(listInt):
        listEl = int(input(f"Antre eleman {i+1} \n"))
        lis += [listEl,]
    print(" lis ak doublon : ",lis)
    lis_sans_doublon = list(set(lis))
    print(lis_sans_doublon)
    print(" List san doublon : ",lis_sans_doublon)

def exercice7():
    lis1 = []
    lis3 = []
    listInt1 = int(input("Konbyen eleman ou vle mete nan premye lis la\n"))
    for i in range(listInt1):
        listEl = int(input(f"Antre eleman {i+1} \n"))
        lis1 += [listEl,]
    lis3 = lis1
    
    lis2 = []
    lis4 = []
    listInt2 = int(input("Konbyen eleman ou vle mete nan dezyem lis la\n"))
    for i in range(listInt2):
        listEl = int(input(f"Antre eleman {i+1} \n"))
        lis2 += [listEl,]
    lis4 = lis2
    print("Premye lis : ",lis3)
    print("dezyem lis : ",lis4)
    lis_komen = [x for x in lis3 if x in lis4]
    print("Lis komen an se : ",lis_komen)

def exercice8():
    lis1 = []
    lis3 = []
    listInt1 = int(input("Konbyen eleman ou vle mete nan premye lis la\n"))
    for i in range(listInt1):
        listEl = int(input(f"Antre eleman {i+1} \n"))
        lis1 += [listEl,]
    lis3 = lis1
    
    lis2 = []
    lis4 = []
    listInt2 = int(input("Konbyen eleman ou vle mete nan dezyem lis la\n"))
    for i in range(listInt2):
        listEl = int(input(f"Antre eleman {i+1} \n"))
        lis2 += [listEl,]
    lis4 = lis2
    print("Premye lis : ",lis3)
    print("dezyem lis : ",lis4)
    lis_distenge = [x for x in lis3 if x not in lis4] + [x for x in lis4 if x not in lis3]
    print("Lis eleman diferan an se : ",lis_distenge)


def exercice9():
    diksyone = {'Janvye': 31, 'Fevriye': 28, 'Mas': 31}
    lis_kle = list(diksyone.keys())
    lis_vale = list(diksyone.values())
    print(lis_kle)
    print(lis_vale)
 
def exercice10():
    lis1 = []
    lis3 = []
    listInt1 = int(input("Konbyen eleman ou vle mete nan premye lis la\n"))
    for i in range(listInt1):
        listEl = int(input(f"Antre eleman {i+1} \n"))
        lis1 += [listEl,]
    lis3 = lis1
    
    lis2 = []
    lis4 = []
    listInt2 = int(input("Konbyen eleman ou vle mete nan dezyem lis la\n"))
    for i in range(listInt2):
        listEl = int(input(f"Antre eleman {i+1} \n"))
        lis2 += [listEl,]
    lis4 = lis2
    
    lis5 = []
    lis6 = []
    listInt3 = int(input("Konbyen eleman ou vle mete nan dezyem lis la\n"))
    for i in range(listInt3):
        listEl = int(input(f"Antre eleman {i+1} \n"))
        lis5 += [listEl,]
    lis6 = lis5
    
    print("Premye lis : ",lis3)
    print("dezyem lis : ",lis4)
    print("twazyem lis : ",lis6)
    lis_ansanm = list(set(lis3 + lis4 + lis6))
    print("twa lis eleman  se : ",lis_ansanm)

    
if __name__=="__main__":
    
    while True:

        print("\t=====Manipulation of the lists in python======")
        print("1. Exercice 1")
        print("2. Exercice 2")
        print("3. Exercice 3")
        print("4. Exercice 4")
        print("5. Exercice 5")
        print("6. Exercice 6")
        print("7. Exercice 7")
        print("8. Exercice 8")
        print("9. Exercice 9")
        print("10. Exercice 10")
        print("11. Exit\n")
        choice = input("\t==========Your choice=======\n")
        if choice =='1':
            exercice1()
        elif choice =='2':
            exercice2()
        elif choice =='3':
            exercice3()
        elif choice =='4':
            exercice4()
        elif choice =='5':
            exercice5()
        elif choice =='6':
            exercice6()
        elif choice =='7':
            exercice7()
        elif choice =='8':
            exercice8()
        elif choice =='9':
            exercice9()
        elif choice =='10':
            exercice10()
        elif choice == '11':
            break
        else:
            print("You're wrong")
        

