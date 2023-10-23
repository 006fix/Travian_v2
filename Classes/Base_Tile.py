import random

class Location:
    def __init__(self, location):
        self.location = location #where it exists on the map
        self.interactable = True #can this square be interacted with
        self.owner = None #which player owns this square
        self.Last_Active = 0 #last moment this square was activated
        self.Sleep = True #is this square asleep


class Square(Location):
    def __init__(self, location):
        super().__init__(location)
        randval = random.randint(0 ,100)
        if randval < 10:
            self.type_square = 'wilderness' #uninhabitable
        elif randval < 30:
            self.type_square = 'oasis' #can't build village can occupy
        else:
            self.type_square = 'habitable' #standard habitable square for village