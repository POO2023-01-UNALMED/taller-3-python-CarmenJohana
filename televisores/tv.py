class TV:

    _numTV=0

    def __init__(self, marca, estado):

        self._marca=marca
        self._estado=estado
        self._precio=500
        self._volumen=1
        self._canal=1
        TV._numTV+=1

    def setMarca(self, marca):
        self._marca=marca

    def getMarca(self):
        return self._marca

    def setControl(self, control):
        self._control=control

    def getControl(self):
        return self._control

    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self._precio=precio

    def setVolumen(self, volumen):
        if self._estado==True and volumen<=7 and volumen>=0:
            self._volumen=volumen

    def getVolumen(self):
        return self._volumen

    def setCanal(self, canal):

        if self._estado==True and canal<=120 and canal>=1:
            self._canal=canal

    def getCanal(self):
        return self._canal

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV=numTV

    def turnOn(self):
        self._estado=True

    def turnOff(self):
        self._estado=False

    def setEstado(self, estado):
        self._estado=estado

    def getEstado(self):
        return self._estado

    def canalDown(self):
        if self._estado==True and self._canal>1:
            self._canal-=1

    def canalUp(self):
        if self._estado==True and self._canal<120:
            self._canal+=1

    def volumenUp(self):
        if self._estado==True and self._volumen<7:
            self._volumen+=1

    def volumenDown(self):
        if self._estado==True and self._volumen>0:
            self._volumen-=1
