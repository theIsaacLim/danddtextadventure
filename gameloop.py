from combat import Player, Enemy, Item, print_health

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
    player = Player('Sheriff Player', 24, 11)
    enemy = Enemy("Rootin' Tootin' Putin", 24, 11)
    while True:
        input_valid = False
        while not input_valid:
            try:
                move_choice = int(get_input("Press 1 to Attack and 2 to not Attack"))
                if move_choice == 1 or move_choice == 2:
                    input_valid = True
                else:
                    send_text("Invalid input")
            except ValueError:
                print("Invalid input")
        send_text("")
        if move_choice == 1:
            player.physical_attack(enemy)

        enemy.physical_attack(player)

        if enemy.dead:
            send_text("")
            exit()

        print_health(player)
        print_health(enemy)
