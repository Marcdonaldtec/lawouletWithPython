def exercice1(text):
    return  print(text.lower())
def exercice2(text):
    return  print(text.split())
def exercice3(text):
    return  print(text.title())
def exercice4(text):
    firstLetter = [letter[0] for letter in text.split()]
    print(firstLetter)
    newString = ''.join(firstLetter)
    print(newString)
def exercice5(text):
    return  print(text.replace("a","@"))
def exercice6(text):
    return  print(text[::-1].upper())
def exercice7(text):
    try:
        print(text.index("z"))
    except ValueError:
        print("Char 'z' was not  found in the sentence")
def exercice8(text):
    return  print(text.split())
def exercice9(text):
    return  print(text.split())
def exercice10(text):
    return  print(text.split())

if __name__=="__main__":
    choice = '11'
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
            text = input("Enter a string\n")
            exercice1(text)
        elif choice =='2':
            text = input("Enter a string\n")
            exercice2(text)
        elif choice =='3':
            text = input("Enter a string\n")
            exercice2(text)
        elif choice =='4':
            text = input("Enter a string\n")
            exercice2(text)
        elif choice =='5':
            text = input("Enter a string\n")
            exercice2(text)
        elif choice =='6':
            text = input("Enter a string\n")
            exercice2(text)
        elif choice =='7':
            text = input("Enter a string\n")
            exercice2(text)
        elif choice =='8':
            exercice2(text)
        elif choice =='9':
            exercice2(text)
        elif choice =='10':
            exercice2(text)
        elif choice == '11':
            break
       
# # exo 1
# text = " Hello Everybody this is Marc Donald OMEUS"

# # exo 2 
# print(text.split())

# # exo 3
# print(text.title())

# # exo 4
# firstLetter = [letter[0] for letter in text.split()]
# print(firstLetter)
# newString = ''.join(firstLetter)
# print(newString)

# exo 5
# print(text.replace("a","@"))

# # exo 6
# print(text[::-1].upper())

# # exo 7
# try:
#     print(text.index("z"))
# except ValueError:
#     print("Char 'z' was not  found in the sentence")
# # exo 8
# print(text.lower().count("a"))
# indexCharA = text.index("a")
# summ = 0
# i =0
# while True:
#     if indexCharA:
#         summ +=indexCharA
#         i +=1
#         break
#     print(summ)   
    

