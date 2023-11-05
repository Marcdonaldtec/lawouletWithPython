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
        print(text.index("a"))
    except ValueError:
        print("Char 'a' was not  found in the sentence")
def exercice8(text):
    indices_a = [i for i, char in enumerate(text) if char.lower() == 'a']
    sum = 0
    for i in indices_a:
        sum +=i
    print(sum)
def exercice9(text):
    indices_a = [i for i, char in enumerate(text) if char.lower() == 'a']
    print(indices_a)
def exercice10(text):
    removeSpace = text.replace(" ","")
    print("Your string without space is :",removeSpace)
    # countChar = removeSpace.len()
    print("The nomber of char is :", len(removeSpace))
    
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
            text = input("Enter a string\n")
            exercice1(text)
        elif choice =='2':
            text = input("Enter a string\n")
            exercice2(text)
        elif choice =='3':
            text = input("Enter a string\n")
            exercice3(text)
        elif choice =='4':
            text = input("Enter a string\n")
            exercice4(text)
        elif choice =='5':
            text = input("Enter a string\n")
            exercice5(text)
        elif choice =='6':
            text = input("Enter a string\n")
            exercice6(text)
        elif choice =='7':
            text = input("Enter a string\n")
            exercice7(text)
        elif choice =='8':
            text = input("Enter a string\n")
            exercice8(text)
        elif choice =='9':
            text = input("Enter a string\n")
            exercice9(text)
        elif choice =='10':
            text = input("Enter a string\n")
            exercice10(text)
        elif choice == '11':
            break
        else:
            print("You're wrong")
        

