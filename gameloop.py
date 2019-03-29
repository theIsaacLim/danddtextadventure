from combat import Player, Enemy, Item, print_health
from random import choice, randint
from dungeon import Dungeon
from dialogue import *
import discord
# Items you can pick up after a battle
afterwards = [Item("nonalcoholic beer", 10, False),
              Item("some weird nonalcoholic root beer-lookin' alien drink", 8, True),
              Item("half a horse leg", 1, False),
              Item("top quality alien oxygen", 0, False)]

dandy_dialogue = ['You think you can defeat me? The dandiest in the west?',
                  "I'm never gonna give you up, kid",
                  "*alien screeching*",
                  "You're done, kid",
                  "Man, you've gone a long way. Too bad I'm gonna murder you tonight",
                  "Y'know they're comin' for ya, right? The council?"]

if __name__ == '__main__':
    send_text(opening)
    dungeon = Dungeon()
    player = Player('Player', 24, 11)
    directions = ['North', 'Yeast', 'South', 'West']

    while True:
        break
        current_room = dungeon.check_room(dungeon.player_position)
        surrounding = dungeon.check_for_surrounding(dungeon.player_position)

        if current_room == True:
            break

        # Battle!
        if type(current_room) is Enemy:
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
                    dungeon.kill_monster(dungeon.player_position)
                    item = choice(afterwards)
                    send_text("Hey! That alien dropped " + item.name + " on the floor after it exploded")
                    send_text(choice(drink).replace("$", item.name))
                    player.consume(item)
                    # move to next room
                    in_battle = False

        elif type(current_room) is Item:
            send_text("There's " + item.name + " floating above the ground")
            send_text(choice(drink).replace("$", current_room.name))
            player.consume(item)



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
                    print("Your input is undandy, pardner")
            except ValueError:
                print("Your input is undandy, pardner")

        dungeon.move(direction)
        send_text(choice(movement_text))
        current_room = dungeon.check_room(dungeon.player_position)

    # Boss battle!

    send_text("You have been teleported into a room with a menacing figure in the middle")
    send_text("What? Is that a cowboy hat on a pistol")
    send_text("Hold on... that might be Dan D Dann. It can't be!")

    send_text("\n")
    send_text('"Yeah..."')
    send_text('"Not so dandy, anymore, huh?"')
    send_text("His head starts to spin outwards, and it folds out and over.")
    send_text("Dan D Dann is no more. All that remains is a slimeball with tentacles in a cowboy jacket and hat. \n He screeches as he prepares to attack\n")

    current_enemy = Enemy('Dan D Dann', 30, 5, dmg=[1, 2])
    in_battle = True
    while in_battle:

        print_health(player)
        print_health(current_enemy)

        input_valid = False
        if randint(1, 3) == 3:
            send_text('"$"'.replace("$", choice(dandy_dialogue)))

        move_choice = int(get_input("Press 1 to shoot the darn alien"))
        player.physical_attack(current_enemy)
        if current_enemy.dead:
            in_battle = False
        current_enemy.physical_attack(player)

    send_text("You hear a cold gunshot and the sound of alien blood splattering onto a metal ship")
    send_text('Dan D Dann is... dead?')
    send_text("You're a hero. But they're coming for you. The council, they're coming")
    send_text("Run from this place")
    get_input("Press anything to run from this place")
    send_text("You run into the far west, never to be seen again")
