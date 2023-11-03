import random
import sqlite3

connection = sqlite3.connect("lawoulet.db")
cursor = connection.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS score (
        id INTEGER PRIMARY KEY,
        username TEXT,
        score INTEGER
    )
''')
connection.commit()

min_number = 1
max_number = 5

def get_username():
    while True:
        username = input("Entrez votre pseudo (sans espaces, en minuscules): ")
        if username.islower() and ' ' not in username:
            return username
        else:
            print("Pseudo invalide. Veuillez entrer un pseudo en minuscules sans espaces.")

def get_user_score(username):
    cursor.execute("SELECT * FROM score WHERE username = ?", (username,))
    data = cursor.fetchone()
    return data[2] if data else 0

def update_user_score(username, score):
    cursor.execute("UPDATE score SET score = ? WHERE username = ?", (score, username))
    connection.commit()

def play_game(username):
    while True:
        secret_number = random.randint(min_number, max_number)
        print(f"J'ai choisi un nombre secret entre {min_number} et {max_number}.")

        attempts = 3
        score = attempts * 30

        while attempts > 0:
            find_secret_number = input(f"Il vous reste {attempts} essais. Devinez le nombre secret : ")
            try:
                find_secret_number = int(find_secret_number)
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                continue

            if find_secret_number < min_number or find_secret_number > max_number:
                print(f"Veuillez entrer un nombre entre {min_number} et {max_number}.")
                continue

            attempts -= 1

            if find_secret_number == secret_number:
                print("BRAVO ! Vous avez deviné le nombre secret.")
                print(f"Votre score pour cette partie est : {attempts * 30}")
                update_user_score(username, get_user_score(username) + attempts * 30)
                print(f"Votre score total est maintenant de : {get_user_score(username)}")
                break
            elif find_secret_number < secret_number:
                print("Le nombre secret est plus élevé. Réessayez.")
            else:
                print("Le nombre secret est plus bas. Réessayez.")

        else:
            print(f"Désolé, vous avez épuisé toutes vos tentatives. Le nombre secret était {secret_number}.")

        play_again = input("\nPou rejwe peze yon touch sou klavye a. Oubyen Peze 'K' pou kite jwet la\n ")
        if play_again.lower() != 'k':
            continue
        else:
            print("Au revoir!")
            break

if __name__ == "__main__":
    username = get_username()
    print(f"Bienvenue, {username}! Votre score actuel est {get_user_score(username)}")
    play_game(username)
