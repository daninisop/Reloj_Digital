import sys
from datetime import datetime

from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget,QLabel,QVBoxLayout
from PyQt6.QtCore import QTimer


class RelojDigital(QWidget):
    def __init__(self):
        super().__init__()

        #Configuración de la ventana
        self.setWindowTitle("Reloj Digital ")
        self.setGeometry(100,100,400,200)
        self.setStyleSheet("background-color: #121212;")

        #Etiqueta de hora
        self.hora= QLabel()
        self.hora.setStyleSheet("color: #00FFCC; qproperty-alignment: AlignCenter;")

        #Etiqueta de la fecha
        self.fecha=QLabel()
        self.fecha.setStyleSheet("color: #00FFCC; qproperty-alignment: AlignCenter;")

        #layouts
        layout= QVBoxLayout()
        layout.addWidget(self.hora)
        layout.addWidget(self.fecha)

        self.setLayout(layout)

        #temporizador
        self.tiempo= QTimer()
        self.tiempo.timeout.connect(self.actualizar_reloj)
        self.tiempo.start(1000)

        #mostrar la hora
        self.actualizar_reloj()

    def actualizar_reloj(self):
        ahora=datetime.now()

        self.hora.setText(ahora.strftime("%H:%M:%S"))
        self.fecha.setText(ahora.strftime("%d/%m/%Y"))


app=QApplication(sys.argv)

ventana=RelojDigital()
ventana.show()

sys.exit(app.exec())



        



