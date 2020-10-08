import random

from abc import ABCMeta, abstractmethod, 
class Instrumento(metaclass=ABCMeta):
    @abstractmethod
    def afinar(self):
        pass

    @abstractmethod
    def tocar(self):
        pass

    @abstractmethod
    def tocando(cadena, nota):
        pass

class Instrumento:
    def _init_(self):
        pass
    def afinar(self):
        pass

    def tocar(self):
        pass

    def tocando(cadena, nota):
        pass


class Bajo(Instrumento):
    def _init_(self):
        pass
    def afinar(self):
        print('afinando bajo')
    def tocar(self):
        print('tocando bajo')
    def tocando(cadena, nota):
        print('tocando bajo en '+nota)

class Guitarra(Instrumento):
    def _init_(self):
        pass
    def afinar(self):
        print('afinando guitarra')
    def tocar(self):
        print('tocando guitarra')
    def tocando(cadena, nota):
        print('tocando guitarra en '+nota)

class Violin(Instrumento):
    def _init_(self):
        pass
    def afinar(self):
        print('afinando violin')
    def tocar(self):
        print('tocando violin')
    def tocando(cadena, nota):
        print('tocando violin en '+nota)

class Persona:
    def _init_(self,Persona):
        pass    
    def setNombre(self,nombre):
        self._nombre_ = nombre
    def get_nombre(self):
        return self._nombre_
    def presentar(self,msg):
        print("Hola mi nombre es "+self.nombre)
    
class Musico(Persona):
    def _init_(self):
        pass
    def tocar(Instrumento):
        i = Instrumento
        i.afinar()
        i.tocar()
        i.tocando()

class banda:
    def _init_(self):
        pass
    lista=[]
    lista[Musico]

    def agregar_musico(self, nombre):
        m = Musico()
        m.setNombre(nombre)
        lista= m.get_nombre()
    
    def generarInstrumento():
        rn = random.randint(0,3)
        sel = rn
        if sel == 1:
            return Guitarra()
        if sel == 2:
            return Bajo()
        else:
            return Violin()
    
    def presentar_banda():
        musico = Musico
        for(musico : lista[Musico]):
            musico.presentar()
            musico.tocar(generarInstrumento())









i = Instrumento()
rn = random.randint(0,3)
sel = rn
if sel == 1:
    i = Guitarra()
if sel == 2:
    i = Bajo()
else:
    i = Violin()

i.afinar()
i.tocar()
i.tocando('DO')


