from random import randint, choice

def send_text(text):
    print(text)

def print_health(player):
    display = int(player.current_health/player.max_health * 20)
    send_text(player.name.upper() + "  [%-20s] " % ('='*display) + str(player.current_health) + "/" + str(player.max_health))

shooting_text = ['Bam! You just shot & dead center', 'You shoots right into one of &\'s heart', 'You can hear the sound of a tight bullet piercing through &\'s skin']
missing_text = ['Ooh- the bullet just barely scrapes a knee but bounces past', 'You can hear the sound of a bullet just barely missing', 'The bullet goes completely haywire and completely misses']
alien_text = ['The slippin\', squishin\', sound of tentacles reaches deep into ya soul', 'You can see a slow pricklin\' as fluorescent slime covers your body']
alien_miss_text = ['The gloop scrapes the corner of your hat', 'The tentacle just barely misses you']

class Enemy():
    def __init__(self, name, max_health, ac):
        self.name = name
        self.max_health = max_health
        self.current_health = self.max_health
        self.ac = ac
        self.strength = 2
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
        dmg = randint(1, 12)
        hit = randint(1, 20) + self.strength
        enemy.get_hit(dmg, hit, self.name)

    def death(self):
        send_text(self.name + " is dead.")
        self.dead = True


class Player(Enemy):
    def __init__(self, name, max_health, ac):
        Enemy.__init__(self, name, max_health, ac)

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

class Item():
    def __init__(self, health_effect, temporary=True):
        pass
