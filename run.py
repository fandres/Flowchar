
#! /usr/bin/python
#-*- coding: utf-8 -*-


#from metodos import *
#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
#from PyQt5 import QtGui
from prueva import flowchart
from pyqtgraph.Qt import QtGui, QtCore
#from PyQt5.QtWidgets import QApplication,QGraphicsView
#from GraphicsView import GraphicsView

import sys

def main(args):
    app = QtGui.QApplication([])
    frame=flowchart()
    #GraphicsView()#MainWindow()
    frame.setGeometry(100, 100, 600, 800)
    #frame.setWindowTitle("Flowchar")
    frame.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main(sys.argv)

