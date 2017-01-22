from Block import Block

class oneinoneout(Block):
    """Forma generica para un bloque de una entrada una salida"""
    def __init__(self,name):

        #super(oneinoneout, self).__init__()
        Block.__init__(self,name,terminals={
            'In': {'io': 'in'},
            'Out': {'io': 'out', 'bypass': 'In'}
        })
        self.block=self.graphicsItem()
        self.block.setbounds(100,200)
        self.block.setBrush(200,100,50,40)
        self.block.updateTerminals()

class oneinceroout(Block):
    """Forma de bloque de una entrada cero salidas"""
    def __init__(self,name):
        #super(oneinceroout, self).__init__()
        Block.__init__(self,name,terminals={
            'In': {'io': 'in'}})
        self.block=self.graphicsItem()
        self.block.setbounds(80,80)
        self.block.updateTerminals()


class twoinoneout(Block):
    """Forma de Bloque de dos entradas dos salidas"""
    def __init__(self,name):
        #super(twoinoneout, self).__init__()
        Block.__init__(self,name,terminals={
            'A': {'io': 'in'},
            'B': {'io': 'in'},
            'Out': {'io': 'out', 'bypass': 'In'}
        })
        self.block=self.graphicsItem()
        self.block.setbounds(120,400)
        self.block.updateTerminals()

class threeinoneout(Block):
    """Forma de Bloque de tres entradas dos salidas"""
    def __init__(self,name):
        #super(twoinoneout, self).__init__()
        Block.__init__(self,name,terminals={
            'A': {'io': 'in'},
            'B': {'io': 'in'},
            'C': {'io': 'in'},
            'Out': {'io': 'out', 'bypass': 'In'}
        })
        self.block=self.graphicsItem()
        self.block.setbounds(120,500)
        self.block.updateTerminals()

class fourinoneout(Block):
    """Forma de Bloque de cuatro entradas dos salidas"""
    def __init__(self,name):
        #super(twoinoneout, self).__init__()
        Block.__init__(self,name,terminals={
            'A': {'io': 'in'},
            'B': {'io': 'in'},
            'C': {'io': 'in'},
            'D': {'io': 'in'},
            'Out': {'io': 'out', 'bypass': 'In'}
        })
        self.block=self.graphicsItem()
        self.block.setbounds(120,500)
        #self.block.labelChanged()
        self.block.updateTerminals()

class twointwoout(Block):
    """Forma de Bloque de cuatro entradas dos salidas"""
    def __init__(self,name):
        #super(twoinoneout, self).__init__()
        Block.__init__(self,name,terminals={
            'A': {'io': 'in'},
            'B': {'io': 'in'},
            'C': {'io': 'out', 'bypass': 'In'},
            'D': {'io': 'out', 'bypass': 'In'}
        })
        self.block=self.graphicsItem()
        self.block.setbounds(120,400)
        self.block.updateTerminals()
