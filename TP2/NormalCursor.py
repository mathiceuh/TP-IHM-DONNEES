from PyQt6.QtGui import QColor, QPen
import math


class NormalCursor:
    def __init__(self, cibles):
        self.x = 0
        self.y = 0
        self.cibles = cibles
        self.closest = None

    def paint(self, painter):
        painter.save()
        pen = QPen(QColor("white"))
        pen.setWidth(2)
        painter.setPen(pen)

        taille = 10
        painter.drawLine(self.x - taille, self.y, self.x + taille, self.y)
        painter.drawLine(self.x, self.y - taille, self.x, self.y + taille)
        painter.restore()

    def move(self, x, y):
        self.x = x
        self.y = y

        if self.closest is not None:
            self.closest.highlighted = False
            self.closest = None

        for cible in self.cibles:
            distance = math.sqrt((self.x - cible.x) ** 2 + (self.y - cible.y) ** 2)
            rayon = cible.size / 2

            if distance <= rayon:
                self.closest = cible
                self.closest.highlighted = True
                break