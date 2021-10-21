import abc, math as m

#def     dist(x1 :float, y1 :float, x2 :float, y2 :float) -> float:
#    return (m.sqrt(((x2-x1)**2)+((y2-y1)**2)))

''''''''''
CLASSE DE DEPLACEMENT & TYPES DE LOCOMOTION
''''''''''
#####################################################################
class   Deplacement(ABC):
    @classmethod
    @abstractmethod
    def move_to(self, x :float, y :float, z :float, zone :str):
        self.dist= (m.sqrt(((x2-x1)**2)+((y2-y1)**2)))
#####################################################################
##############

class   Volant(Deplacement):
    def move_to(self, x :float, y :float, z :float, zone :str):
        try:
            assert (z > 0)
        except:
            print("Flying underground!\n")
        return (f"se déplace vers {x}, {y}, {z} en volant")
##############

class   Courant(Deplacement):
    def move_to(self, x :float, y :float, z :float, zone :str):
        try:
            assert (z == 0 and zone == 'terre')
        except:
            print("Running in the sky!\n")
        return (f"se déplace vers {x}, {y} en courant")
##############

class   Marchant(Deplacement):
    def move_to(self, x :float, y :float, z :float, zone :str):
        try:
            assert (z == 0 and zone == 'terre')
        except:
            print("Walking in the sky!\n")
        return (f"se déplace vers {x}, {y} en marchant")
##############

class   Roulant(Deplacement):
    def move_to(self, x :float, y :float, z :float, zone :str):
        try:
            assert (z == 0 and zone == 'terre')
        except:
            print("Rolling in the sky!\n")
        return (f"se déplace vers {x}, {y} en roulant")
##############

class   Flottant(Deplacement):
    def move_to(self, x :float, y :float, z :float, zone :str):
        try:
            assert (z == 0 and zone == 'mer')
        except:
            print("Flotte dans la boue!\n")
        return (f"se déplace vers {x}, {y} en flottant")
##############

class   Nageant(Deplacement):
    def move_to(self, x :float, y :float, z :float, zone :str):
        try:
            assert (z < 0 and zone == 'mer')
        except:
            print("Swimming againt gravity!\n")
        return (f"se déplace vers {x}, {y}, {z} en nageant")
##############




''''''''''
CLASSES D'ANIMAUX
''''''''''
#####################################################################
class   Animal:                                
                                               
    def __init__(self, patte= 4, queue= False):
        self.patte = patte
        self.queue = queue
#####################################################################
##############

class Humain(Animal, Marchant, Courant, Nageant):
    
    def __init__(self):
        Animal.__init__(self, 2, False)
    
    def move_to(self, x :float, y :float, z :float, zone :str):
        mov = None
        Deplacement.move_to(x, y, z, zone)
        print('L\'humain ')
        if (mov= Nageant.move_to(self, x, y, z, zone) or
            (2.0 < Dist < 10.0 and mov= Courant.move_to(self, x, y, z, zone)) or
            mov = Marchant.move_to(self, x, y, z))
            print(mov, x, y, z)
        else
            print(' ne peut pas aller dans cette direction ou cette zone')

##############

class Cygne(Animal, Volant, Flottant):
    
    def __init__(self):
        Animal.__init__(self, 2, False)
    
    def move_to(self, x :float, y :float, z :float, zone :str):
        mov = None
        Deplacement.move_to(x, y, z, zone)
        print('Le cygne ')
        if (mov= Volant.move_to(self, x, y, z, zone) or
            mov= Flottant.move_to(self, x, y, z, zone))
            print(mov, x, y, z)
        else(' ne peut pas aller dans cette direction ou cette zone')
##############

class Canard(Animal, Volant, Flottant, Marchant, Courant):
    
    def __init__(self):
        Animal.__init__(self, 2, False)
    
    def move_to(self, x :float, y :float, z :float, zone :str):
        mov = None
        Deplacement.move_to(x, y, z, zone)
        print('Le canard ')
        if (mov= Volant.move_to(self, x, y, z, zone) or
            mov= Flottant.move_to(self, x, y, z, zone) or
            (2.0 < Dist < 10.0 and mov= Courant.move_to(self, x, y, z, zone)) or
            mov = Marchant.move_to(self, x, y, z))
            print(mov, x, y, z)
        else(' ne peut pas aller dans cette direction ou cette zone')
##############

class Poisson(Animal, Nageant, Flottant):
    
    def __init__(self):
        Animal.__init__(self, 0, True)
    
    def move_to(self, x :float, y :float, z :float, zone :str):
        mov = None
        Deplacement.move_to(x, y, z, zone)
        print('Le poisson ')
        if (mov= Nageant.move_to(self, x, y, z, zone) or
            mov= Flottant.move_to(self, x, y, z, zone))
            print(mov, x, y, z)
        else(' ne peut pas aller dans cette direction ou cette zone')




''''''''''
CLASSES DE VEHICULE
''''''''''
#####################################################################
class   Vehicule:
    
    def __init__(self, porte= 2):
        self.porte = porte
#####################################################################
##############

class VoitureSansPermis(Vehicule, Roulant):
    
    def __init__(self):
        Vehicule.__init__(self, 3)
    
    def move_to(self, x :float, y :float, z :float, zone :str):
        mov = None
        Deplacement.move_to(x, y, z, zone)
        print('La voiture sans permis ')
        if (mov= Roulant.move_to(self, x, y, z, zone))
            print(mov, x, y, z)
        else('ne peut pas aller dans cette direction ou cette zone')
##############

class Berline(Vehicule, Roulant):
    
    def __init__(self):
        Vehicule.__init__(self, 3)
    
    def move_to(self, x :float, y :float, z :float, zone :str):
        mov = None
        Deplacement.move_to(x, y, z, zone)
        print('La berline ')
        if (mov= Roulant.move_to(self, x, y, z, zone)
            print(mov, x, y, z)
        else('ne peut pas aller dans cette direction ou cette zone')
##############

class Moto(Vehicule, Roulant):
    
    def __init__(self):
        Vehicule.__init__(self, 3)
    
    def move_to(self, x :float, y :float, z :float, zone :str):
        mov = None
        Deplacement.move_to(x, y, z, zone)
        print('La moto ')
        if (mov= Roulant.move_to(self, x, y, z, zone)
            print(mov, x, y, z)
        else('ne peut pas aller dans cette direction ou cette zone')
##############

class Hors_Bord(Vehicule, Flottant):
    
    def __init__(self):
        Vehicule.__init__(self, 3)
    
    def move_to(self, x :float, y :float, z :float, zone :str):
        mov = None
        Deplacement.move_to(x, y, z, zone)
        print('Le hors-bord ')
        if (mov= Roulant.move_to(self, x, y, z, zone)
            print(mov, x, y, z)
        else('ne peut pas aller dans cette direction ou cette zone')
##############

class Spitfire(Vehicule, Volant)
    
    def __init__(self):
        Vehicule.__init__(self, 3):
    
    def move_to(self, x :float, y :float, z :float, zone :str):
        mov = None
        Deplacement.move_to(x, y, z, zone)
        print('Le Spitfire ')
        if (mov= Roulant.move_to(self, x, y, z, zone)
            print(mov, x, y, z)
        else('ne peut pas aller dans cette direction ou cette zone')