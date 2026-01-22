import csv
import random
import time
import os
from PyQt6.QtWidgets import QApplication


class XPManager:
    def __init__(self, donnees_setup, widget):
        self.donnees = donnees_setup
        self.widget = widget

        self.blocs = []
        for densite in self.donnees["densites"]:
            for taille in self.donnees["tailles"]:
                self.blocs.append((densite, taille))

        random.shuffle(self.blocs)

        self.idx_bloc = 0
        self.idx_rep = 0
        self.idx_cible = 0
        self.sequence_cibles = []
        self.temps_debut_essai = 0

        self.dossier_logs = "logs"
        if not os.path.exists(self.dossier_logs):
            os.makedirs(self.dossier_logs)

        nom_fichier = f"log_{self.donnees['id_user']}_{self.donnees['technique']}.csv"
        self.nom_fichier_log = os.path.join(self.dossier_logs, nom_fichier)

        with open(self.nom_fichier_log, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["User", "Technique", "Density", "Size", "TargetID", "Time", "Success", "Timestamp"])

        self.charger_bloc()

    def charger_bloc(self):
        if self.idx_bloc >= len(self.blocs):
            print("=== EXPÉRIENCE TERMINÉE ===")
            QApplication.instance().quit()
            return

        densite, taille = self.blocs[self.idx_bloc]
        print(f"Début Bloc {self.idx_bloc + 1}/{len(self.blocs)} : Densité={densite}, Taille={taille}")

        fichier_pos = os.path.join("targets", f"targets_{densite}_{taille}.csv")
        fichier_seq = os.path.join("sequence", f"sequence_{densite}.csv")

        if os.path.exists(fichier_pos):
            self.widget.charger_cibles(fichier_pos)
        else:
            print(f"Erreur : Fichier cibles manquant : {fichier_pos}")
            QApplication.instance().quit()
            return

        if os.path.exists(fichier_seq):
            with open(fichier_seq, newline='') as f:
                reader = csv.reader(f)
                self.sequence_cibles = [int(x) for x in list(reader)[0]]
        else:
            print(f"Erreur : Fichier séquence manquant : {fichier_seq}")
            QApplication.instance().quit()
            return

        self.idx_rep = 0
        self.idx_cible = 0
        self.demarrer_essai()

    def demarrer_essai(self):
        if self.idx_cible < len(self.sequence_cibles):
            id_cible = self.sequence_cibles[self.idx_cible]
            self.widget.activer_cible(id_cible)
            self.temps_debut_essai = time.time()

    def traitement_clic(self, cible_obj, succes):
        temps_actuel = time.time()
        if self.temps_debut_essai == 0: return

        duree = (temps_actuel - self.temps_debut_essai) * 1000

        densite, taille = self.blocs[self.idx_bloc]
        id_cible = self.sequence_cibles[self.idx_cible]

        with open(self.nom_fichier_log, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                self.donnees['id_user'], self.donnees['technique'],
                densite, taille, id_cible, f"{duree:.2f}", succes, temps_actuel
            ])

        if succes:
            self.idx_cible += 1
            if self.idx_cible >= len(self.sequence_cibles):
                self.idx_cible = 0
                self.idx_rep += 1

                if self.idx_rep >= self.donnees['repetitions']:
                    self.idx_bloc += 1
                    self.charger_bloc()
                else:
                    self.demarrer_essai()
            else:
                self.demarrer_essai()