import string
import secrets

def generer_mot_de_passe(longueur=12):
    caracteres = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    mot_de_passe = ''.join(secrets.choice(caracteres) for _ in range(longueur))
    return mot_de_passe