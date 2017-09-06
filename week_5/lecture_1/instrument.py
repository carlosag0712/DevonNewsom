class Instrument(object):
    """
    attributes:
    size (small, med, large)
    weight

    methods:
    play
    tune
    """
    def __init__(self, s, w = 300):
        self.size = s
        self.weight = w
        self.has_been_played = False
        self.in_tune = True

    def play(self):
        print "i am playing"
        self.has_been_played = True
        self.in_tune = False

    def tune(self):
        self.in_tune = True
        print "i am tuning now"


class PandaBass(Instrument):
    def __init__(self, color):
        super(PandaBass, self).__init__("large")
        self.color = color

    def eat(self):
        self.in_tune = True
        print "nom nom nom"
    
    def play(self):
        super(PandaBass, self).play()
        print "GRORR IM A PANDABASS"

bob = PandaBass("brown")

bob.eat()
bob.play()

print bob.in_tune
print bob.weight