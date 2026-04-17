def demander_longueur():
    try:
        longueur = int(input("Longueur du mot de passe : "))
        if 8 <= longueur <= 20:
            return longueur
        else:
            print(" Longueur invalide (8-20)")
            return None
    except:
        print(" Entrée invalide")
        return None