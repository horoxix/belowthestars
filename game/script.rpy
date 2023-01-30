# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define narrator = Character("")
define e = Character("Eileen")

# The game starts here.
label start:

    $ honesty = 0
    $ romance = 0
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Rev"

    # e "Pleased to meet you, %(player_name)s!"

    scene pond1_night
    player_name "I tried to forget that night..."
    player_name "For someone who hadn't had the most comfortable life thus far, it was still the hardest thing I'd ever attempted."
    player_name "Hard work, from dawn 'till dusk... The kind where the dirt just cakes your skin and becomes part of you..."
    player_name "Yeah that has nothing on that night..."

    scene pond1_night2
    player_name "If you ask me today, i'd tell you that i'm over it, that it's ancient history."
    player_name "But lying... In my line of work, that came easy."
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene pond1_day
    narrator "Two years after the incident..."
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show eileen happy
    # These display lines of dialogue.
    e "Good morning %(player_name)s! You're up late!"
    e "Are you feeling alright?"

    player_name "Yeah... just drank too much last night."

    show eileen wink
    e "I should have known. You forgot what today was, didn't you?"
    menu:
        "What should I do?"

        "It's your birthday?":
            $ romance += 1
            player_name "Of course not, It's your birthday!"
        "It's mom's birthday?":
            $ romance -= 1
            player_name "Ummm it's my mom's birthday?"
        "I have no idea.":
            $ honesty += 1
            player_name "Fuck.. You're right. I'm sorry. Remind me?"
            
    label after_menu:

        if honesty > 0:
            e "Hey, at least I can count on your honesty!."
        elif romance > 0:
            e "I knew you wouldn't forget!"
        else:
            e "I knew you'd forget... It's okay don't worry about it"

    
    # This ends the game.
    return
