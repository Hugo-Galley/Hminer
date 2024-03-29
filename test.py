import re

def verifier_adresse_ethereum(adresse):
    # Expression régulière pour vérifier le format d'une adresse Ethereum
    regex_adresse_ethereum = r'^0x[a-fA-F0-9]{40}$'

    # Vérifier si l'adresse correspond au format attendu
    if re.match(regex_adresse_ethereum, adresse):
        return True
    else:
        return False

# Exemple d'utilisation
adresse_test = "0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5"
if verifier_adresse_ethereum(adresse_test):
    print("L'adresse Ethereum est au format valide.")
else:
    print("L'adresse Ethereum n'est pas au format valide.")
