#! /usr/bin/python
#-*- coding: utf-8 -*-

#from PyQt5 import QtGui,QtCore
from pyqtgraph.Qt import QtCore, QtGui, USE_PYSIDE
from pyqtgraph.widgets.GraphicsView import GraphicsView
from Formblock import *

from grid import GridItem

from basic_form import *

class flowchart(QtGui.QMainWindow):
    def __init__(self):
        super(flowchart, self).__init__()
        self._zone=GraphicsView()
        self._zone.setBackground(QtGui.QColor(0,0,0,0))
        self._scene=self._zone.scene()
        
        self.grid=GridItem([255,255,255], [255,255,255])
        self.grid.set_color_line(25,25, 25)
        self.grid.set_color_txt(25,25, 25)
        self._scene.addItem(self.grid)
        
        a=rectangulo("car")
        a.moveBy(100, 200)
        a.set_size(8, 8)
        a.pos_txer()
        self._scene.addItem(a)
        
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self._zone)

        self.widget = QtGui.QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("FlowChart")
        
        self.mm1=oneinceroout("cero1")
        self.mm1.block.moveBy(10,200)
        
        self.mm2=oneinceroout("cero")
        self.mm2.block.moveBy(100,200)
        
        self.mm=oneinceroout("cero3")
        self.mm.block.moveBy(30,200)
        
        self.mm4=oneinceroout("cero4")
        self.mm4.block.moveBy(30,300)
        
        #self._scene.addItem(self.mm1.graphicsItem())
        #self._scene.addItem(self.mm2.graphicsItem())
        #self._scene.addItem(self.mm.graphicsItem())
        #self._scene.addItem(self.mm4.graphicsItem())
        
