from combat import Player, Enemy, Item, print_health
from dungeon import Dungeon

# The equivalent to the print function, will be replaced for messaging functionality
def send_text(text):
    """
    Sends a text to the user, currently as just a print value but eventually as an actual text message on some social media
    :param text:
    :return:
    """
    print(text)

# Decision making!
def get_input(prompt):
    """
    Gets an input from the user, currently as STD python unit but
    :param prompt: the prompt from the user
    :return: A string
    """
    return input(prompt)


if __name__ == '__main__':
    send_text("Welcome to Far Space, \nthe best game in the western regions of space, except space has no west because space doesn't have poles as it is not a planet, but we can mostly ignore this because we have defined it as un-dandy, pardner\nAll un-dandy information will be reported to the council of the dandiness, lead by supreme leader Dan\nIf you dare disobey Dan, you will be shot with a shotgun with a cowboy hat on it\n\nSupereme leader Dan has come down with a case of the backdoor trots so he's ordered y'all to invade this alien spaceship. Have a hog-killin' time! Yee-haw!")
    dungeon = Dungeon()
    player = Player('Player', 24, 11)
    directions = ['North', 'Yeast', 'South', 'West']

    while True:
        current_room = dungeon.check_room(dungeon.player_position)
        surrounding = dungeon.check_for_surrounding(dungeon.player_position)

        # Battle!
        if type(current_room) is not int and current_room is not True and current_room is not None:
            current_enemy = current_room
            in_battle = True
            while in_battle:
                print_health(player)
                print_health(current_enemy)

                input_valid = False
                while not input_valid:
                    try:
                        move_choice = int(get_input("Press 1 to shoot the darn alien and 2 to not shoot the darn alien. Dan recommends y'all shoot the darn alien"))
                        if move_choice == 1 or move_choice == 2:
                            input_valid = True
                        else:
                            send_text("Invalid input")
                    except ValueError:
                        send_text("Invalid input")
                send_text("")
                if move_choice == 1:
                    player.physical_attack(current_enemy)

                current_enemy.physical_attack(player)

                if current_enemy.dead:
                    # move to next room
                    in_battle = False


        # Movement
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
