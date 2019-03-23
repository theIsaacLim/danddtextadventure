from combat import Enemy, Item, Player
from random import randint

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

    def __printDungeon(self):
        for line in self.dungeon_map:
            print()
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
            [1, 1, 1, 1, 0],
            [1, 0, 0, 1, 1],
            [1, 0, 0, 1, 0],
            [3, 1, 1, 1, 5]],

            [[1, 1, 1, 0, 0],  # Entrance 2 - The pincers
            [1, 0, 0, 0, 0],
            [1, 1, 5, 0, 1],
            [1, 0, 1, 0, 1],
            [3, 1, 1, 1, 1]],

            [[0, 0, 1, 0, 0],  # Entrance 3 - The broken fish
            [5, 0, 1, 0, 0],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [3, 1, 1, 0, 0]],

            [[0, 0, 1, 0, 0],  # Entrance 4 - The thingy-ma-bob
            [5, 1, 1, 0, 0],
            [0, 1, 0, 1, 1],
            [1, 1, 1, 1, 0],
            [3, 0, 0, 0, 0]],

            [[5, 0, 1, 0, 0],  # Entrance 5 - The weird cross
            [1, 0, 1, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [3, 1, 1, 0, 0]]
        ]
        dungeon_end = [
            [[0, 0, 1, 0, 4],  # Exit 1 - The rabbit
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 1, 5]],

            [[0, 0, 1, 1, 4],  # Exit 2 - The two golf clubs
            [0, 0, 1, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 0, 5]],
            [[0, 0, 0, 0, 4],  # Exit 3 - The dog head

            [0, 1, 1, 1, 1],
            [1, 1, 0, 1, 0],
            [0, 0, 1, 1, 5],
            [0, 0, 1, 0, 0]],

            [[5, 1, 1, 1, 4],  # Exit 4 - The fish
            [0, 1, 0, 0, 1],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 0, 1, 0, 0]],

            [[1, 1, 1, 1, 4],  # Exit 5 - The rabbit ears
            [1, 0, 1, 0, 1],
            [1, 0, 5, 1, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1]]
        ]

        dungeon_preset = [
            [[0, 1, 1, 1, 5],  # Preset 1 - The Monster face
            [0, 1, 0, 1, 1],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0]],

            [[0, 0, 1, 0, 0],  # Preset 2 - The staircase
            [0, 1, 1, 1, 1],
            [1, 1, 0, 5, 1],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0]],

            [[1, 1, 1, 0, 0],  # Preset 3 - The lambda
            [1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [0, 5, 1, 0, 0],
            [0, 0, 1, 0, 0]],

            [[1, 1, 1, 1, 1],  # Preset 4 - The bent loop
            [1, 0, 0, 5, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 1, 1]],

            [[0, 0, 1, 1, 0],  # Preset 5 - The hooked string
            [0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 0, 0],
            [5, 1, 1, 0, 0]],

            [[0, 0, 1, 0, 1],  # Preset 6 - The rabbit
            [0, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 1, 1, 1, 5],
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

        self.__printDungeon()

    def check_for_surrounding(self, position):
        """
        Check for surrounding rooms around an existing room
        :param position: Position as an array [x, y]
        :return: a list of possible directions, ie. True True False False, meaning that North and East are directions you can go in but South and West are not
        """
        print(self.dungeon_map[position[1]][position[0]])
        at_bottom_row = position[0] == len(self.dungeon_map)-1
        at_top_row = position[0] == 0
        at_left_end = position[1] == 0
        at_right_end = position[1] == len(self.dungeon_map[0])-1

        if at_bottom_row and not at_left_end and not at_right_end:
            print('AT BOTTOM ROW')
            return [self.dungeon_map[position[1]-1][position[0]] is not 0,  # North
                    self.dungeon_map[position[1]][position[0]+1] is not 0,  # East
                    False,  # South
                    self.dungeon_map[position[1]][position[0]-1] is not 0]  # West
        elif at_top_row and not at_left_end and not at_right_end:
            print('AT TOP ROW')
            return [False,  # North
                    self.dungeon_map[position[1]][position[0]+1] is not 0,  # East
                    self.dungeon_map[position[1]+1][position[0]] is not 0,  # South
                    self.dungeon_map[position[1]][position[0]-1] is not 0]  # West
        elif at_left_end and not at_top_row and not at_bottom_row:
            print('AT LEFT END')
            return [self.dungeon_map[position[1]-1][position[0]] is not 0,  # North
                    self.dungeon_map[position[1]][position[0]+1] is not 0,  # East
                    self.dungeon_map[position[1]+1][position[0]] is not 0,  # South
                    False]  # West
        elif at_right_end and not at_top_row and not at_bottom_row:
            print('AT RIGHT END')
            return [self.dungeon_map[position[1]-1][position[0]] is not 0,  # North
                    False,  # East
                    self.dungeon_map[position[1]+1][position[0]] is not 0,  # South
                    self.dungeon_map[position[1]][position[0]-1] is not 0]  # West
        elif not at_bottom_row and not at_top_row and not at_left_end and not at_right_end:
            print('IN THE MIDDLE')
            return [self.dungeon_map[position[1]-1][position[0]] is not 0,  # North
                    self.dungeon_map[position[1]][position[0]+1] is not 0,  # East
                    self.dungeon_map[position[1]+1][position[0]] is not 0,  # South
                    self.dungeon_map[position[1]][position[0]-1] is not 0]  # West
        else:
            if at_top_row:
                if at_left_end:
                    print('Top left')
                    return [False,  # North
                            self.dungeon_map[position[1]][position[0]+1] is not 0,  # East
                            self.dungeon_map[position[1]+1][position[0]] is not 0,  # South
                            False]  # West
                elif at_right_end:
                    print('Top right')
                    return [False,  # North
                            False,  # East
                            self.dungeon_map[position[1]+1][position[0]] is not 0,  # South
                            self.dungeon_map[position[1]][position[0]-1] is not 0]  # West
            if at_bottom_row:
                if at_left_end:
                    print('Bottom left')
                    return [self.dungeon_map[position[1]-1][position[0]] is not 0,  # North
                            self.dungeon_map[position[1]][position[0]+1] is not 0,  # East
                            False,  # South
                            False]  # West
                elif at_right_end:
                    print('Bottom right')
                    return [self.dungeon_map[position[1]-1][position[0]] is not 0,  # North
                            False,  # East
                            False,  # South
                            self.dungeon_map[position[1]][position[0]-1] is not 0]  # West

dungeon = Dungeon()
print(dungeon.check_for_surrounding([int(input("x")), int(input("y"))]))
