
class Lizard(object):
    """
    attribues:
    size_of_tail
    scale_color
    name

    methods:
    climb
    scurry
    """
    def __init__(self, name, size, color):
        self.name = name
        self.tail_size = size
        self.scale_color = color
        self.altitude = 0
        self.distance_traveled = 0

    def climb(self, height):
        self.altitude += height
        print "im climbingggg!!!"

    def scurry(self, speed, surface):
        """
        surface => wood, grass, water
        """
        speed_mod = 0
        if surface == "wood":
            speed_mod = 5
        elif surface == "grass":
            speed_mod = 3
        else:
            speed_mod = 1
        self.distance_traveled += self.distance_traveled + (speed*speed_mod)
        
class Godzilla(Lizard):
    def __init__(self, color):
        super(Godzilla, self).__init__("Godzilla", 100, color)
        self.enemies = []

    def add_enemy(self, enemy_name):
        self.enemies.append(enemy_name)

    def battle(self, enemy_name):
        if not enemy_name in self.enemies:
            print "{} isn't an enemy".format(enemy_name)
        else:
            print "Godzilla vs. {}".format(enemy_name)

godzilla = Godzilla("greyish-green")
godzilla.add_enemy("Rodan")
godzilla.add_enemy("Mothra")
godzilla.add_enemy("Ghidrah")

godzilla.battle("Ghidrah")
godzilla.battle("MechaGodzilla")
godzilla.scurry(1000, "grass")

