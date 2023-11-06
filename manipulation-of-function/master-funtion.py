import random
import string
import re

def tounen_envès(mo):
    return print(" L'inverse de votre mo est :", mo[::-1])

def kòd_aleyatwa(n):
    return ''.join(random.choice(string.ascii_letters) for _ in range(n))

def kòd_aleyatwa_san_repetisyon(n):
    return ''.join(random.sample(string.ascii_letters, n))

def kòd_aleyatwa_alfanimerik(n):
    karaktè = string.ascii_letters + string.digits
    return ''.join(random.sample(karaktè, n))

def jenere_slug(chenn):
    chenn_san_karakter_anpwazon = re.sub(r'[^a-zA-Z0-9-]', '-', chenn)
    slug = '-'.join(chenn_san_karakter_anpwazon.split('-'))
    return slug

def separe_let_avek_vigl(mo):
    lèt_avek_vigl = ','.join(mo)
    return lèt_avek_vigl

def kripte_alfabet(mo):
    kripte = '-'.join(str(ord(k) - ord('A')) for k in mo)
    return kripte

def dekripte_alfabet(kripte):
    dekripte = ''.join(chr(int(i) + ord('A')) for i in kripte.split('-'))
    return dekripte

def retounen_2_vale(vale1, vale2):
    return vale2 , vale1

def inisyal_non(nom):
    inisyal = ''
    mo_koupe = nom.split('-')
    for mo in mo_koupe:
        inisyal += mo[0]
    return inisyal
 


if __name__=="__main__":
    
    while True:

        print("\t=====Manipulate that string======")
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
            text = input("Enter a word\n")
            tounen_envès(text)
        elif choice =='2':
            n = int(input("Enter a number\n"))
            kod = kòd_aleyatwa(n)
            print(kod)
        elif choice =='3':
            n = int(input("Enter a number\n"))
            kodAleyatwa = kòd_aleyatwa_alfanimerik(n)
            print(kodAleyatwa)
        elif choice =='4':
            n = int(input("Enter a number\n"))
            kodAleyatwa = kòd_aleyatwa_alfanimerik(n)
            print(kodAleyatwa)
        elif choice =='5':
            text = input("Enter a string\n")
            slug = jenere_slug(text)
            print(slug)
        elif choice =='6':
            text = input("Enter a word\n")
            word = separe_let_avek_vigl(text)
            print(word)
        elif choice =='7':
            text = input("Enter a string\n")
            word = kripte_alfabet(text)
            print(word)
        elif choice =='8':
            text = input("Enter a string\n")
            mo = dekripte_alfabet(text)
            print(mo)
        elif choice =='9':
            num1 = int(input("Enter the first number\n"))
            num2 = int(input("Enter the second number\n"))
            pemitasyon = retounen_2_vale(num1,num2)
            print(f"Avan pemitasyon ou antre {num1} e {num2}")
            print("Apre pemitation :", pemitasyon)
        elif choice =='10':
            text = input("Enter your name\n")
            name = inisyal_non(text)
            print(name)
        elif choice == '11':
            break
        else:
            print("You're wrong")
        

