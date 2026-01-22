import sys
import csv
import random
import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def main():
    if len(sys.argv) < 4:
        print("Usage: python generate_targets.py <nb_cibles> <taille> <espacement_min>")
        sys.exit(1)

    nb_cibles = int(sys.argv[1])
    taille_cible = int(sys.argv[2])
    espacement_min = int(sys.argv[3])

    largeur_ecran = 1024
    hauteur_ecran = 800
    marge = taille_cible + 10

    cibles = []
    tentatives_max = 100000

    while len(cibles) < nb_cibles and tentatives_max > 0:
        x = random.randint(marge, largeur_ecran - marge)
        y = random.randint(marge, hauteur_ecran - marge)

        collision = False
        for c in cibles:
            dist = distance((x, y), (c[0], c[1]))
            if dist < (taille_cible + espacement_min):
                collision = True
                break

        if not collision:
            cibles.append((x, y, taille_cible))

        tentatives_max -= 1

    if len(cibles) < nb_cibles:
        print(f"Erreur : Seulement {len(cibles)} cibles placées. Augmentez l'espace ou réduisez le nombre/taille.")
        sys.exit(1)

    nom_fichier_cibles = f"targets/targets_{nb_cibles}_{taille_cible}.csv"
    with open(nom_fichier_cibles, 'w', newline='') as f:
        writer = csv.writer(f)
        for c in cibles:
            writer.writerow(c)

    sequence = list(range(nb_cibles))
    random.shuffle(sequence)

    nom_fichier_seq = f"sequence/sequence_{nb_cibles}.csv"
    with open(nom_fichier_seq, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(sequence)


if __name__ == "__main__":
    main()