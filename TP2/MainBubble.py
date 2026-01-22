import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ExpSetup import ExpSetup
from XPManager import XPManager
from BubbleWidget import BubbleWidget
from NormalWidget import NormalWidget
from RopeWidget import RopeWidget

def main():
    application = QApplication(sys.argv)
    setup = ExpSetup()

    if setup.exec():
        parametres = setup.recuperer_valeurs()
        technique = parametres.get("technique", "Normal")

        fenetre = QMainWindow()
        fenetre.resize(1024, 800)

        if technique == "Bubble":
            widget = BubbleWidget()
        elif technique == "Rope":
            widget = RopeWidget()
        else:
            widget = NormalWidget()

        fenetre.setCentralWidget(widget)
        manager = XPManager(parametres, widget)

        widget.callback_clic = manager.traitement_clic

        fenetre.show()
        sys.exit(application.exec())
    else:
        sys.exit()


if __name__ == "__main__":
    main()