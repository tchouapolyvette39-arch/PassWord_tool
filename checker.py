# =========================
# checker.py
# =========================

import re


WEAK_PATTERNS = ["123", "password", "admin", "qwerty", "azerty"]


def check_password_strength(password):

    score = 0
    feedback = []

    # Longueur
    if len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 20
    else:
        feedback.append("Mot de passe trop court")

    # Majuscules
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Ajoutez des majuscules")

    # Minuscules
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Ajoutez des minuscules")

    # Chiffres
    if re.search(r"[0-9]", password):
        score += 20
    else:
        feedback.append("Ajoutez des chiffres")

    # Caractères spéciaux
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        feedback.append("Ajoutez des caractères spéciaux")

    # Motifs faibles
    for pattern in WEAK_PATTERNS:
        if pattern in password.lower():
            score -= 20
            feedback.append(f"Mot interdit détecté : {pattern}")

    # Niveau final
    if score >= 80:
        level = "FORT 🔒"
    elif score >= 50:
        level = "MOYEN ⚠️"
    else:
        level = "FAIBLE ❌"

    return {
        "score": max(score, 0),
        "level": level,
        "feedback": feedback
    }
