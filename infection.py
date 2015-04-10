# A simple simulation of Andrea Loes' infection game
import random as r
import numpy as np

def in_history(new_name, old_names):
    """ Return True if new_name is in old_names. """
    for name in old_names:
        if new_name == name:
            return True
    return False
    

class Person(object):
    
    def __init__(self, name):
        """ Create a person for the simulation and name them. """
        self._name = name
        self._infected = False
        
    @property
    def name(self):
        """Get name of person."""
        return self._name    
    
    @property
    def contacts(self):
        """ Return list of people this person contacted over the course of the simulation. """
        return self._contacts
            
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
            
class Universe(object):
    
    def __init__(self, names):
        """ Run infection simulation on this universe of people. """
        self._names = names
        self._people = dict()
        for n in names:
            self._people[n] = Person(n)
         
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
        for key,val in self._persons.items():
            if val.infected is True:
                infections.append(key)
        return infections

        
class InfectionGame(Universe):
    
    def __init__(self, rounds, names, patient0=None):
        """ Names and rounds of infection game. """
        super(InfectionGame, self).__init__(names)
        self._rounds = rounds
        # Randomly select patient 0, the start of the infection
        if patient0 is None:
            self._patient0 = r.choice(self.people)
        else:
            self._patient0 = patient0
        
    @property
    def rounds(self):
        """ Get rounds of infections. """
        return self._rounds
    
    @property
    def patient0(self):
        """Get patient-0, i.e. the person that started the infection spread. """
        return self._patient0
        
    def infect(self):
        """ Run infection simulation. """
        for r in range(1,self.rounds+1):
            history = True
            counter = 0
            # A new round with no old contacts
            while history is True or counter < 100:
                peeps = self.names
                r.shuffle(peeps)
                self._check_history(peeps)
                counter += 1
            if counter == 100:
                raise Exception("Reached maximum iterations.")
            for i in range(len(self.people)):
                self.people[peeps[i]].
                p._contact = peeps[i]
        
    def _check_history(self, shuffled):
        """ Check history each person to make sure they don't contact the same person twice. """
        contacts = self.contacts
        for i in range(len(shuffled)):
            for j in range(len(self.contacts[i])):
                if shuffled[i] = self.contacts[i,j]:
                    return True
        return False