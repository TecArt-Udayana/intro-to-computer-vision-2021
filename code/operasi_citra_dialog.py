from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class OperasiCitraDialog(QDialog):
    def __init__(self, jenis_operasi, parameter=None, parent=None):
        super(OperasiCitraDialog, self).__init__(parent)
        self.result = ""
        mainLayout = QVBoxLayout()

        self.jenis_operasi = jenis_operasi
        if jenis_operasi == 'Hough Transform Line':
            layoutSlider1 = QHBoxLayout()
            layoutSlider2 = QHBoxLayout()
            layoutSlider3 = QHBoxLayout()
            layoutSlider4 = QHBoxLayout()
            layoutSlider5 = QHBoxLayout()

            self.setWindowTitle("Atur threshold")
            self.convertslider = QSlider()
            self.convertslider.setOrientation(Qt.Horizontal)
            self.convertslider.setTickPosition(QSlider.TicksBelow)
            self.convertslider.setTickInterval(1)
            self.convertslider.setMinimum(0)
            self.convertslider.setMaximum(500)
            layoutSlider1.addWidget(self.convertslider)

            slider1Group = QGroupBox("Threshold (Min 0 max 500)")
            slider1Group.setLayout(layoutSlider1)

            self.convertslider2 = QSlider()
            self.convertslider2.setOrientation(Qt.Horizontal)
            self.convertslider2.setTickPosition(QSlider.TicksBelow)
            self.convertslider2.setTickInterval(1)
            self.convertslider2.setMinimum(1)
            self.convertslider2.setMaximum(255)
            layoutSlider2.addWidget(self.convertslider2)

            slider2Group = QGroupBox("Panjang Garis Minimum")
            slider2Group.setLayout(layoutSlider2)

            self.convertslider3 = QSlider()
            self.convertslider3.setOrientation(Qt.Horizontal)
            self.convertslider3.setTickPosition(QSlider.TicksBelow)
            self.convertslider3.setTickInterval(1)
            self.convertslider3.setMinimum(0)
            self.convertslider3.setMaximum(500)
            layoutSlider3.addWidget(self.convertslider3)

            slider3Group = QGroupBox("Jarak Garis Maksimum")
            slider3Group.setLayout(layoutSlider3)

            self.convertslider4 = QSlider()
            self.convertslider4.setOrientation(Qt.Horizontal)
            self.convertslider4.setTickPosition(QSlider.TicksBelow)
            self.convertslider4.setTickInterval(1)
            self.convertslider4.setMinimum(0)
            self.convertslider4.setMaximum(255)
            layoutSlider4.addWidget(self.convertslider4)

            slider4Group = QGroupBox("Threshold 1 Canny (Min 0 Max 255)")
            slider4Group.setLayout(layoutSlider4)

            self.convertslider5 = QSlider()
            self.convertslider5.setOrientation(Qt.Horizontal)
            self.convertslider5.setTickPosition(QSlider.TicksBelow)
            self.convertslider5.setTickInterval(1)
            self.convertslider5.setMinimum(0)
            self.convertslider5.setMaximum(255)
            layoutSlider5.addWidget(self.convertslider5)

            slider5Group = QGroupBox("Threshold 2 Canny (Min 0 Max 255)")
            slider5Group.setLayout(layoutSlider5)

            mainLayout.addWidget(slider1Group)
            mainLayout.addWidget(slider2Group)
            mainLayout.addWidget(slider3Group)
            mainLayout.addWidget(slider4Group)
            mainLayout.addWidget(slider5Group)
        elif jenis_operasi == 'Hough Transform Circle':
            layoutSlider1 = QHBoxLayout()
            layoutSlider2 = QHBoxLayout()
            layoutSlider3 = QHBoxLayout()
            layoutSlider4 = QHBoxLayout()
            layoutSlider5 = QHBoxLayout()
            layoutSlider6 = QHBoxLayout()

            self.setWindowTitle("Atur parameter Hough Transform Circle Detection")
            self.convertslider = QSlider()
            self.convertslider.setOrientation(Qt.Horizontal)
            self.convertslider.setTickPosition(QSlider.TicksBelow)
            self.convertslider.setTickInterval(1)
            self.convertslider.setMinimum(0)
            self.convertslider.setMaximum(255)
            layoutSlider1.addWidget(self.convertslider)

            slider1Group = QGroupBox("Strong Pixel (Min 0 Max 255)")
            slider1Group.setLayout(layoutSlider1)

            self.convertslider2 = QSlider()
            self.convertslider2.setOrientation(Qt.Horizontal)
            self.convertslider2.setTickPosition(QSlider.TicksBelow)
            self.convertslider2.setTickInterval(1)
            self.convertslider2.setMinimum(1)
            self.convertslider2.setMaximum(255)
            layoutSlider2.addWidget(self.convertslider2)

            slider2Group = QGroupBox("Weak Pixel (Min 0 Max 255)")
            slider2Group.setLayout(layoutSlider2)

            self.convertslider3 = QSlider()
            self.convertslider3.setOrientation(Qt.Horizontal)
            self.convertslider3.setTickPosition(QSlider.TicksBelow)
            self.convertslider3.setTickInterval(1)
            self.convertslider3.setMinimum(0)
            self.convertslider3.setMaximum(500)
            layoutSlider3.addWidget(self.convertslider3)

            slider3Group = QGroupBox("Radius Lingkaran Minimum (Min 0 Max 500)")
            slider3Group.setLayout(layoutSlider3)

            self.convertslider4 = QSlider()
            self.convertslider4.setOrientation(Qt.Horizontal)
            self.convertslider4.setTickPosition(QSlider.TicksBelow)
            self.convertslider4.setTickInterval(1)
            self.convertslider4.setMinimum(0)
            self.convertslider4.setMaximum(500)
            layoutSlider4.addWidget(self.convertslider4)

            slider4Group = QGroupBox("Radius Lingkaran Maksimum (Min 0 Max 500)")
            slider4Group.setLayout(layoutSlider4)

            self.convertslider5 = QSlider()
            self.convertslider5.setOrientation(Qt.Horizontal)
            self.convertslider5.setTickPosition(QSlider.TicksBelow)
            self.convertslider5.setTickInterval(1)
            self.convertslider5.setMinimum(0)
            self.convertslider5.setMaximum(255)
            layoutSlider5.addWidget(self.convertslider5)

            slider5Group = QGroupBox("Threshold 1 Canny (Min 0 Max 255)")
            slider5Group.setLayout(layoutSlider5)

            self.convertslider6 = QSlider()
            self.convertslider6.setOrientation(Qt.Horizontal)
            self.convertslider6.setTickPosition(QSlider.TicksBelow)
            self.convertslider6.setTickInterval(1)
            self.convertslider6.setMinimum(0)
            self.convertslider6.setMaximum(255)
            layoutSlider6.addWidget(self.convertslider6)

            slider6Group = QGroupBox("Threshold 2 Canny (Min 0 Max 255)")
            slider6Group.setLayout(layoutSlider6)

            mainLayout.addWidget(slider1Group)
            mainLayout.addWidget(slider2Group)
            mainLayout.addWidget(slider3Group)
            mainLayout.addWidget(slider4Group)
            mainLayout.addWidget(slider5Group)
            mainLayout.addWidget(slider6Group)

        buttonLayout = QHBoxLayout()
        self.btnJalankan = QPushButton("OK")
        buttonLayout.addWidget(self.btnJalankan)
        self.btnJalankan.clicked.connect(self.OnOk)

        self.btnBatalkan = QPushButton("Cancel")
        buttonLayout.addWidget(self.btnBatalkan)
        self.btnBatalkan.clicked.connect(self.OnCancel)

        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)

    def OnOk(self):
        if self.jenis_operasi == 'Hough Transform Line':
            self.result = [self.convertslider.value(), self.convertslider2.value(), self.convertslider3.value(),
                           self.convertslider4.value(), self.convertslider5.value()]
        elif self.jenis_operasi == 'Hough Transform Circle':
            self.result = [self.convertslider.value(), self.convertslider2.value(), self.convertslider3.value(),
                           self.convertslider4.value(), self.convertslider5.value(), self.convertslider6.value()]
        self.done(1)
        return self.result

    def OnCancel(self):
        self.close()

    def GetValue(self):
        return self.result
