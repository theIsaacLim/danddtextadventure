from combat import Enemy, Item
from random import randint, choice

# name, max_health, ac, hit=[1, 20]
enemies = [Enemy('Floating brain', 15, 5, dmg=[3, 12]),
           Enemy('rOoTiN\' tOoTiN\' PuTiN', 30, 5, dmg=[1, 5]),
           Enemy('Literally just a floating tentacle', 1, 10, dmg=[1, 12])]

afterwards = [Item("nonalcoholic beer", 5, False),
              Item("some weird nonalcoholic root beer-lookin' alien drink", 5, True),
              Item("half a horse testicle", 1, False)]

class Room():
    def __init__(self, monster, item, start=False, leave=False):
        """
        :param monster: Enemy class
        :param item: Item class
        """

class Dungeon():
    def __putTile(self, yAxis, xAxis, tile):
        for i in range(5):
            for e in range(5):
                self.dungeon_map[i+yAxis][e+xAxis] = tile[i][e]

    def __printDungeon(self, use_surround_map=False):
        if not use_surround_map:
            for line in self.dungeon_map:
                print("")
                for room in line:
                    print(str(room) if room != 0 else " ", end="")
        else:
            for line in self.for_surround_check:
                print("")
                for room in line:
                    print(str(room) if room != 0 else " ", end="")

    def __init__(self):
        '''
        Key for dungeon map generation:
        0 ---> No room / Empty space
        1 ---> Normal room / Empty room
        2 ---> Encounter room / Monster room
        3 ---> Dungeon start / Entrance
        4 ---> Portal room / Exit
        5 ---> Treasure room
        '''
        self.dungeon_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        for i in range(9):
            self.dungeon_map.append([0,0,0,0,0,0,0,0,0,0])

        dungeon_start = [  # Presets with the entrance to the dungeon
            [[0, 0, 1, 0, 0],  # Entrance 1 - The loop
            [2, 1, 2, 1, 0],
            [1, 0, 0, 1, 1],
            [2, 0, 0, 2, 0],
            [3, 1, 2, 1, 5]],

            [[1, 1, 2, 0, 0],  # Entrance 2 - The pincers
            [1, 0, 0, 0, 0],
            [1, 2, 5, 0, 1],
            [1, 0, 1, 0, 1],
            [3, 1, 2, 1, 1]],

            [[0, 0, 2, 0, 0],  # Entrance 3 - The broken fish
            [5, 0, 1, 0, 0],
            [1, 2, 1, 2, 2],
            [1, 0, 2, 0, 1],
            [3, 1, 1, 0, 0]],

            [[0, 0, 2, 0, 0],  # Entrance 4 - The thingy-ma-bob
            [5, 1, 2, 0, 0],
            [0, 1, 0, 2, 1],
            [1, 2, 1, 1, 0],
            [3, 0, 0, 0, 0]],

            [[5, 0, 1, 0, 0],  # Entrance 5 - The weird cross
            [1, 0, 1, 0, 0],
            [2, 1, 2, 1, 2],
            [0, 0, 1, 0, 0],
            [3, 1, 2, 0, 0]]
        ]
        dungeon_end = [
            [[0, 0, 1, 0, 4],  # Exit 1 - The rabbit
            [2, 1, 1, 2, 1],
            [1, 0, 1, 0, 0],
            [0, 1, 2, 0, 0],
            [0, 0, 1, 2, 5]],

            [[0, 0, 1, 1, 4],  # Exit 2 - The two golf clubs
            [0, 0, 1, 0, 0],
            [2, 1, 2, 1, 2],
            [0, 0, 1, 0, 1],
            [0, 0, 2, 0, 5]],
            [[0, 0, 0, 0, 4],  # Exit 3 - The dog head

            [0, 2, 1, 2, 1],
            [2, 1, 0, 1, 0],
            [0, 0, 2, 1, 5],
            [0, 0, 1, 0, 0]],

            [[5, 1, 1, 2, 4],  # Exit 4 - The fish
            [0, 1, 0, 0, 1],
            [1, 2, 0, 0, 2],
            [0, 1, 1, 1, 1],
            [0, 0, 2, 0, 0]],

            [[1, 1, 1, 2, 4],  # Exit 5 - The rabbit ears
            [1, 0, 1, 0, 1],
            [2, 0, 5, 2, 2],
            [0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1]]
        ]

        dungeon_preset = [
            [[0, 1, 1, 1, 5],  # Preset 1 - The Monster face
            [0, 1, 0, 1, 1],
            [1, 2, 0, 0, 2],
            [0, 1, 2, 1, 0],
            [0, 0, 1, 0, 0]],

            [[0, 0, 1, 0, 0],  # Preset 2 - The staircase
            [0, 1, 2, 1, 2],
            [1, 1, 0, 5, 1],
            [2, 0, 0, 0, 0],
            [1, 1, 1, 0, 0]],

            [[2, 1, 1, 0, 0],  # Preset 3 - The lambda
            [1, 0, 1, 0, 0],
            [1, 0, 2, 1, 2],
            [0, 5, 1, 0, 0],
            [0, 0, 1, 0, 0]],

            [[1, 1, 1, 1, 2],  # Preset 4 - The bent loop
            [1, 0, 0, 5, 1],
            [1, 1, 2, 0, 2],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 1, 1]],

            [[0, 0, 1, 2, 0],  # Preset 5 - The hooked string
            [0, 0, 0, 1, 0],
            [1, 1, 2, 1, 1],
            [0, 1, 0, 0, 0],
            [5, 2, 1, 0, 0]],

            [[0, 0, 1, 0, 1],  # Preset 6 - The rabbit
            [0, 0, 1, 2, 1],
            [1, 1, 2, 0, 1],
            [0, 1, 1, 2, 5],
            [0, 0, 1, 0,0]]
        ]

        ran_num = randint(0, len(dungeon_start)-1) # Randomly choose a start tile to use
        self.__putTile(5, 0, dungeon_start[ran_num])

        ran_num = randint(0, len(dungeon_end)-1) # Randomly choose a start tile to use
        self.__putTile(0, 5, dungeon_end[ran_num])

        ran_num = randint(0, len(dungeon_preset)-1) # Randomly choose a preset tile to use
        self.__putTile(0, 0, dungeon_preset[ran_num])

        ran_num = randint(0, len(dungeon_preset)-1) # Randomly choose a preset tile to use
        self.__putTile(5, 5, dungeon_preset[ran_num])

        for_surrounding_check = []

        for row in self.dungeon_map:
            for_surrounding_check.append([0] + row + [0])

        for_surrounding_check = [[0] * 12] + for_surrounding_check + [[0] * 12]
        self.for_surround_check = for_surrounding_check
        self.player_position = [0, 9]

    def check_for_surrounding(self, position):
        """
        Check for surrounding rooms around an existing room
        :param position: Position as an array [x, y]
        :return: a list of possible directions, ie. True True False False, meaning that North and East are directions you can go in but South and West are not
        """
        position = [position[0] + 1, position[1] + 1]

        ls = [self.for_surround_check[position[1]-1][position[0]],  # North
                self.for_surround_check[position[1]][position[0]+1],  # East
                self.for_surround_check[position[1]+1][position[0]], # South
                self.for_surround_check[position[1]][position[0]-1]]  # West
        return [x is not 0 for x in ls]

    def move(self, direction):
        """
        :param direction: 0 for N, 1 for E, 2 for S, 3 for W
        :return: Items in new room
        """
        if direction == 0:
            self.player_position = [self.player_position[0], self.player_position[1] - 1]
        elif direction == 1:
            self.player_position = [self.player_position[0] + 1, self.player_position[1]]
        elif direction == 2:
            self.player_position = [self.player_position[0], self.player_position[1] + 1]
        elif direction == 3:
            self.player_position = [self.player_position[0] - 1, self.player_position[1]]

    def check_room(self, position):
        global enemies
        """
        :param position: x, y
        :return:
        """
        '''
        Key for dungeon map generation:
        0 ---> No room / Empty space
        1 ---> Normal room / Empty room
        2 ---> Encounter room / Monster room
        3 ---> Dungeon start / Entrance
        4 ---> Portal room / Exit
        5 ---> Treasure room
        '''
        type_of_room = self.dungeon_map[position[1]][position[0]]
        if type_of_room == 0:
            raise TypeError
        elif type_of_room == 1 or type_of_room == 3:
            return None
        elif type_of_room == 2:
            return choice(enemies)
        elif type_of_room == 4:
            return True
        elif type_of_room == 5:
            # TODO: ITEMS!
            return None

if __name__ == '__main__':
    directions = ['North', 'Yeast', 'South', 'West']
    dungeon = Dungeon()

    current_room = dungeon.check_room(dungeon.player_position)

    print()
    while current_room != True:
        surrounding = dungeon.check_for_surrounding(dungeon.player_position)
        for i in range(len(surrounding)):
            if surrounding[i] == True:
                print("There's a room to your " + directions[i])

        input_valid = False
        while not input_valid:
            try:
                direction = int(input("Which direction will you go in? 0 for North, 1 for Yeast, 2 for South, 3 for West"))
                if direction in [surrounding.index(i) for i in surrounding]:
                    input_valid = True
                else:
                    print("Invalid input")
            except ValueError:
                print("Invalid input")

        dungeon.move(direction)
        current_room = dungeon.check_room(dungeon.player_position)
