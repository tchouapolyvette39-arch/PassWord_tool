import re

def verifier_mot_de_passe(password):
    score = 0

    # Longueur
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Types de caractères
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Motifs faibles
    if "123" in password or "password" in password.lower():
        score -= 1

    # Résultat
    if score <= 2:
        niveau = "Faible"
    elif score <= 4:
        niveau = "Moyen"
    else:
        niveau = "Fort"

    return niveau, score