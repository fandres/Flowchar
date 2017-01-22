#! /usr/bin/python
#-*- coding: utf-8 -*-
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph.graphicsItems.GraphicsObject import GraphicsObject
import pyqtgraph.functions as fn

class rectangulo(GraphicsObject):
    
    def __init__(self,  name):
        
        GraphicsObject.__init__(self)
         
        self.pen = fn.mkPen(200,0,100, width=2)
        self.selectPen = fn.mkPen(2,2,2,width=1)
        self.brush = fn.mkBrush(2, 20, 20, 150)
        self.hoverBrush = fn.mkBrush(2, 2, 2, 2)
        self.selectBrush = fn.mkBrush(2, 2, 2, 2)
        
        #self.sup=s
        self.hovered = False
        self.name=name
        
        self.bounds = QtCore.QRectF(0, 0, 100, 100)
        
        self.nameItem = QtGui.QGraphicsTextItem(self.name, self)
        self.nameItem.setDefaultTextColor(QtGui.QColor(50, 50, 50))
        self.nameItem.moveBy(self.bounds.width()/2. - self.nameItem.boundingRect().width()/2., 0)
        self.nameItem.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        
        self.nameItem.focusOutEvent = self.labelFocusOut
        self.nameItem.keyPressEvent = self.labelKeyPress
        
    def pos_text(self, x, y):
        self.nameItem.moveBy(x, y)
        
    def pos_txer(self):
        self.nameItem.moveBy(-3.7*self.bounds.width(), -1*self.bounds.height())
        
    def pos_txbox(self):
        self.nameItem.moveBy(self.bounds.width()/2. - self.nameItem.boundingRect().width()/2., 0)
        
    def set_pen(self, r, g, b, w=2):
        self.pen = fn.mkPen(r, g, b, width=w)
        self.update()
        
    def set_select_pen(self, r, g, b, w):
        self.selectPen = fn.mkPen(r, g, b,width=w)
        
    
    def set_brush(self, r, g, b, w):
        self.brush = fn.mkBrush(r, g, b, w)
        self.update()
        
    def set_hoverbrush(self, r, g, b, w):
        self.hoverBrush = fn.mkBrush(r, g, b, w)
    
    def set_selectbrush(self, r, g, b, w):
        self.selectBrush = fn.mkBrush(r, g, b, w)
    
    def labelFocusOut(self, ev):
        QtGui.QGraphicsTextItem.focusOutEvent(self.nameItem, ev)
        self.labelChanged()
        
    def labelKeyPress(self, ev):
        if ev.key() == QtCore.Qt.Key_Enter or ev.key() == QtCore.Qt.Key_Return:
            self.labelChanged()
        else:
            QtGui.QGraphicsTextItem.keyPressEvent(self.nameItem, ev)
            
    def labelChanged(self):
        newName = str(self.nameItem.toPlainText())
        #if newName != self.name:
        #    self.node.rename(newName)
            
        ### re-center the label
        bounds = self.boundingRect()
        #self.nameItem.setPos(bounds.width()/2. - self.nameItem.boundingRect().width()/2., 0)
        
        
    def set_width(self, a):
        self.bounds.setWidth(a)
        
    def set_height(self, a):
        self.bounds.setHeight(a)

    def set_size(self, w, h):
        self.bounds.setWidth(w)
        self.bounds.setHeight(h)        
        
        
    def boundingRect(self):
        return self.bounds.adjusted(0,0, 5, 5)
        
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
        else:
            self.hovered = False
        self.update()
        
    def mousePressEvent(self, ev):
        ev.ignore()
        
    def mouseClickEvent(self, ev):
        if int(ev.button()) == int(QtCore.Qt.LeftButton):
            ev.accept()
            #print "    ev.button: left"
            sel = self.isSelected()
            #ret = QtGui.QGraphicsItem.mousePressEvent(self, ev)
            self.setSelected(True)
            if not sel and self.isSelected():
                #self.setBrush(QtGui.QBrush(QtGui.QColor(200, 200, 255)))
                #self.emit(QtCore.SIGNAL('selected'))
                #self.scene().selectionChanged.emit() ## for some reason this doesn't seem to be happening automatically
                self.update()
            #return ret
        
        elif int(ev.button()) == int(QtCore.Qt.RightButton):
            #print "    ev.button: right"
            ev.accept()
            #pos = ev.screenPos()
            self.raiseContextMenu(ev)
            #self.menu.popup(QtCore.QPoint(pos.x(), pos.y()))
            
#    def itemChange(self, change, val):
#        if change == self.ItemPositionHasChanged:
#            for k, t in self.terminals.items():
#                t[1].nodeMoved()
#        return GraphicsObject.itemChange(self, change, val)
        
    def mouseDragEvent(self, ev):
        #print "Node.mouseDrag"
        if ev.button() == QtCore.Qt.LeftButton:
            ev.accept()
            self.setPos(self.pos()+self.mapToParent(ev.pos())-self.mapToParent(ev.lastPos()))
        
        
       
class circulo(GraphicsObject):
    
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
        
        
class triangulo(GraphicsObject):
    
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
        
        
        
        
