from abc import ABC, abstractmethod
import math as m

def     dist(x1 :float, y1 :float, x2 :float, y2 :float) -> float:
    return (m.sqrt(((x2-x1)**2)+((y2-y1)**2)))



'''
CLASSE ABSTRAITE DEPLACEMENT & TYPES DE DEPLACEMENT
'''
#####################################################################
class   Deplacement(ABC):
    def __init__(self, x = 0.0, y = 0.0, z = 0.0, zone = ""):
        self._x = x
        self._y = y
        self._z = z
        self._zone = zone
    
    @property
    @abstractmethod
    def x(self):
        return self._x

    @property
    @abstractmethod
    def y(self):
        return self._y
    
    @property
    @abstractmethod
    def z(self):
        return self._z
    
    @property
    @abstractmethod
    def zone(self):
        return self._zone

    @abstractmethod
    def move_to(self, x :float, y :float, z :float, zone :str):
        pass
#####################################################################
##############

class   Volant(Deplacement):

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def zone(self):
        return self._zone

    def move_to(self, x, y, z, zone):
        try:
            assert (z > 0.0)
        except:
            raise(ValueError("Flying underground!\n"))
        return (f"se déplace vers {x}, {y}, {z} en volant")
##############

class   Courant(Deplacement):

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def zone(self):
        return self._zone

    def move_to(self, x, y, z, zone):
        try:
            assert (z == 0.0 and zone == 'terre')
        except:
            raise(ValueError("Running in the sky!\n"))
        return (f"se déplace vers {x}, {y} en courant")
##############

class   Marchant(Deplacement):

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def zone(self):
        return self._zone

    def move_to(self, x, y, z, zone):
        try:
            assert (z == 0.0 and zone == 'terre')
        except:
            raise(ValueError("Walking in the sky!\n"))
        return (f"se déplace vers {x}, {y} en marchant")
##############

class   Roulant(Deplacement):

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def zone(self):
        return self._zone

    def move_to(self, x, y, z, zone):
        try:
            assert (z == 0.0 and zone == 'terre')
        except:
            raise(ValueError("Rolling in the sky!\n"))
        return (f"se déplace vers {x}, {y} en roulant")
##############

class   Flottant(Deplacement):

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def zone(self):
        return self._zone

    def move_to(self, x, y, z, zone):
        try:
            assert (z == 0.0 and zone == 'mer')
        except:
            raise(ValueError("Flotte dans la boue!\n"))
        return (f"se déplace vers {x}, {y} en flottant")
##############

class   Nageant(Deplacement):
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def zone(self):
        return self._zone

    def move_to(self, x, y, z, zone):
        try:
            assert (z < 0.0 and zone == 'mer')
        except:
            raise(ValueError("Swimming againt gravity!\n"))
        return (f"se déplace vers {x}, {y}, {z} en nageant")
##############




'''
CLASSES D'ANIMAUX
'''
#####################################################################
class   Animal:                                
                                               
    def __init__(self, patte= 4, queue= False):
        self.patte = patte
        self.queue = queue
#####################################################################
##############

class Humain(Animal, Marchant, Courant, Nageant, Flottant):
    
    def __init__(self):
        Animal.__init__(self, 2, False)
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def zone(self):
        return self._zone

    def move_to(self, x, y, z, zone):
        distance = dist(0, 0, x, y)
        if (distance >= 2.0 and distance <= 10.0 and zone == "terre"):
            try:
                return Courant.move_to(self,x,y,z,zone)
            except:
                pass
        elif (distance < 2.0 or distance > 10.0 and zone == "terre"):
            try:
                return Marchant.move_to(self,x,y,z,zone)
            except:
                pass
        else:    
            try:
                return Flottant.move_to(self,x,y,z,zone)
            except:
                pass
            try:
                return Nageant.move_to(self,x,y,z,zone)
            except:
                raise ValueError()



##############

class Cygne(Animal, Volant, Flottant, Nageant):
    
    def __init__(self):
        Animal.__init__(self, 2, True)
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def zone(self):
        return self._zone

    def move_to(self, x, y, z, zone = None):
        try:
            return Flottant.move_to(self,x,y,z,zone)
        except:
            pass
        try:
            return Volant.move_to(self,x,y,z,zone)
        except:
            pass
        try:
            return Nageant.move_to(self,x,y,z,zone)
        except:
            raise ValueError()

class Canard(Animal, Volant, Flottant, Nageant, Marchant, Courant):
    
    def __init__(self):
        Animal.__init__(self, 2, True)
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def zone(self):
        return self._zone

    def move_to(self, x, y, z, zone):
        distance = dist(0, 0, x, y)
        if (z > 0):
            try:
                return Volant.move_to(self,x,y,z,zone)
            except:
                pass
        if (zone == "terre"):
            if (distance >= 2.0 and distance <= 10.0):
                try:
                    return Courant.move_to(self,x,y,z,zone)
                except:
                    pass
            else:
                try:
                    return Marchant.move_to(self,x,y,z,zone)
                except:
                    pass       
        else: 
            if(z == 0): 
                try:
                    return Flottant.move_to(self,x,y,z,zone)
                except:
                    pass
            else:
                try:
                    return Nageant.move_to(self,x,y,z,zone)
                except:
                    raise ValueError()
        

##############

class Poisson(Animal, Nageant):
    
    def __init__(self):
        Animal.__init__(self, 0, True)
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def zone(self):
        return self._zone

    def move_to(self, x, y, z, zone):
        try:
            return Nageant.move_to(self,x,y,z,zone)
        except:
            raise ValueError()




'''
CLASSES DE VEHICULE
'''
#####################################################################
class   Vehicule:
    
    def __init__(self, porte= 2):
        self.porte = porte
#####################################################################
##############

class VoitureSansPermis(Vehicule, Roulant):
    
    def __init__(self):
        Vehicule.__init__(self)
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def zone(self):
        return self._zone

    def move_to(self, x, y, z, zone):
        try:
            return Roulant.move_to(x, y, z, zone)
        except:
            raise ValueError()

##############

class Berline(Vehicule, Roulant):
    
    def __init__(self):
        Vehicule.__init__(self, 5)
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def zone(self):
        return self._zone

    def move_to(self, x, y, z, zone):
        try:
            return Roulant.move_to(x, y, z, zone)
        except:
            raise ValueError()

##############

class Moto(Vehicule, Roulant):
    
    def __init__(self):
        Vehicule.__init__(self, 0)
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def zone(self):
        return self._zone

    def move_to(self, x, y, z, zone):
        try:
            return Roulant.move_to(x, y, z, zone)
        except:
            raise ValueError()
##############

class Hors_Bord(Vehicule, Flottant):
    
    def __init__(self):
        Vehicule.__init__(self)
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def zone(self):
        return self._zone

    def move_to(self, x, y, z, zone):
        try:
            return Flottant.move_to(x, y, z, zone)
        except:
            raise ValueError()

##############

class Spitfire(Vehicule, Volant):
    
    def __init__(self):
        Vehicule.__init__(self)
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def zone(self):
        return self._zone

    def move_to(self, x, y, z, zone):
        try:
            return Volant.move_to(x, y, z, zone)
        except:
            raise ValueError()