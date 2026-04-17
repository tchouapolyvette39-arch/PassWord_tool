from generator import generer_mot_de_passe
from checker import verifier_mot_de_passe
from utils import demander_longueur

def menu():
    while True:
        print("\n=== PASSWORD TOOL ===")
        print("1. Générer un mot de passe")
        print("2. Tester un mot de passe")
        print("3. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            longueur = demander_longueur()
            if longueur:
                pwd = generer_mot_de_passe(longueur)
                print(f"Mot de passe généré : {pwd}")

        elif choix == "2":
            pwd = input("Entrer le mot de passe : ")
            niveau, score = verifier_mot_de_passe(pwd)
            print(f"Niveau : {niveau} (Score: {score})")

        elif choix == "3":
            print("Au revoir ")
            break

        else:
            print("Choix invalide")

if __name__ == "__main__":
    menu()