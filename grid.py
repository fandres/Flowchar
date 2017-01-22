#! /usr/bin/python
#-*- coding: utf-8 -*-

"""
Copyright (c) 2012  University of North Carolina at Chapel Hill
Luke Campagnola    ('luke.campagnola@%s.com' % 'gmail')

The MIT License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""



from pyqtgraph.graphicsItems.UIGraphicsItem import *
import numpy as np
from pyqtgraph.Point import Point


from pyqtgraph.Qt import QtCore, QtGui
#from pyqtgraph.graphicsItems.GraphicsObject import GraphicsObject
import pyqtgraph.functions as fn

__all__ = ['GridItem']
class GridItem(UIGraphicsItem):
    """
    **Bases:** :class:`UIGraphicsItem <pyqtgraph.UIGraphicsItem>`
    
    Displays a rectangular grid of lines indicating major divisions within a coordinate system.
    Automatically determines what divisions to use.
    """
    
    def __init__(self, line, txt):
        UIGraphicsItem.__init__(self)
        #QtGui.QGraphicsItem.__init__(self, *args)
        #self.setFlag(QtGui.QGraphicsItem.ItemClipsToShape)
        #self.setCacheMode(QtGui.QGraphicsItem.DeviceCoordinateCache)
       
        self.r_l=line[0]
        self.g_l=line[1]
        self.b_l=line[2]
        
        self.r_t=txt[0]
        self.g_t=txt[1]
        self.b_t=txt[2]
        self.picture = None
       
        
    def set_color_line(self, r, g, b):
        self.r_l=r
        self.g_l=g
        self.b_l=b
        
    def set_color_txt(self, r, g, b):
        self.r_t=r
        self.g_t=g
        self.b_t=b
        
        
    def viewRangeChanged(self):
        UIGraphicsItem.viewRangeChanged(self)
        self.picture = None
        #UIGraphicsItem.viewRangeChanged(self)
        #self.update()
        
    def paint(self, p, opt, widget):
        #p.setPen(QtGui.QPen(QtGui.QColor(100, 100, 100)))
        #p.drawRect(self.boundingRect())
        #UIGraphicsItem.paint(self, p, opt, widget)
        ### draw picture
        if self.picture is None:
            #print "no pic, draw.."
            self.generatePicture()
        p.drawPicture(QtCore.QPointF(0, 0), self.picture)
        #p.setPen(QtGui.QPen(QtGui.QColor(255,0,0)))
        #p.drawLine(0, -100, 0, 100)
        #p.drawLine(-100, 0, 100, 0)
        #print "drawing Grid."
        
        
    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter()
        p.begin(self.picture)
        
        dt = fn.invertQTransform(self.viewTransform())
        vr = self.getViewWidget().rect()
        unit = self.pixelWidth(), self.pixelHeight()
        dim = [vr.width(), vr.height()]
        lvr = self.boundingRect()
        ul = np.array([lvr.left(), lvr.top()])
        br = np.array([lvr.right(), lvr.bottom()])
        
        texts = []
        
        if ul[1] > br[1]:
            x = ul[1]
            ul[1] = br[1]
            br[1] = x
        for i in [2,1,0]:   ## Draw three different scales of grid
            dist = br-ul
            nlTarget = 10.**i
            d = 10. ** np.floor(np.log10(abs(dist/nlTarget))+0.5)
            ul1 = np.floor(ul / d) * d
            br1 = np.ceil(br / d) * d
            dist = br1-ul1
            nl = (dist / d) + 0.5
            #print "level", i
            #print "  dim", dim
            #print "  dist", dist
            #print "  d", d
            #print "  nl", nl
            for ax in range(0,2):  ## Draw grid for both axes
                ppl = dim[ax] / nl[ax]
                c = np.clip(3.*(ppl-3), 0., 30.)
                linePen = QtGui.QPen(QtGui.QColor(self.r_l,self.g_l,self.b_l, c)) 
                textPen = QtGui.QPen(QtGui.QColor(self.r_t,self.g_t, self.b_t,  c*2)) 
                #linePen.setCosmetic(True)
                #linePen.setWidth(1)
                bx = (ax+1) % 2
                for x in range(0, int(nl[ax])):
                    linePen.setCosmetic(False)
                    if ax == 0:
                        linePen.setWidthF(self.pixelWidth())
                        #print "ax 0 height", self.pixelHeight()
                    else:
                        linePen.setWidthF(self.pixelHeight())
                        #print "ax 1 width", self.pixelWidth()
                    p.setPen(linePen)
                    p1 = np.array([0.,0.])
                    p2 = np.array([0.,0.])
                    p1[ax] = ul1[ax] + x * d[ax]
                    p2[ax] = p1[ax]
                    p1[bx] = ul[bx]
                    p2[bx] = br[bx]
                    ## don't draw lines that are out of bounds.
                    if p1[ax] < min(ul[ax], br[ax]) or p1[ax] > max(ul[ax], br[ax]):
                        continue
                    p.drawLine(QtCore.QPointF(p1[0], p1[1]), QtCore.QPointF(p2[0], p2[1]))
                    if i < 2:
                        p.setPen(textPen)
                        if ax == 0:
                            x = p1[0] + unit[0]
                            y = ul[1] + unit[1] * 8.
                        else:
                            x = ul[0] + unit[0]*3
                            y = p1[1] + unit[1]
                        texts.append((QtCore.QPointF(x, y), "%g"%p1[ax]))
        tr = self.deviceTransform()
        #tr.scale(1.5, 1.5)
        p.setWorldTransform(fn.invertQTransform(tr))
        for t in texts:
            x = tr.map(t[0]) + Point(0.5, 0.5)
            p.drawText(x, t[1])
        p.end()
