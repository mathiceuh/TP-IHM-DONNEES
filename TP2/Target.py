from PyQt6.QtGui import QColor


class Target:
    defaultCol = QColor("blue")
    highlightCol = QColor("yellow")
    toSelectCol = QColor("red")

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.toSelect = False
        self.highlighted = False

    def paint(self, peintre):
        couleur = Target.defaultCol

        if self.toSelect:
            couleur = Target.toSelectCol
        elif self.highlighted:
            couleur = Target.highlightCol

        peintre.setBrush(couleur)

        rayon = self.size / 2
        peintre.drawEllipse(int(self.x - rayon), int(self.y - rayon), self.size, self.size)
