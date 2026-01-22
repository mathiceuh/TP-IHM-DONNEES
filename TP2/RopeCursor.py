from BubbleCursor import BubbleCursor
from PyQt6.QtGui import QColor, QPen


class RopeCursor(BubbleCursor):
    def __init__(self, cibles):
        super().__init__(cibles)

    def paint(self, peintre):
        if self.closest is None:
            return

        peintre.save()

        crayon = QPen(QColor("white"))
        crayon.setWidth(2)
        peintre.setPen(crayon)

        peintre.drawLine(self.x, self.y, self.closest.x, self.closest.y)

        peintre.restore()