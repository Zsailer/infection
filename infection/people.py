# A simple simulation of Andrea Loes' infection game

class Person(object):
    
    def __init__(self, name):
        """ Cree a person for the simulation and name them. """
        self._name = name
        self._infected = False
        self._contacts = [name]
        
    @property
    def name(self):
        """Get name of person."""
        return self._name    
    
    @property
    def contacts(self):
        """ Return list of people this person contacted over the course of the simulation. """
        return self._contacts[1:]
            
    @property
    def infected(self):
        """ Get True if person is infected. """ 
        return self._infected
        
    def _contact(self, name):
        """ Add someone to the list of people they contacted contacts."""
        try:
            self._contacts.append(name)
        except:
            self._contacts = [name]
            
    @infected.setter
    def infected(self, infected):
        """ Set person to infected. """
        if self._infected is True:
            pass
        else:
            self._infected = True
            
class People(object):
    
    def __init__(self, names):
        """ Run infection simulation on this universe of people. """
        self._names = names
        self._people = list()
        for n in names:
            p = Person(n)
            self._people.append(p)
            setattr(self, n, p)
         
    @property
    def names(self):
        """ Get names of people in universe. """
        return self._names 
               
    @property
    def people(self):
        """ Get people in this universe. """
        return self._people
    
    @property
    def contacts(self):
        """Get all contacts of the universe. """
        return [p.contacts for p in self.people]
        
    @property
    def infections(self):
        """ Get all people infected in the universe. """
        infections = list()
        for p in self.people:
            if p.infected is True:
                infections.append(p.name)
        return infections
        
    @property
    def healthy(self):
        """ Get all healthy people in this universe. """
        healthy = list()
        for p in self.people:
            if p.infected is False:
                healthy.append(p.name)
        return healthy

