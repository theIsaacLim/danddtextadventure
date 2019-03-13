from random import randint

character = {'name': 'Player',
             'health': 24,
             'ac': 17}

class Player(object):
    def __init__(self, name, age):
        self.name = 'Player'
        self.max_health = 24
        self.current_health = self.max_health
        self.ac = 17

    def get_hit(self, dmg):
        hit = randint(20)
        if hit >= self.ac:
            self.current_health -= dmg
            if self.current_health <= 0:
                self.death()

    def death(self):
        exit("bleh. you're fucking dead, mate.")

