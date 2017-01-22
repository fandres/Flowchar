#! /usr/bin/python
#-*- coding: utf-8 -*-

from pyqtgraph.graphicsItems.GraphicsObject import GraphicsObject
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.functions as fn
from pyqtgraph.Point import Point

#from TerminalGraph  import TerminalGraphicsItem

#class ConnectionItem(QtGui.QGraphicsItem):
class ConnectionItem(GraphicsObject):
    
    def __init__(self, source, target=None):
        #QtGui.QGraphicsItem.__init__(self)
        GraphicsObject.__init__(self)
        self.setFlags(
            self.ItemIsSelectable | 
            self.ItemIsFocusable
        )
        self.source = source
        self.target = target
        self.length = 0
        self.hovered = False
        self.path = None
        self.shapePath = None
        self.style = {
            'shape': 'line',
            'color': (100, 100, 250),
            'width': 1.0,
            'hoverColor': (150, 150, 250),
            'hoverWidth': 1.0,
            'selectedColor': (200, 200, 0),
            'selectedWidth': 3.0,
            }
        #self.line = QtGui.QGraphicsLineItem(self)
        self.source.getViewBox().addItem(self)
        self.updateLine()
        self.setZValue(0)
        
    def close(self):
        if self.scene() is not None:
            #self.scene().removeItem(self.line)
            self.scene().removeItem(self)
        
    def setTarget(self, target):
        self.target = target
        self.updateLine()
    
    def setStyle(self, **kwds):
        self.style.update(kwds)
        if 'shape' in kwds:
            self.updateLine()
        else:
            self.update()
    
    def updateLine(self):
        start = Point(self.source.connectPoint())
        #if isinstance(self.target):
         #   stop = Point(self.target.connectPoint())
        #elif isinstance(self.target, QtCore.QPointF):
         #   stop = Point(self.target)
        #else:
        #    return
        self.prepareGeometryChange()
        
        #self.path = self.generatePath(start, stop)
        self.shapePath = None
        self.update()
        
    def generatePath(self, start, stop):
        path = QtGui.QPainterPath()
        path.moveTo(start)
        if self.style['shape'] == 'line':
            path.lineTo(stop)
        elif self.style['shape'] == 'cubic':
            path.cubicTo(Point(stop.x(), start.y()), Point(start.x(), stop.y()), Point(stop.x(), stop.y()))
        else:
            raise Exception('Invalid shape "%s"; options are "line" or "cubic"' % self.style['shape'])
        return path

    def keyPressEvent(self, ev):
        if ev.key() == QtCore.Qt.Key_Delete or ev.key() == QtCore.Qt.Key_Backspace:
            #if isinstance(self.target, TerminalGraphicsItem):
            self.source.disconnect(self.target)
            ev.accept()
        else:
            ev.ignore()
    
    def mousePressEvent(self, ev):
        ev.ignore()
        
    def mouseClickEvent(self, ev):
        if ev.button() == QtCore.Qt.LeftButton:
            ev.accept()
            sel = self.isSelected()
            self.setSelected(True)
            if not sel and self.isSelected():
                self.update()
                
    def hoverEvent(self, ev):
        if (not ev.isExit()) and ev.acceptClicks(QtCore.Qt.LeftButton):
            self.hovered = True
        else:
            self.hovered = False
        self.update()
            
            
    def boundingRect(self):
        return self.shape().boundingRect()
        ##return self.line.boundingRect()
        #px = self.pixelWidth()
        #return QtCore.QRectF(-5*px, 0, 10*px, self.length)
    def viewRangeChanged(self):
        self.shapePath = None
        self.prepareGeometryChange()
        
    def shape(self):
        if self.shapePath is None:
            if self.path is None:
                return QtGui.QPainterPath()
            stroker = QtGui.QPainterPathStroker()
            px = self.pixelWidth()
            stroker.setWidth(px*8)
            self.shapePath = stroker.createStroke(self.path)
        return self.shapePath
        
    def paint(self, p, *args):
        if self.isSelected():
            p.setPen(fn.mkPen(self.style['selectedColor'], width=self.style['selectedWidth']))
        else:
            if self.hovered:
                p.setPen(fn.mkPen(self.style['hoverColor'], width=self.style['hoverWidth']))
            else:
                p.setPen(fn.mkPen(self.style['color'], width=self.style['width']))
                
        #p.drawLine(0, 0, 0, self.length)
        
        p.drawPath(self.path)
