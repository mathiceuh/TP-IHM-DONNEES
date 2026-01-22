from PyQt6.QtGui import QColor
import math


class BubbleCursor:
    defaultCol = QColor("gray")  # Ou ta couleur choisie

    def __init__(self, targets):
        self.x = 0
        self.y = 0
        self.size = 0  # Initialisation à 0, sera maj par move
        self.targets = targets
        self.closest = None

    def paint(self, painter):
        if self.closest is None:
            return

        painter.save()
        couleur = QColor(self.defaultCol)
        couleur.setAlpha(128)
        painter.setBrush(couleur)
        painter.setPen(couleur)  # ou Qt.NoPen

        painter.drawEllipse(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)
        painter.restore()

    def move(self, x, y):
        self.x = x
        self.y = y

        if self.closest is not None:
            self.closest.highlighted = False

        min_dist = float('inf')
        new_closest = None

        for target in self.targets:
            dist_center = math.sqrt((self.x - target.x) ** 2 + (self.y - target.y) ** 2)

            dist_edge = dist_center - (target.size / 2)

            if dist_edge < min_dist:
                min_dist = dist_edge
                new_closest = target
                dist_center_closest = dist_center

        self.closest = new_closest
        if self.closest is not None:
            self.closest.highlighted = True

        self.size = int(dist_center_closest + (self.closest.size / 2))