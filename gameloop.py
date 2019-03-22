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
    send_text("Welcome to Far Space, \nthe best game in the western regions of space, except space has no west because space doesn't have poles as it is not a planet, but we can mostly ignore this because we have defined it as un-dandy, pardner\nAll un-dandy information will be reported to the council of the dandiness, lead by supreme leader Dan\nIf you dare disobey Dan, you will be shot with a shotgun with a cowboy hat on it\n\nSupereme leader Dan has come down with a case of the backdoor trots so he's ordered y'all to invade this alien spaceship. Have a hog-killin' time! Yee-haw!")
    while True:
        player = Player('Player', 24, 11)
        current_enemy = Enemy("Rootin' Tootin' Putin", 24, 11)

        in_battle = True
        while in_battle:
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

            print_health(player)
            print_health(current_enemy)
