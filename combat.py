from random import randint, choice
from dialogue import *

def send_text(text):
    print(text)

def print_health(player):
    display = int(player.current_health/player.max_health * 20)
    send_text(player.name.upper() + "  [%-20s] " % ('='*display) + str(player.current_health) + "/" + str(player.max_health))


class Enemy():
    def __init__(self, name, max_health, ac, hit=[1, 20], dmg=[1, 12]):
        self.name = name
        self.max_health = max_health
        self.current_health = self.max_health
        self.ac = ac
        self.dmg = dmg
        self.strength = 2
        self.hit = hit
        self.dead = False

    def get_hit(self, dmg, hit, enemyName):
        global shooting_text, missing_text
        if hit >= self.ac:
            send_text(choice(shooting_text).replace('&', self.name))
            self.current_health -= dmg
            if self.current_health <= 0:
                self.death()
        else:
            send_text(choice(missing_text))

    def physical_attack(self, enemy):
        dmg = randint(self.dmg[0], self.dmg[1])
        hit = randint(self.hit[0], self.hit[1]) + self.strength
        enemy.get_hit(dmg, hit, self.name)

    def death(self):
        send_text(self.name + " is dead.")
        self.dead = True


class Player(Enemy):
    def __init__(self, name, max_health, ac):
        Enemy.__init__(self, name, max_health, ac, dmg=[1, 12])

    def death(self):
        send_text(self.name + " is dead")
        exit("That's a game over")

    def get_hit(self, dmg, hit, enemyName):
        global alien_text, alien_miss_text
        if hit >= self.ac:
            send_text(choice(alien_text).replace('&', self.name))
            self.current_health -= dmg
            if self.current_health <= 0:
                self.death()
        else:
            send_text(choice(alien_miss_text))


    def consume(self, item):
        """
        Modifies both max_health and current_health values depending on the type of item
        Input: Input an Item() class
        :return: None
        """
        self.current_health += item.health_effect
        print(self.current_health)
        if item.temporary:
            if self.current_health > self.max_health:
                self.current_health = self.max_health
        else:
            self.max_health = self.current_health


class Item():
    def __init__(self, name, health_effect, temporary=True):
        self.name = name
        self.health_effect = health_effect
        self.temporary = temporary
