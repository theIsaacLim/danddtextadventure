from combat import Enemy, Item, Player

class Room():
    def __init__(self, monster, item, start=False, leave=False):
        """
        :param monster: Enemy class
        :param item: Item class
        """

class Dungeon():
    def __init__(self, size):
        """
        Constructor also generates the rooms and how they're connected
        :param size: the size of the room
        """

    def check_for_surrounding(self, position):
        """
        Check for surrounding rooms around an existing room
        :param position: Position as an array [x, y]
        :return: a Room class
        """
