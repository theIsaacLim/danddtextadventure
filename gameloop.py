from combat import Player, Enemy, Item, print_health
from random import choice
from dungeon import Dungeon
from dialogue import send_text, opening, get_input, directional_text


if __name__ == '__main__':
    send_text(opening)
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
                current_enemy.physical_attack(player)

                print_health(player)
                print_health(current_enemy)

                input_valid = False
                while not input_valid:
                    try:
                        move_choice = int(get_input("Press 1 to shoot the darn alien and 2 to run. Dan recommends y'all shoot the darn alien"))
                        if move_choice == 1 or move_choice == 2:
                            input_valid = True
                        else:
                            send_text("Invalid input")
                    except ValueError:
                        send_text("Invalid input")
                send_text("")
                if move_choice == 1:
                    player.physical_attack(current_enemy)
                elif move_choice == 2:
                    in_battle = False


                if current_enemy.dead:
                    # move to next room
                    in_battle = False


        # Movement
        for i in range(len(surrounding)):
            if surrounding[i] == True:
                print(choice(directional_text).replace("%", directions[i]))

        input_valid = False
        while not input_valid:
            try:
                text_to_print = "Which direction will you go in? \nReply with "
                directions_you_can_go_in = {}
                for i in range(len(surrounding)):
                    if surrounding[i]:
                        directions_you_can_go_in[i] = directions[i]
                        text_to_print += str(i) + " for " + directions[i] + ", "

                direction = int(input(text_to_print))
                if direction in directions_you_can_go_in:
                    input_valid = True
                    direction = directions.index(directions_you_can_go_in[direction])
                else:
                    print("Invalid input")
            except ValueError:
                print("Invalid input")

        dungeon.move(direction)
        current_room = dungeon.check_room(dungeon.player_position)
