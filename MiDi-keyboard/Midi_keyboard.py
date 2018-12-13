import sys
import playsound
import time
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton, QColorDialog
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from pygame import mixer
mixer.init()
 
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.d = {'1': '.\\Note\'s_Sound\\nota_1.wav',
                  '2': '.\\Note\'s_Sound\\nota_2.wav',
                  '3': '.\\Note\'s_Sound\\nota_3.wav',
                  '4': '.\\Note\'s_Sound\\nota_4.wav',
                  '5': '.\\Note\'s_Sound\\nota_5.wav',
                  '6': '.\\Note\'s_Sound\\nota_6.wav',
                  '7': '.\\Note\'s_Sound\\nota_7.wav',
                  '8': '.\\Note\'s_Sound\\nota_8.wav',
                  '9': '.\\Note\'s_Sound\\nota_9.wav',
                  '10': '.\\Note\'s_Sound\\nota_10.wav',
                  '11': '.\\Note\'s_Sound\\nota_11.wav',
                  '12': '.\\Note\'s_Sound\\nota_12.wav',
                  '13': '.\\Note\'s_Sound\\nota_13.wav',
                  '14': '.\\Note\'s_Sound\\nota_14.wav',
                  '15': '.\\Note\'s_Sound\\nota_15.wav',
                  '16': '.\\Note\'s_Sound\\nota_16.wav',
                  '17': '.\\Note\'s_Sound\\nota_17.wav',}
        self.buttons = []
        self.musicc = []
        self.booll = False
        self.initUI()
 
    def initUI(self):
        self.setGeometry(330, 250, 642, 417)
        self.setWindowTitle('MIDI-Keyboard')
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('icon.png')) 

        oImage = QImage("image.jpg")
        sImage = oImage.scaled(QSize(642, 417))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("You can play:")
        self.label.setGeometry(QtCore.QRect(220, 10, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 61, 171))
        self.pushButton.setText("1")
        self.pushButton.setStyleSheet("background-color: {}".format('#ffffff'))
        self.pushButton.clicked.connect(self.playmusic)

        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 60, 61, 171))
        self.pushButton_2.setText("2")
        self.pushButton_2.setStyleSheet("background-color: {}".format('#ffffff'))
        self.pushButton_2.clicked.connect(self.playmusic)
        
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 60, 61, 171))
        self.pushButton_3.setText("3")
        self.pushButton_3.setStyleSheet("background-color: {}".format('#ffffff'))
        self.pushButton_3.clicked.connect(self.playmusic)

        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 60, 61, 171))
        self.pushButton_4.setText("4")
        self.pushButton_4.setStyleSheet("background-color: {}".format('#ffffff'))
        self.pushButton_4.clicked.connect(self.playmusic)

        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 60, 61, 171))
        self.pushButton_5.setText("5")
        self.pushButton_5.setStyleSheet("background-color: {}".format('#ffffff'))
        self.pushButton_5.clicked.connect(self.playmusic)

        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(320, 60, 61, 171))
        self.pushButton_6.setText("6")
        self.pushButton_6.setStyleSheet("background-color: {}".format('#ffffff'))
        self.pushButton_6.clicked.connect(self.playmusic)

        self.pushButton_7 = QtWidgets.QPushButton(self)
        self.pushButton_7.setGeometry(QtCore.QRect(380, 60, 61, 171))
        self.pushButton_7.setText("7")
        self.pushButton_7.setStyleSheet("background-color: {}".format('#ffffff'))
        self.pushButton_7.clicked.connect(self.playmusic)

        self.pushButton_8 = QtWidgets.QPushButton(self)
        self.pushButton_8.setGeometry(QtCore.QRect(440, 60, 61, 171))
        self.pushButton_8.setText("8")
        self.pushButton_8.setStyleSheet("background-color: {}".format('#ffffff'))
        self.pushButton_8.clicked.connect(self.playmusic)

        self.pushButton_9 = QtWidgets.QPushButton(self)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 60, 61, 171))
        self.pushButton_9.setText("9")
        self.pushButton_9.setStyleSheet("background-color: {}".format('#ffffff'))
        self.pushButton_9.clicked.connect(self.playmusic)

        self.pushButton_10 = QtWidgets.QPushButton(self)
        self.pushButton_10.setGeometry(QtCore.QRect(560, 60, 61, 171))
        self.pushButton_10.setText("10")
        self.pushButton_10.setStyleSheet("background-color: {}".format('#ffffff'))
        self.pushButton_10.clicked.connect(self.playmusic)

        self.pushButton_11 = QtWidgets.QPushButton(self)
        self.pushButton_11.setGeometry(QtCore.QRect(70, 60, 21, 111))
        self.pushButton_11.setText("11")
        self.pushButton_11.setStyleSheet("background-color: {}".format('#000000'))
        self.pushButton_11.clicked.connect(self.playmusic)

        self.pushButton_12 = QtWidgets.QPushButton(self)
        self.pushButton_12.setGeometry(QtCore.QRect(130, 60, 21, 111))
        self.pushButton_12.setText("12")
        self.pushButton_12.setStyleSheet("background-color: {}".format('#000000'))
        self.pushButton_12.clicked.connect(self.playmusic)

        self.pushButton_13 = QtWidgets.QPushButton(self)
        self.pushButton_13.setGeometry(QtCore.QRect(250, 60, 21, 111))
        self.pushButton_13.setText("13")
        self.pushButton_13.setStyleSheet("background-color: {}".format('#000000'))
        self.pushButton_13.clicked.connect(self.playmusic)

        self.pushButton_14 = QtWidgets.QPushButton(self)
        self.pushButton_14.setGeometry(QtCore.QRect(310, 60, 21, 111))
        self.pushButton_14.setText("14")
        self.pushButton_14.setStyleSheet("background-color: {}".format('#000000'))
        self.pushButton_14.clicked.connect(self.playmusic)

        self.pushButton_15 = QtWidgets.QPushButton(self)
        self.pushButton_15.setGeometry(QtCore.QRect(370, 60, 21, 111))
        self.pushButton_15.setText("15")
        self.pushButton_15.setStyleSheet("background-color: {}".format('#000000'))
        self.pushButton_15.clicked.connect(self.playmusic)

        self.pushButton_16 = QtWidgets.QPushButton(self)
        self.pushButton_16.setGeometry(QtCore.QRect(490, 60, 21, 111))
        self.pushButton_16.setText("16")
        self.pushButton_16.setStyleSheet("background-color: {}".format('#000000'))
        self.pushButton_16.clicked.connect(self.playmusic)

        self.pushButton_17 = QtWidgets.QPushButton(self)
        self.pushButton_17.setGeometry(QtCore.QRect(550, 60, 21, 111))
        self.pushButton_17.setText("17")
        self.pushButton_17.setStyleSheet("background-color: {}".format('#000000'))
        self.pushButton_17.clicked.connect(self.playmusic)

        self.Start_button = QtWidgets.QPushButton(self)
        self.Start_button.setGeometry(QtCore.QRect(20, 312, 121, 31))
        self.Start_button.setText("Start recording")
        self.Start_button.setStyleSheet("background-color: {}".format('#979191'))
        self.Start_button.clicked.connect(self.rec)

        self.Stop_button = QtWidgets.QPushButton(self)
        self.Stop_button.setGeometry(QtCore.QRect(150, 312, 121, 31))
        self.Stop_button.setText("Stop recording")
        self.Stop_button.setStyleSheet("background-color: {}".format('#979191'))
        self.Stop_button.clicked.connect(self.rec)
        self.Stop_button.setEnabled(False)

        self.Play_button = QtWidgets.QPushButton(self)
        self.Play_button.setGeometry(QtCore.QRect(370, 312, 251, 31))
        self.Play_button.setText("Рlay the last recording")
        self.Play_button.setStyleSheet("background-color: {}".format('#979191'))
        self.Play_button.clicked.connect(self.play_rec)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setText(' MIDI-Keyboard by Danil Alekseev')
        self.label_2.setGeometry(QtCore.QRect(460, 380, 171, 16))
        self.label_2.setStyleSheet("background-color: {}".format('#ffffff'))
        self.label_2.setObjectName("label_2")

        self.buttons = [self.pushButton, self.pushButton_2, self.pushButton_3,
                        self.pushButton_4, self.pushButton_5, self.pushButton_6,
                        self.pushButton_7, self.pushButton_8, self.pushButton_9,
                        self.pushButton_10, self.pushButton_11, self.pushButton_12,
                        self.pushButton_13, self.pushButton_14, self.pushButton_15,
                        self.pushButton_16, self.pushButton_17]

        self.show()

    def playmusic(self):
        if self.booll == True:
            self.musicc.append(self.sender().text())
        mixer.music.stop()
        mixer.music.load(u'' + self.d[self.sender().text()])
        mixer.music.play()

    def rec(self):
        n = self.sender().text()
        if n == "Start recording":
            self.booll = True
            self.label.setText('Recording...')
            self.Play_button.setEnabled(False)
            self.Stop_button.setEnabled(True)
            self.Start_button.setEnabled(False)
            self.musicc = []

        elif n == "Stop recording":
            self.booll = False
            self.label.setText('Alright, play:')
            self.Play_button.setEnabled(True)
            self.Start_button.setEnabled(True)
            self.Stop_button.setEnabled(False)

    def play_rec(self):
        if self.musicc != []:
            for i in self.musicc:
                playsound.playsound(self.d[i], True)
            self.Stop_button.setEnabled(False)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
