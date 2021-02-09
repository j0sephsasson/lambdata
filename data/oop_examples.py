""" OOP EXAMPLE """ 

class BareMinimumClass:
    pass 

class Complex:
    def __init__(self, realpart, imagpart):

        """ CONSTRUCTOR FOR COMPLEX NUMBERS """ 

        self.r = realpart
        self.i = imagpart

    def add(self,complex_obj):

        """ ADDS COMPLEX NUMBERS TOGETHER """

        self.r += complex_obj.r
        self.i += complex_obj.i
    
    def __repr__(self):
        return"({},{}i)".format(self.r,self.i)

class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def get_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes

    def is_popular(self):
        return self.upvotes > 100

class Animal:
    def __init__(self,name,weight,location,diet,safe):
        self.name = name
        self.weight = weight
        self.location = location
        self.diet = diet
        self.safe = safe

    def eat(self,food):
       return "HUGE FAN OF" + food
    
    def run(self):
        return "I GO QUICK"

class Sloth(Animal):
    def __init__(self,name,weight,location,diet,safe,naps=160):
        super().__init__(name,weight,safe,location,diet)
        self.naps = naps 

