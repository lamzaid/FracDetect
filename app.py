from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QComboBox, QMessageBox
from PyQt5.QtCore import Qt, QSize, QCoreApplication
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5 import QtCore


class MainWindow(QMainWindow):
    path_image = None
    nbre_predict_btn = 0
    part_of_body = None
    type = None
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FracDetect")

        self.setup_ui()

    def setup_ui(self):

        # Créer un widget central et un layout vertical
        central_widget = QWidget(self)
        layout = QHBoxLayout(central_widget)

        # Créer les labels pour chaque partie
        part1_label = QLabel()
        part1_layout = QVBoxLayout(part1_label)
        part11_label = QLabel()
        part12_label = QLabel()
        part2_label = QLabel("2")
        part3_label = QLabel("3")
        part4_label = QLabel("You can evolve the code of the application to add functionalities to this window by assigning the desired widgets and layouts using the variable part4_label.")
        part5_label = QLabel("You can evolve the code of the application to add functionalities to this window by assigning the desired widgets and layouts using the variable part5_label.")
        part6_label = QLabel("You can evolve the code of the application to add functionalities to this window by assigning the desired widgets and layouts using the variable part6_label.")
        font = QFont("Arial", 12, QFont.StyleItalic)  # Example: Arial, size 12, bold and italic
        part4_label.setFont(font)
        part5_label.setFont(font)
        part6_label.setFont(font)
        

        # Définir les styles des labels pour chaque partie
        part1_label.setStyleSheet("background-color: black; color: white;")
        part11_label.setStyleSheet("background-color: balck; color: white;")
        part12_label.setStyleSheet("background-color: black; color: white;")
        part2_label.setStyleSheet("background-color: black;")
        part3_label.setStyleSheet("background-color: black;")
        part4_label.setStyleSheet("background-color: #333333; color: white;")
        part5_label.setStyleSheet("background-color: #999999; color: white;")
        part6_label.setStyleSheet("background-color: #CCCCCC; color: white;")

        # Ajoutez les widgets QLabel enfants au layout parent
        part1_layout.addWidget(part11_label)
        part1_layout.addWidget(part12_label)

        # Ajout des labels au layout
        part1_layout.addWidget(part11_label, 1)  # 1/3
        part1_layout.addWidget(part12_label, 2)  # 2/3


        # Ajouter les labels au layout vertical avec les ratios souhaités
        layout.addWidget(part1_label, 1)
        layout.addWidget(part2_label, 2)
        layout.addWidget(part3_label, 2)
        layout.addWidget(part4_label, 4)
        layout.addWidget(part5_label, 4)
        layout.addWidget(part6_label, 4)

        part12_label.hide()
        part4_label.hide()
        part5_label.hide()
        part6_label.hide()


        # Créer les boutons pour la partie 1
        button1 = self.createBtn("./src/pics/file.ico")
        button2 = self.createBtn("./src/pics/folder.ico")
        button3 = self.createBtn("./src/pics/graph.ico")
        button4 = self.createBtn("./src/pics/params.ico")
        button5 = self.createBtn("./src/pics/info.ico")
        quit_button = self.createBtn("./src/pics/quit.ico")


        button1.setChecked(True)
        button1.setCheckable(True)


        # Connecter le signal des boutons au slot correspondant
        button1.clicked.connect(lambda: self.on_button1_clicked(part2_label, part3_label, part4_label, part5_label, part6_label))
        button2.clicked.connect(lambda: self.on_button2_clicked(part2_label, part3_label, part4_label, part5_label, part6_label))
        button3.clicked.connect(lambda: self.on_button3_clicked(part2_label, part3_label, part4_label, part5_label, part6_label))
        button4.clicked.connect(lambda: self.on_button4_clicked(part12_label))
        button5.clicked.connect(lambda: self.on_button5_clicked(part2_label, part3_label, part4_label, part5_label, part6_label))
        quit_button.clicked.connect(self.quit_application)


        # Créer un layout vertical pour les boutons de la partie 11
        buttons_layout1 = QHBoxLayout()
        buttons_layout1.addWidget(button1)
        buttons_layout1.addWidget(button2)
        buttons_layout1.addWidget(button3)
        buttons_layout2 = QHBoxLayout()
        buttons_layout2.addWidget(button4)
        buttons_layout2.addWidget(button5)
        buttons_layout2.addWidget(quit_button)


        # Ajouter le layout des boutons à la partie 11
        part11_layout = QVBoxLayout()
        part11_layout.addLayout(buttons_layout1)
        part11_layout.addLayout(buttons_layout2)
        
        part11_layout.addStretch()
        part11_label.setLayout(part11_layout)

        # Création des QComboBox
        combo1 = QComboBox()
        combo2 = QComboBox()

        # Ajout des options aux QComboBox
        combo1.addItem("Body Part")
        combo1.addItems(["ELBOW", "FINGER", "FOREARM", "HAND", "HUMERUS" , "SHOULDER", "WRIST"])
        combo2.addItem("Type")
        combo2.addItems(["Radiology", "Scanner", "IRM"])

        # Création du QPushButton
        button = QPushButton("Update values")

        # Connexion du signal clicked du QPushButton à la fonction on_button_clicked
        button.clicked.connect(lambda: self.on_button_clicked(combo1, combo2))

        # Création du QVBoxLayout pour organiser les widgets verticalement
        part12_layout = QVBoxLayout()
        part12_layout.setAlignment(QtCore.Qt.AlignTop)

        # Ajout des QComboBox et du QPushButton au QVBoxLayout
        part12_layout.addWidget(combo1)
        part12_layout.addWidget(combo2)
        part12_layout.addWidget(button)

        # Définition du QGroupBox comme widget central du QLabel
        part12_label.setLayout(part12_layout)

        # Application du style personnalisé aux QComboBox
        combo_style = '''
            QComboBox {
                background-color: #FFFFFF;
                border: 1px solid #CCCCCC;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                color: #000000;
                min-width: 150px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: right;
                width: 20px;
                border: none;
                background: none;
            }
            QComboBox::down-arrow {
                image: none;
            }
            QComboBox QAbstractItemView {
                background-color: #DDDDDD;
                border: 1px solid #CCCCCC;
                outline: none;
                padding: 5px;
                font-size: 12px;
                color: #000000;
            }
            QComboBox QAbstractItemView::item {
                color: #FFFFFF;
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: #555555;
            }
        '''

        combo1.setStyleSheet(combo_style)
        combo2.setStyleSheet(combo_style)

        # Application du style personnalisé au QPushButton
        button_style = '''
            QPushButton {
                background-color: #808080;
                color: #FFFFFF;
                border-radius: 25px;
                font-size: 18px;
                font-weight: bold;
                border: none;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #555555;
                cursor: pointer;
            }
            QPushButton:pressed {
                background-color: #333333;
            }
        '''
        button.setStyleSheet(button_style)

        # Ajouter un bouton pour importer une image dans la partie 2
        button_upload = QPushButton("Upload an image")
        button_upload.setStyleSheet('''
            QPushButton {
                background-color: #808080;
                color: #FFFFFF;
                border-radius: 25px;
                font-size: 18px;
                font-weight: bold;
                border: none;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #555555;
                cursor: pointer;
            }
            QPushButton:pressed {
                background-color: #333333;
            }
        ''')
        button_upload.clicked.connect(lambda: self.import_image(part2_label, part2_layout, part3_label))

        # Créer un layout vertical pour la partie 2
        part2_layout = QVBoxLayout()
        part2_layout.addWidget(button_upload)
        part2_layout.addStretch()
        part2_label.setLayout(part2_layout)

        # Définir le widget central
        self.setCentralWidget(central_widget)
   
    def createBtn(self, image_path):
        button = QPushButton(self)
        icon = QIcon(image_path)
        button.setIconSize(QSize(48, 48))
        button.setIcon(icon)
        return button
    
    def on_button1_clicked(self, part2_label, part3_label, part4_label, part5_label, part6_label):
        part2_label.show()
        part3_label.show()
        part4_label.hide()
        part5_label.hide()
        part6_label.hide()

    def on_button2_clicked(self, part2_label, part3_label, part4_label, part5_label,part6_label):
        part2_label.hide()
        part3_label.hide()
        part4_label.show()
        part5_label.hide()
        part6_label.hide()

    def on_button3_clicked(self, part2_label, part3_label, part4_label, part5_label,part6_label):
        part2_label.hide()
        part3_label.hide()
        part4_label.hide()
        part5_label.show()
        part6_label.hide()

    def on_button4_clicked(self, part12_label,):
        is_visible = part12_label.isVisible()
        if is_visible:
            part12_label.hide()
        else:
            part12_label.show()

    def on_button5_clicked(self, part2_label, part3_label, part4_label, part5_label,part6_label):
        part2_label.hide()
        part3_label.hide()
        part4_label.hide()
        part5_label.hide()
        part6_label.show()

    def on_button6_clicked(self, part2_label, part3_label, part4_label, part5_label,part6_label):
        part2_label.hide()
        part3_label.hide()
        part4_label.hide()
        part5_label.hide()
        part6_label.hide()

    def on_button_clicked(self, combo1, combo2):
        if combo1.currentText() == "Body Part" or combo2.currentText() =="Type":
            self.show_error_messages()
        else:
            self.part_of_body = combo1.currentText()
            self.type = combo2.currentText()
            print("Body part:", self.part_of_body)
            print("Type:", self.type)

    def show_error_messages(self):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setWindowTitle("Error")
        message_box.setText("Please select values for both combo boxes.")
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()
    
    def import_image(self, part2_label, part2_layout, part3_label):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            pixmap = QPixmap(file_path)
            # Redimensionner l'image
            scaled_pixmap = pixmap.scaled(part2_label.size() / 1.2, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
            part2_label.setPixmap(scaled_pixmap)
            part2_label.setAlignment(Qt.AlignCenter)
            if self.nbre_predict_btn ==0: 
                self.createPredictBtn(part2_layout, part3_label)
                self.nbre_predict_btn += 1
            self.path_image = file_path

    def createPredictBtn(self, part2_layout, part3_label):
        predict_button = QPushButton("Predict")
        predict_button.setStyleSheet('''
            QPushButton {
                background-color: #808080;
                color: #FFFFFF;
                border-radius: 25px;
                font-size: 18px;
                font-weight: bold;
                border: none;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #555555;
                cursor: pointer;
            }
            QPushButton:pressed {
                background-color: #333333;
            }
        ''')
        part2_layout.addWidget(predict_button)
        predict_button.clicked.connect(lambda: self.predict(part3_label))

    def resizeEvent(self, event):
        # Ignorer les événements de redimensionnement de la fenêtre
        self.setFixedSize(self.size())

    def predict(self, part3_label):
        if self.part_of_body != None and self.type != None:
            print(self.path_image)
            print(self.part_of_body)
            print(self.type)
            #file_path = model_hossame(self.path_image)
            file_path = "C:/Users/zaidl/Desktop/PFA2A/output.jpg"
            pixmap = QPixmap(file_path)
            # Redimensionner l'image
            scaled_pixmap = pixmap.scaled(part3_label.size() / 1.2, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
            part3_label.setPixmap(scaled_pixmap)
            part3_label.setAlignment(Qt.AlignCenter)
        else:
            self.show_error_messages()

    def quit_application(self):
        # Méthode pour quitter l'application
        QCoreApplication.quit()

# Créer une instance de QApplication
app = QApplication([])

# Créer une instance de la classe MainWindow
window = MainWindow()
window.setStyleSheet("background-color: black;")

# Obtenir la taille de l'écran principal
desktop = QApplication.desktop()
screen_rect = desktop.availableGeometry(desktop.primaryScreen())

# Définir la taille et la position de la fenêtre pour occuper tout l'écran, en laissant de l'espace pour la barre des tâches
window.setGeometry(screen_rect)

# Afficher la fenêtre
window.show()

# Exécuter la boucle d'événements de l'application
app.exec()
