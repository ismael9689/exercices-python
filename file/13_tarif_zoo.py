"""Exercice 13 : tarif zoo

Tarif d'entrée au zoo :
- moins de 3 ans : gratuit ;
- de 3 à 11 ans : 14,50 € ;
- 12 ans et plus avec carte jeune : 16,80 € ;
- 12 ans et plus sans carte jeune : 19,50 €.

Correction, trois erreurs :
1. En Python la virgule ne sert pas de séparateur décimal : 14,5 crée le tuple
   (14, 5). Il faut écrire 14.5.
2. Les « if » étaient indépendants : un enfant de 2 ans passait aussi dans
   age <= 11, puis dans le dernier else, et repartait avec 19,5. On enchaîne
   avec if / elif / else pour qu'une seule branche s'exécute.
3. La fonction ne renvoyait rien (pas de return), donc elle renvoyait None.
"""


def tarifZoo(age, carteJeune):
    if age < 3:
        prix = 0
    elif age <= 11:
        prix = 14.5
    elif carteJeune:
        prix = 16.8
    else:
        prix = 19.5
    return prix


if __name__ == "__main__":
    assert tarifZoo(2, False) == 0
    assert tarifZoo(8, True) == 14.5
    assert tarifZoo(18, True) == 16.8
    assert tarifZoo(30, False) == 19.5
    print("Exercice 13 : tous les tests passent.")
