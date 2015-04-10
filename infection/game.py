import random
from .people import People
        
class InfectionGame(People):
    
    def __init__(self, names, patient0=None):
        """ Names and rounds of infection game. 
        
            Args:
            ---- 
            rounds: int
                Number of infection rounds to simulate spread.
            names: list of str
                List of names for participants in the game.
            patient0: str
                Name if you want to manually enter patient0.
                
            Attr:
            ----
            round: int
                number of round of infection
            patient0: str
                name of person who is the source of infection 
        """
        # Check that the number of people in the game are even.
        if len(names)%2.0 != 0:
            raise Exception("The number of people participating must be even.")
            
        super(InfectionGame, self).__init__(names)
        self._rounds = 0
        # Randomly select patient 0, the start of the infection
        if patient0 is None:
            self._patient0 = random.choice(self.people)
            self._people[self.names.index(self._patient0.name)].infected = True
        else:
            self._patient0 = patient0
        
    @property
    def rounds(self):
        """ Get number of rounds this infection spread. """
        return self._rounds
    
    @property
    def patient0(self):
        """Get patient-0, i.e. the person that started the infection spread. """
        return self._patient0
        
    def infect(self, n):
        """ Run infection simulation. 
            Arg: 
            ---
            n: int
                number of rounds of infection.
        """
        self._rounds += n
        # Run infection simulation with a specified number of rounds
        for r in range(1,n+1):
            history = True
            counter = 0
            
            # A new round with no old contacts
            while history is True and counter < 100:
                peeps = list(self.names)
                # Shuffle people in place
                random.shuffle(peeps)
                # Prepare an ordered list of pairing to propose
                paired_list = self._make_pairs(peeps)
                # Check if contacts are in history
                history = self._check_history(paired_list)
                counter += 1
            
            # Raise error if while loop hit limit.
            if counter >= 100:
                raise Exception("Reached maximum iterations.")
                
            # Add next round of contacts to all people.                
            for p in range(len(self.people)):
                self.people[p]._contact(paired_list[p])
            
            # Set people properties to infected
            for i in self.infections:
                self.people[paired_list.index(i)].infected = True


    def _check_history(self, shuffled):
        """ Check history each person to make sure they don't contact the same person twice.
            
            Arg:
            ---
            shuffled: list of str
                Shuffled list that has been ordered into pairing. 
        """
        for i in range(len(shuffled)):
            for j in range(len(self.contacts[i])):
                if shuffled[i] == self.contacts[i][j] or shuffled[i] == self.names[i]:
                    return True
        return False
        
    def _make_pairs(self, shuffled):
        """ Take a shuffled list, split into two, form pairs, anr return list thats ordered to make pairs. """
        # Split shuffled list in half 
        split_n = int(len(shuffled)/2)
        half1 = shuffled[0:split_n]
        half2 = shuffled[split_n:]
        
        # Create mapping between two people.
        pairs = dict()
        for i in range(split_n):
            pairs[half1[i]] = half2[i]
            pairs[half2[i]] = half1[i]

        # Form reordered list with self.people
        pair_list = list()
        for p in range(len(self.people)):
            pair_list.append(pairs[self.people[p].name])
            
        return pair_list