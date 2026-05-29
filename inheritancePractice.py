class PartyAnimal:
    def __init__(self, nam) :
        self.x = 0
        self.name = nam
        print(self.name,  "I am constructing")
    
    def party(self):
        self.x = self.x +1
        print(self.name, "party count: ", self.x)

class FootballFan(PartyAnimal):
    def __init__(self, name):
        super().__init__(name)
        self.points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

sal = PartyAnimal("Sally")
sal.party()
jim = FootballFan("Jim")
jim.touchdown()
jim.party()
