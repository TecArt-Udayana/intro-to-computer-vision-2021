import sys
import os

from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QColor, QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QCheckBox, QComboBox, QFileDialog, QMainWindow, QLabel, QPushButton, QSlider, \
    QTabWidget, QWidget, QListWidget, QMessageBox
import cv2
import numpy as np
import os
import hough
from operasi_citra_dialog import OperasiCitraDialog


# Untuk menampilkan preview warna HSV
def generateSolidColorPixmap(w, h, color):
    canvas = QImage(QSize(w, h), QImage.Format_RGB30)
    for baris in range(0, h):
        for kolom in range(0, w):
            canvas.setPixel(kolom, baris, color.rgb())
    return canvas


class MainWindow(QMainWindow):
    selectedHue = 0
    selectedSaturation = 255
    selectedValue = 255

    lowerHSV = (0, 0, 0)
    upperHSV = (179, 255, 255)

    imgRaw = None
    imgMask = None
    imgMasked = None

    imgHsvSpace = None

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(os.path.join(os.path.dirname(
            __file__), "main_window.ui"), self)

        self.tabs = self.findChild(QTabWidget, "tabWidget")
        self.tabs.setTabText(0, "HSV Demo")
        self.tabs.setTabText(1, "Computer Vision Demo")
        self.tabs.setCurrentIndex(0)
        self.init_hsv_tab_ui()
        self.init_hough_tab_gui()

    def init_hsv_tab_ui(self):
        self.sliderH = self.findChild(QSlider, "sliderH")
        self.sliderS = self.findChild(QSlider, "sliderS")
        self.sliderV = self.findChild(QSlider, "sliderV")

        self.lblH = self.findChild(QLabel, "lblH")
        self.lblS = self.findChild(QLabel, "lblS")
        self.lblV = self.findChild(QLabel, "lblV")

        self.lblLower = self.findChild(QLabel, "lblLower")
        self.lblUpper = self.findChild(QLabel, "lblUpper")

        self.previewH = self.findChild(QLabel, "previewH")
        self.previewS = self.findChild(QLabel, "previewS")
        self.previewV = self.findChild(QLabel, "previewV")

        self.previewRaw = self.findChild(QLabel, "previewRaw")
        self.previewMask = self.findChild(QLabel, "previewMask")
        self.previewMaskedRaw = self.findChild(QLabel, "previewMaskedRaw")
        self.previewHsvSpace = self.findChild(QLabel, "previewHsvSpace")

        self.cboxSetMode = self.findChild(QComboBox, "cboxSetMode")

        self.cboxErode = self.findChild(QCheckBox, "cboxErode")
        self.sliderErotion = self.findChild(QSlider, "sliderErotion")
        self.cboxDilate = self.findChild(QCheckBox, "cboxDilate")
        self.sliderDilation = self.findChild(QSlider, "sliderDilation")

        self.btnOpen = self.findChild(QPushButton, "btnOpen")
        self.btnCopy = self.findChild(QPushButton, "btnCopy")

        self.init_hsv_tab_handler()
        self.loadHsvSpace()
        self.updateHSVPreview()

    def init_hough_tab_gui(self):
        self.operation_list = self.findChild(QListWidget, "algorithmList")
        for n in ['Hough Transform Line', 'Hough Transform Line (Parameterized)', 'Hough Transform Circle', 'Hough Transform Circle (Parameterized)']:
            self.operation_list.addItem(str(n))

        self.previewRawHough = self.findChild(QLabel, "previewRawHough")
        self.previewGrayHough = self.findChild(QLabel, "previewGrayHough")
        self.previewCannyHough = self.findChild(QLabel, "previewCannyHough")
        self.previewResultHough = self.findChild(QLabel, "previewResultHough")

        self.btnOpenHough = self.findChild(QPushButton, "btnOpenHough")
        self.btnStartHough = self.findChild(QPushButton, "btnStartHough")

        self.init_hough_tab_handler()

    def loadHsvSpace(self):
        self.imgHsvSpace = cv2.imread(os.path.join(os.path.dirname(__file__), "assets", "hsv_color.png"))

    def init_hsv_tab_handler(self):
        self.sliderH.valueChanged.connect(self.onHChanged)
        self.sliderS.valueChanged.connect(self.onSChanged)
        self.sliderV.valueChanged.connect(self.onVChanged)
        self.cboxSetMode.currentTextChanged.connect(self.onCBoxModeChanged)
        self.btnOpen.clicked.connect(self.onBtnOpenClicked)
        self.btnCopy.clicked.connect(self.updateMask)

        self.cboxDilate.stateChanged.connect(self.updateMask)
        self.cboxErode.stateChanged.connect(self.updateMask)
        self.sliderErotion.valueChanged.connect(self.onSliderErodeChanged)
        self.sliderDilation.valueChanged.connect(self.onSliderDilateChanged)

    def init_hough_tab_handler(self):
        self.btnOpenHough.clicked.connect(self.onBtnOpenClicked)
        self.btnStartHough.clicked.connect(self.startHoughTransform)

    def startHoughTransform(self):
        if self.imgRaw is not None:
            selectedItem = self.operation_list.currentItem()
            if(selectedItem):
                selectedItem = selectedItem.text()
                self.startOperation(selectedItem)
            else:
                self.dialog_critical("Tidak ada opsi dipilih !")
        else:
            self.dialog_critical("Tidak ada citra awal yang dapat diproses !")

    def startOperation(self, selectedOperasi):
        imageArray = self.imgRaw
        gray, edges = imageArray, imageArray
        if (selectedOperasi == 'Hough Transform Line'):
            dlg = OperasiCitraDialog(selectedOperasi)
            if dlg.exec_():
                value = dlg.GetValue()
                gray, edges, imageArray, lines = hough.hough_transform_line(imageArray,value[0],value[1],value[2], value[3], value[4])
                if lines is not None:
                    for index, line in enumerate(lines):
                        x1, y1, x2, y2 = line[0]
            else:
                return
        elif (selectedOperasi == 'Hough Transform Line (Parameterized)'):
            gray, edges, imageArray, lines = hough.hough_transform_line(imageArray)
            if lines is not None:
                for index, line in enumerate(lines):
                    x1, y1, x2, y2 = line[0]
        elif (selectedOperasi == 'Hough Transform Circle'):
            dlg = OperasiCitraDialog(selectedOperasi)
            if dlg.exec_():
                value = dlg.GetValue()
                gray, edges, imageArray = hough.hough_transform_circle(imageArray,value[0],value[1],value[2],value[3], value[4], value[5])
            else:
                return
        elif (selectedOperasi == 'Hough Transform Circle (Parameterized)'):
            gray, edges, imageArray = hough.hough_transform_circle(imageArray)

        _asQImage = QImage(
            gray.data, gray.shape[1], gray.shape[0], gray.shape[1] * 3,
            QtGui.QImage.Format_RGB888)
        _asQImage = _asQImage.rgbSwapped()
        self.previewGrayHough.setPixmap(QPixmap.fromImage(_asQImage).scaled(self.previewRawHough.size().width(), self.previewRawHough.size().height(),Qt.KeepAspectRatio))

        _asQImage = QImage(
            edges.data, edges.shape[1], edges.shape[0], edges.shape[1] * 3,
            QtGui.QImage.Format_RGB888)
        _asQImage = _asQImage.rgbSwapped()
        self.previewCannyHough.setPixmap(QPixmap.fromImage(_asQImage).scaled(self.previewRawHough.size().width(), self.previewRawHough.size().height(),Qt.KeepAspectRatio))

        _asQImage = QImage(
            imageArray.data, imageArray.shape[1], imageArray.shape[0], imageArray.shape[1] * 3,
            QtGui.QImage.Format_RGB888)
        _asQImage = _asQImage.rgbSwapped()
        self.previewResultHough.setPixmap(QPixmap.fromImage(_asQImage).scaled(self.previewRawHough.size().width(), self.previewRawHough.size().height(),Qt.KeepAspectRatio))

    # =========== Helper ===========
    def updatePreviewHsvSpace(self):
        if self.imgHsvSpace is None:
            return

        frame_HSV = cv2.cvtColor(self.imgHsvSpace, cv2.COLOR_BGR2HSV)
        lower_orange = np.array(self.lowerHSV)
        upper_orange = np.array(self.upperHSV)

        frame_threshold = cv2.inRange(
            frame_HSV, lower_orange, upper_orange)

        frame_threshold = cv2.bitwise_and(self.imgHsvSpace, self.imgHsvSpace, mask=frame_threshold)
        _asQImage = QImage(
            frame_threshold.data, frame_threshold.shape[1], frame_threshold.shape[0], frame_threshold.shape[1] * 3,
            QtGui.QImage.Format_RGB888)
        _asQImage = _asQImage.rgbSwapped()
        self.previewHsvSpace.setPixmap(QPixmap.fromImage(_asQImage).scaledToWidth(self.previewMask.size().width()))

    def updateHSVPreview(self):
        # Parameter : h, s, v
        # h dari nilai hue yang dipilih, s dan v set ke max value (255)
        prevH = generateSolidColorPixmap(
            200, 300, QColor.fromHsv(self.selectedHue, 255, 255))
        self.previewH.setPixmap(QPixmap.fromImage(prevH))

        # h dari nilai hue yang dipilih, s dari nilai saturation yang dipilih
        # v set ke max value (255)
        prevS = generateSolidColorPixmap(
            200, 300, QColor.fromHsv(self.selectedHue, self.selectedSaturation, 255))
        self.previewS.setPixmap(QPixmap.fromImage(prevS))

        # h dari nilai hue yang dipilih, s dari nilai saturation yang dipilih
        # v dari nilai v yang dipilih
        prevV = generateSolidColorPixmap(
            200, 300, QColor.fromHsv(self.selectedHue, self.selectedSaturation, self.selectedValue))
        self.previewV.setPixmap(QPixmap.fromImage(prevV))

        # Check dropdown pilihan mode UPPER atau LOWER
        if self.cboxSetMode.currentText() == "UPPER":
            self.upperHSV = (self.selectedHue // 2,
                             self.selectedSaturation, self.selectedValue)
            self.lblUpper.setText(
                f"H {self.upperHSV[0]}; S {self.upperHSV[1]}; V {self.upperHSV[2]}")
        elif self.cboxSetMode.currentText() == "LOWER":
            self.lowerHSV = (self.selectedHue // 2,
                             self.selectedSaturation, self.selectedValue)
            self.lblLower.setText(
                f"H {self.lowerHSV[0]}; S {self.lowerHSV[1]}; V {self.lowerHSV[2]}")

        self.updateMask()
        self.updatePreviewHsvSpace()

    def updateRawImg(self, img):
        # _dsize = (self.previewRaw.size().height(),
        #           self.previewRaw.size().width())

        self.imgRaw = img

        _imgAsQImg = QImage(
            self.imgRaw.data, self.imgRaw.shape[1], self.imgRaw.shape[0], QImage.Format_RGB888).rgbSwapped()

        # self.imgRaw = img.scaled(200,100, QtCore.KeepAspectRatio)
        # self.imgRaw = img.scaledToHeight(self.previewMask.size().height())
        self.previewRaw.setPixmap(QPixmap.fromImage(_imgAsQImg).scaledToWidth(self.previewRaw.size().width()))
        self.previewRawHough.setPixmap(QPixmap.fromImage(_imgAsQImg).scaledToWidth(self.previewRawHough.size().width()))

    def updateMask(self):
        if self.imgRaw is None:
            return

        frame_HSV = cv2.cvtColor(self.imgRaw, cv2.COLOR_BGR2HSV)
        lower_orange = np.array(self.lowerHSV)
        upper_orange = np.array(self.upperHSV)

        frame_threshold = cv2.inRange(
            frame_HSV, lower_orange, upper_orange)

        if self.cboxErode.isChecked():
            _kernel = self.sliderErotion.value()
            frame_threshold = cv2.erode(frame_threshold, np.ones((_kernel, _kernel), dtype=np.uint8))

        if self.cboxDilate.isChecked():
            _kernel = self.sliderDilation.value()
            frame_threshold = cv2.dilate(frame_threshold, np.ones((_kernel, _kernel), dtype=np.uint8))

        self.updateMaskedRaw(frame_threshold)
        frame_threshold = cv2.cvtColor(frame_threshold, cv2.COLOR_GRAY2RGB)

        _asQImage = QImage(
            frame_threshold.data, frame_threshold.shape[1], frame_threshold.shape[0], frame_threshold.shape[1] * 3,
            QtGui.QImage.Format_RGB888)
        _asQImage = _asQImage.rgbSwapped()
        self.previewMask.setPixmap(QPixmap.fromImage(_asQImage).scaledToHeight(self.previewMask.size().height()))

    def updateMaskedRaw(self, masking):
        if self.imgRaw is None:
            return

        frame_threshold = cv2.bitwise_and(self.imgRaw, self.imgRaw, mask=masking)
        _asQImage = QImage(
            frame_threshold.data, frame_threshold.shape[1], frame_threshold.shape[0], frame_threshold.shape[1] * 3,
            QtGui.QImage.Format_RGB888)
        _asQImage = _asQImage.rgbSwapped()
        self.previewMaskedRaw.setPixmap(
            QPixmap.fromImage(_asQImage).scaledToHeight(self.previewMaskedRaw.size().height()))

    # =========== EVENT HANDLER ===========

    def onCBoxModeChanged(self, text):
        if text == "UPPER":
            self.selectedHue = self.upperHSV[0] * 2
            self.selectedSaturation = self.upperHSV[1]
            self.selectedValue = self.upperHSV[2]
        elif text == "LOWER":
            self.selectedHue = self.lowerHSV[0] * 2
            self.selectedSaturation = self.lowerHSV[1]
            self.selectedValue = self.lowerHSV[2]

        self.sliderH.setValue(self.selectedHue)
        self.sliderS.setValue(self.selectedSaturation)
        self.sliderV.setValue(self.selectedValue)

        self.updateHSVPreview()

    def onHChanged(self):
        _v = self.selectedHue = self.sliderH.value()
        self.lblH.setText(str(f"QT5 ({_v}) | cv2 ({_v // 2})"))
        self.updateHSVPreview()

    def onSChanged(self):
        _v = self.selectedSaturation = self.sliderS.value()
        self.lblS.setText(str(_v))
        self.updateHSVPreview()

    def onVChanged(self):
        _v = self.selectedValue = self.sliderV.value()
        self.lblV.setText(str(_v))
        self.updateHSVPreview()

    def onSliderErodeChanged(self):
        self.cboxErode.setText(f"Erode {self.sliderErotion.value()}")
        self.updateMask()

    def onSliderDilateChanged(self):
        self.cboxDilate.setText(f"Dilate {self.sliderDilation.value()}")
        self.updateMask()

    def onBtnOpenClicked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Jpeg (*.jpeg);;BMP (*.bmp)", options=options)
        if not fileName:
            return
        # self.srcQimg = QImage(fileName=fileName, format=QImage.Format_RGB32)
        self.updateRawImg(cv2.imread(fileName))
        # with open(fileName, 'rb') as f:
        #     self.updateRawImg(QImage.fromData(f.read()))

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
