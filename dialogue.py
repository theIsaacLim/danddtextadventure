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

shooting_text = ['Bam! You just shot & dead center',
                 'You shoots right into one of &\'s heart',
                 'You can hear the sound of a tight bullet piercing through &\'s skin']

missing_text = ['Ooh- the bullet just barely scrapes a knee but bounces past',
                'You can hear the sound of a bullet just barely missing',
                'The bullet goes completely haywire and completely misses']

alien_text = ['The slippin\', squishin\', sound of tentacles reaches deep into ya soul',
              'You can see a slow pricklin\' as fluorescent slime covers your body']


alien_miss_text = ['A blob of gloop from the alien scrapes the corner of your hat',
                   'A tentacle just barely misses you and crashes down next to you']

directional_text = ['To your %, you can see a glowing doorway',
                    'You can hear the gentle humming of a spaceship to your %',
                    "There's an alien-looking doorway to your %"]

movement_text = ['Carefully, you put one foot in front of another',
                 "You can hear your footsteps echoing through the hall as you dart into the next room"]

drink = ["You glurp down the $",
         "You eat the $ like a ravenous dog",
         "You become one with the $ as it goes down your throat"]

opening = "Welcome to Far Space, \nthe best game in the western regions of space, except space has no west because space doesn't have poles as it is not a planet, but we can mostly ignore this because we have defined it as un-dandy, pardner\nAll un-dandy information will be reported to the council of the dandiness, lead by supreme leader Dan D Dann\nIf you dare disobey Dan D Dann, you will be shot with a shotgun with a cowboy hat on it\n\nSupereme leader Dan has come down with a case of the backdoor trots so he's ordered y'all to invade this alien spaceship. Have a hog-killin' time! Yee-haw!\n"
