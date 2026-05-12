# =========================
# main.py - Interface CLI
# =========================

from generator import generate_password
from checker import check_password_strength
from utils import display_menu, clear_screen


def main():

    while True:

        display_menu()

        choice = input("\nChoix : ")

        if choice == "1":
            length = int(input("Longueur du mot de passe (8-20) : "))
            password = generate_password(length)
            print(f"\n[✔] Mot de passe généré : {password}")

        elif choice == "2":
            pwd = input("Entrez le mot de passe à tester : ")
            result = check_password_strength(pwd)

            print("\n===== RESULTAT =====")
            print(f"Score : {result['score']}/100")
            print(f"Niveau : {result['level']}")
            print("Feedback :")
            for f in result['feedback']:
                print(f"- {f}")

        elif choice == "3":
            print("Fermeture du programme...")
            break

        else:
            print("Choix invalide")


if __name__ == "__main__":
    main()
