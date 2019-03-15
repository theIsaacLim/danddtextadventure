from combat import Player, Enemy, print_health

# The equivalent to the print function, will be replaced for messaging functionality
def send_text(text):
    print(text)

# Decision making!
def make_decision(text):
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

if __name__ == '__main__':
    player = Player('player', 24, 11)
    enemy = Enemy('enemy', 24, 11)
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
        print("")
        if move_choice == 1:
            player.physical_attack(enemy)

        enemy.physical_attack(player)

        if enemy.dead:
            exit("All enemies in this room are dead... Congratulations!")

        print_health(player)
        print_health(enemy)
