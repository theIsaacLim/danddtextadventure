from combat import Player, Enemy, print_health

player = Player('player', 24, 11)
enemy = Enemy('11enemy', 24, 11)
while True:
    input_valid = False
    while not input_valid:
        try:
            move_choice = int(input("Press 1 to Attack and 2 to not Attack\n"))
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

    print_health(player)
    print_health(enemy)
