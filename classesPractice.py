class PracticingClasses:
    def __init__(self, z) :
        self.x = 0
        self.name = z
        print(self.name,  "I am constructing")
    
    def party(self):
        self.x = self.x +1
        print(self.name, "so far: ", self.x)

    def __del__(self):
        print("I am destructing", self.x)
an = PracticingClasses("Sally")

an.party()
jn = PracticingClasses("Jane")
jn.party()
an.party()
jn.party()
#an = 42 ## object is now gone, replaced party animal it deconstructed on it's own
#print('an contains', an)

