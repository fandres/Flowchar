#! /usr/bin/python
#-*- coding: utf-8 -*-
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph.graphicsItems.GraphicsObject import GraphicsObject
import pyqtgraph.functions as fn

class blll(GraphicsObject):
    
    def __init__(self, name):
        
        GraphicsObject.__init__(self)
         
        self.pen = fn.mkPen(200,0,100, width=2)
        self.selectPen = fn.mkPen(20,20,200,width=4)
        self.brush = fn.mkBrush(200, 20, 20, 150)
        self.hoverBrush = fn.mkBrush(200, 200, 200, 200)
        self.selectBrush = fn.mkBrush(200, 200, 255, 200)
        self.hovered = False
        self.nn=name
        
        self.bounds = QtCore.QRectF(0, 0, 100, 100)
        
        
    def boundingRect(self):
        return self.bounds.adjusted(-5, -5, 5, 5)
        
    def paint(self, p, *args):
        
        p.setPen(self.pen)
        if self.isSelected():
            p.setPen(self.selectPen)
            p.setBrush(self.selectBrush)
        else:
            p.setPen(self.pen)
            if self.hovered:
                p.setBrush(self.hoverBrush)
            else:
                p.setBrush(self.brush)
                
        p.drawRect(self.bounds)
        
        
    def hoverEvent(self, ev):
        if not ev.isExit() and ev.acceptClicks(QtCore.Qt.LeftButton):
            ev.acceptDrags(QtCore.Qt.LeftButton)
            self.hovered = True
            print(self.nn)
        else:
            self.hovered = False
        self.update()
        
        
        
