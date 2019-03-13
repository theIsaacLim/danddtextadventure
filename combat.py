from random import randint


class Player(object):
    def __init__(self, name, max_health, ac):
        self.name = name
        self.max_health = max_health
        self.current_health = self.max_health
        self.ac = ac
        self.strength = 2

    def get_hit(self, dmg, hit):
        if hit >= self.ac:
            self.current_health -= dmg
            if self.current_health <= 0:
                self.death()

    def physical_attack(self, enemy):
        dmg = randint(1, 12)
        hit = randint(1, 20) + self.strength
        enemy.get_hit(dmg, hit)

    def death(self):
        print(self.name + " is dead")
        exit("That's a game over")


class Enemy(object):
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
            if self.current_health <= 0:
                self.death()

    def physical_attack(self, enemy):
        dmg = randint(1, 12)
        hit = randint(1, 20) + self.strength
        enemy.get_hit(dmg, hit)

    def death(self):
        print(self.name + " is dead.")
        self.dead = True

player = Player('ya boi', 24, 11)
enemy = Enemy('ya enemy', 24, 11)
while True:
    input_valid = False
    while not input_valid:
        try:
            move_choice = int(input("Press 1 to Attack and 2 to not Attack"))
            if move_choice == 1 or move_choice == 2:
                input_valid = True
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")

    if move_choice == 1:
        player.physical_attack(enemy)

    enemy.physical_attack(player)

    if enemy.dead:
        exit("All enemies in this room is dead... Congratulations!")

    print(player.name + ": " + str(player.current_health) + "/" + str(player.max_health))
    print(enemy.name + ": " + str(enemy.current_health) + "/" + str(enemy.max_health))
