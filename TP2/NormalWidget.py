from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter
from Target import Target
from NormalCursor import NormalCursor
import csv


class NormalWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.targets = []
        self.cursor = None
        self.callback_clic = None

        try:
            self.charger_cibles('targets/src_tp_bubble.csv')
        except:
            self.targets = []
            self.cursor = None

    def charger_cibles(self, nom_fichier):
        self.targets = []
        try:
            with open(nom_fichier, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    t = Target(int(row[0]), int(row[1]), int(row[2]))
                    self.targets.append(t)

            self.cursor = NormalCursor(self.targets)
            self.update()
        except FileNotFoundError:
            print(f"Erreur: Impossible de charger {nom_fichier}")

    def activer_cible(self, id_cible):
        for t in self.targets:
            t.toSelect = False

        if 0 <= id_cible < len(self.targets):
            self.targets[id_cible].toSelect = True
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for target in self.targets:
            target.paint(painter)

        if self.cursor:
            self.cursor.paint(painter)

    def mouseMoveEvent(self, event):
        if self.cursor:
            self.cursor.move(event.pos().x(), event.pos().y())
            self.update()

    def mousePressEvent(self, event):
        if not self.cursor: return

        cible_survolee = self.cursor.closest
        succes = False

        if cible_survolee is not None and cible_survolee.toSelect:
            succes = True
            cible_survolee.toSelect = False

        self.update()

        if self.callback_clic:
            self.callback_clic(cible_survolee, succes)