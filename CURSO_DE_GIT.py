# main.py
# Controlador principal que conecta TODAS las pantallas dentro de la carpeta `Pantallas`
# Estructura esperada:
# Pantallas/
#   Bienvenida.py
#   Pantalla_De_Inicio.py
#   Leccion_1.py
#   Leccion_2.py
#   Leccion_3.py
#   Leccion_4.py
#   Leccion_5.py
#   Leccion_6.py
#   Leccion_7.py
#   Leccion_8_quiz.py
#   Quiz_P1.py
#   Quiz_P2.py
#   Quiz_P3.py
#   Quiz_P4.py
#   Quiz_P5.py

import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget, QWidget, QMainWindow

# ===== IMPORTS DE PANTALLAS =====
from Pantallas import Bienvenida
from Pantallas import Pantalla_De_Inicio
from Pantallas import Lección_1
from Pantallas import Lección_2
from Pantallas import Lección_3
from Pantallas import Lección_4
from Pantallas import Lección_5
from Pantallas import Lección_6
from Pantallas import Lección_7
from Pantallas import Lección_8_quiz
from Pantallas import Quiz_P1
from Pantallas import Quiz_P2
from Pantallas import Quiz_P3
from Pantallas import Quiz_P4
from Pantallas import Quiz_P5


class App(QStackedWidget):
    def __init__(self):
        super().__init__()

        # ===== BIENVENIDA =====
    self.Bienvenida = QMainWindow()
    self.Bienvenida = Bienvenida()
    self.Bienvenida.setupUi(self.Bienvenida)

        # ===== MENÚ =====
    self.Pantalla_De_Inicio = QMainWindow()
    self.Pantalla_De_Inicio = Pantalla_De_Inicio()
    self.Pantalla_De_Inicio.setup(self.Pantalla_De_Inicio)

        # ===== LECCIONES =====
    self.Lección_1 = QMainWindow(); Leccion_1().setupUi(self.Lección_1)
    self.Lección_2 = QMainWindow(); Leccion_2().setupUi(self.Lección_2)
    self.Lección_3 = QMainWindow(); Leccion_3().setupUi(self.Lección_3)
    self.Lección_4 = QMainWindow(); Leccion_4().setupUi(self.Lección_4)

    self.Lección_5 = QMainWindow(); Leccion_5().setupUi(self.Lección_5)
    self.Lección_6 = QMainWindow(); Leccion_6().setupUi(self.Lección_6)
    self.Lección_7 = QMainWindow(); Leccion_7().setupUi(self.Lección_7)
    self.Lección_8_quiz = QMainWindow(); Leccion_8_quiz().setupUi(self.Lección_8_quiz)

        # ===== QUIZ =====
    self.Quiz_P1 = QMainWindow(); Quiz_P1().setupUi(self.Quiz_P1)
    self.Quiz_P2 = QMainWindow(); Quiz_P2().setupUi(self.Quiz_P2)
    self.Quiz_P3 = QMainWindow(); Quiz_P3().setupUi(self.Quiz_P3)
    self.Quiz_P4 = QMainWindow(); Quiz_P4().setupUi(self.Quiz_P4)        
    self.Quiz_P5 = QMainWindow(); Quiz_P5().setupUi(self.Quiz_P5)

        # ===== AGREGAR AL STACK =====
               
pantallas = [
    self.Bienvenida,
    self.Pantalla_De_Inicio,
    self.Lección_1,
    self.Lección_2,
    self.Lección_3,
    self.Lección_4,
    self.Lección_5,
    self.Lección_6,
    self.Lección_7,
    self.Lección_8_quiz,
    self.Quiz_P1,
    self.Quiz_P2,
    self.Quiz_P3,
    self.Quiz_P4,
    self.Quiz_P5
]

for w in pantallas:
    self.addWidget(w)

        # ===== CONEXIONES =====
    self.ui_Bienvenida.pushButton.clicked.connect(lambda: self.setCurrentWidget(self.Pantalla_De_Inicio))

    self.Pantalla_De_Inicio.pushButton.clicked.connect(lambda: self.setCurrentWidget(self.Lección_1))
    self.Pantalla_De_Inicio.pushButton_2.clicked.connect(lambda: self.setCurrentWidget(self.Lección_1))
    self.Pantalla_De_Inicio.pushButton_3.clicked.connect(QApplication.quit)

    self.Lección_1.findChild(type(self.ui_Bienvenida.pushButton), 'pushButton').clicked.connect(lambda: self.setCurrentWidget(self.Lección_2))
    self.Lección_2.findChild(type(self.ui_Bienvenida.pushButton), 'pushButton').clicked.connect(lambda: self.setCurrentWidget(self.Lección_3))
    self.Lección_3.findChild(type(self.ui_Bienvenida.pushButton), 'pushButton').clicked.connect(lambda: self.setCurrentWidget(self.Lección_4))
    self.Lección_4.findChild(type(self.ui_Bienvenida.pushButton), 'pushButton').clicked.connect(lambda: self.setCurrentWidget(self.Lección_5))
    self.Lección_5.findChild(type(self.ui_Bienvenida.pushButton), 'pushButton').clicked.connect(lambda: self.setCurrentWidget(self.Lección_6))
    self.Lección_6.findChild(type(self.ui_Bienvenida.pushButton), 'pushButton').clicked.connect(lambda: self.setCurrentWidget(self.Lección_7))
    self.Lección_7.findChild(type(self.ui_Bienvenida.pushButton), 'pushButton_2').clicked.connect(lambda: self.setCurrentWidget(self.Lección_8_quiz))
    self.Lección_8_quiz.findChild(type(self.ui_Bienvenida.pushButton), 'pushButton_2').clicked.connect(lambda: self.setCurrentWidget(self.Quiz_P1))

    self.Quiz_P1.pushButton_2.clicked.connect(lambda: self.setCurrentWidget(self.Quiz_P2))
    self.Quiz_P2.pushButton_6.clicked.connect(lambda: self.setCurrentWidget(self.Quiz_P3))
    self.Quiz_P3.pushButton_6.clicked.connect(lambda: self.setCurrentWidget(self.Quiz_P4))
    self.Quiz_P4.pushButton_2.clicked.connect(lambda: self.setCurrentWidget(self.Quiz_P5))
    self.Quiz_P5.pushButton_2.clicked.connect(QApplication.quit)

    self.setCurrentWidget(self.Bienvenida)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.setWindowTitle('Curso Básico de Git')
    window.resize(900, 650)
    window.show()
    sys.exit(app.exec_())
