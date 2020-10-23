#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import urllib
import urllib.request
from urllib.request import urlopen

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QWidget, QLabel, QGridLayout, QApplication, QPushButton, QMessageBox, QVBoxLayout)
from bs4 import BeautifulSoup
from gevent import os


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.url = "https://sun9-65.userapi.com/c858216/v858216128/2224e1/G2PVPHEk8wY.jpg" #Ссылка на картинку
        self.url_txt = "https://raw.githubusercontent.com/DrawManG/TextQt5/master/main.py" #Ссылка на текст из гита рава
        grid = QGridLayout()
        self.lab = QVBoxLayout()
        self.setLayout(self.lab)
        self.but1 = QPushButton('Parsing')
        self.but1.clicked.connect(self.but1click)
        self.ParsImage = QLabel()
        self.txtParse = QLabel()

        self.lab.addWidget(self.but1)
        self.lab.addWidget(self.ParsImage)
        self.lab.addWidget(self.txtParse)
        #$self.lab.
        grid.setSpacing(10)
        self.setLayout(grid)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Parser')

        self.show()


    def but1click(self): # нажатие на кнопку
        self.text()
        self.picture()

    def text(self): #функция по парсингу текста
        con = urlopen(self.url_txt).read()
        soup = BeautifulSoup(con, 'html.parser')
        texts = soup.get_text()
        self.txtParse.setText(texts)
    def picture(self): #функция по парсингу картинки
        self.name_image_1 = 'img.png'
        img = urllib.request.urlopen(self.url).read()
        out = open(self.name_image_1, "wb")
        out.write(img)
        self.pixmap = QPixmap(self.name_image_1)
        self.ParsImage.setPixmap(self.pixmap)
        out.close()
        os.remove(self.name_image_1)

class Qmessa(QMessageBox): # класс сообщений
    def __init__(self, a):
        super().__init__()
        msg = QMessageBox()
        msg.setWindowTitle("Info")
        msg.setText(a)
        result = msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())