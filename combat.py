from random import randint
from gameloop import send_text, get_input

def print_health(player):
    display = int(player.current_health/player.max_health * 20)
    send_text(player.name.upper() + "  [%-20s] " % ('='*display) + str(player.current_health) + "/" + str(player.max_health))


class Enemy():
    def __init__(self, name, max_health, ac):
        self.name = name
        self.max_health = max_health
        self.current_health = self.max_health
        self.ac = ac
        self.strength = 2
        self.dead = False

    def get_hit(self, dmg, hit):
        if hit >= self.ac:
            self.current_health -= dmg
            if self.current_hezalth <= 0:
                self.death()

    def physical_attack(self, enemy):
        dmg = randint(1, 12)
        hit = randint(1, 20) + self.strength
        enemy.get_hit(dmg, hit)

    def death(self):
        send_text(self.name + " is dead.")
        self.dead = True


class Player(Enemy):
    def __init__(self, name, max_health, ac):
        Enemy.__init__(self, name, max_health, ac)

    def death(self):
        send_text(self.name + " is dead")
        exit("That's a game over")

    def consume(self, item):
        """
        Modifies both max_health and current_health values depending on the type of item
        Input: Input an Item() class
        :return: None
        """

class Item():
    def __init__(self, health_effect, temporary=True):
        pass
