"""Exercice 9 : prix billet

Prix d'un billet selon le jour de la semaine (1 = lundi ... 7 = dimanche)
et le nombre de jours. Renvoie -1 si le jour est invalide.
- Lundi à jeudi : 30 € par jour, -10 % au-delà de 3 jours, -20 % au-delà de 5 jours.
- Vendredi à dimanche : 50 € par jour, -10 % au-delà de 5 jours.

Correction : avec « if jours > 3 ... elif jours > 5 », la branche elif n'était
jamais atteinte (tout nombre > 5 est aussi > 3, donc la première condition gagne).
Il faut tester la condition la plus forte en premier : jours > 5, puis jours > 3.
"""


def prix_billet(jour_semaine: int, jours: int) -> float:
    if jour_semaine < 1 or jour_semaine > 7:
        return -1
    if jour_semaine <= 4:
        prix = 30 * jours
        if jours > 5:
            prix = prix * (1 - 20 / 100)
        elif jours > 3:
            prix = prix * (1 - 10 / 100)
    else:
        prix = 50 * jours
        if jours > 5:
            prix = prix * (1 - 10 / 100)
    return prix


if __name__ == "__main__":
    assert prix_billet(0, 2) == -1
    assert prix_billet(1, 2) == 60
    assert prix_billet(2, 4) == 108
    assert prix_billet(3, 6) == 144
    assert prix_billet(6, 3) == 150
    assert prix_billet(7, 6) == 270
    print("Exercice 9 : tous les tests passent.")
