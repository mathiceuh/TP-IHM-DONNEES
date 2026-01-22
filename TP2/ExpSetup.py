from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QSpinBox, QPushButton


class ExpSetup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configuration Expérience")

        layout_principal = QVBoxLayout()
        self.setLayout(layout_principal)

        # Numéro d'utilisateur
        layout_user = QHBoxLayout()
        layout_user.addWidget(QLabel("ID Utilisateur :"))
        self.entree_user = QLineEdit()
        layout_user.addWidget(self.entree_user)
        layout_principal.addLayout(layout_user)

        # Technique
        layout_tech = QHBoxLayout()
        layout_tech.addWidget(QLabel("Technique :"))
        self.combo_tech = QComboBox()
        self.combo_tech.addItems(["Normal", "Bubble", "Rope"])
        layout_tech.addWidget(self.combo_tech)
        layout_principal.addLayout(layout_tech)

        # Densités
        layout_densites = QHBoxLayout()
        layout_densites.addWidget(QLabel("Densités (ex: 30,60,90) :"))
        self.entree_densites = QLineEdit("30,60,90")
        layout_densites.addWidget(self.entree_densites)
        layout_principal.addLayout(layout_densites)

        # Tailles
        layout_tailles = QHBoxLayout()
        layout_tailles.addWidget(QLabel("Tailles (ex: 6,12,18) :"))
        self.entree_tailles = QLineEdit("6,12,18")
        layout_tailles.addWidget(self.entree_tailles)
        layout_principal.addLayout(layout_tailles)

        # Répétitions
        layout_rep = QHBoxLayout()
        layout_rep.addWidget(QLabel("Répétitions :"))
        self.spin_rep = QSpinBox()
        self.spin_rep.setValue(1)
        self.spin_rep.setMinimum(1)
        layout_rep.addWidget(self.spin_rep)
        layout_principal.addLayout(layout_rep)

        # Bouton de validation
        self.bouton_valider = QPushButton("Valider")
        self.bouton_valider.clicked.connect(self.accept)
        layout_principal.addWidget(self.bouton_valider)

    def recuperer_valeurs(self):
        try:
            densites = [int(x) for x in self.entree_densites.text().split(',')]
        except ValueError:
            densites = [30, 60, 90]

        try:
            tailles = [int(x) for x in self.entree_tailles.text().split(',')]
        except ValueError:
            tailles = [6, 12, 18]

        return {
            "id_user": self.entree_user.text(),
            "technique": self.combo_tech.currentText(),  # C'est ici que la clé est définie
            "densites": densites,
            "tailles": tailles,
            "repetitions": self.spin_rep.value()
        }