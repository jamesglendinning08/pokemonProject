###############################################################################
# Title: Pokemon Menus
# Assignment: Pokemon (part 3) - Populate & Menu
# Class: CS30
# Coder: James Glendinning
# Date: 9/26/2025
# Version: 1
###############################################################################
'''4 dictionaries of Pokemon compounded into one global database.'''
###############################################################################
# Imports and Global Variables ------------------------------------------------
player = {"name": None, "active": None}

pokedex = {"Charmander": {"type": "Fire",
                         "moves": ["Tackle", "Scratch", "Ember"],
                         "status": "inactive"},
          "Bulbasaur": {"type": "Grass",
                        "moves": ["Tackle", "Growl", "Vine Whip"],
                        "status": "inactive"},
          "Squirtle": {"type": "Water",
                        "moves": ["Tackle", "Scratch", "Water Gun"],
                        "status": "inactive"},
          "Pikachu": {"type": "Electric",
                        "moves": ["Tackle", "Quick Attack", "Thunderbolt"],
                        "status": "inactive"}}

activepokemon = None

activemove = None
# Functions -------------------------------------------------------------------


def introduction():
    print("Welcome, trainer, to the world of Pokémon!")
    print("My name is Professor Oak, and I am here to help you begin",
          "your Pokémon journey.")
    print("However, before we start, I must ask you something crucial!\n")
    player["name"] = input("What is your name? ")
    print("It is wonderful to meet you, " + player["name"].title() + "!")
    print("Now, let us begin.")
    
    
def mainmenu():
    print("Choose your Pokémon, one move, and its nickname:")
    print("-POKEMON\n-MOVE\n-NICKNAME\n-QUIT\n-START")
    menuchoice = input("What will you do? \n").lower()
    if menuchoice in menuchoices:
        menuchoices[menuchoice]()
    else:
        print("Invalid choice.")
        mainmenu()
            
 
def pokemon():
    global activepokemon
    print("Which Pokémon do you choose?")
    print("-CHARMANDER\n-BULBASAUR\n-SQUIRTLE\n-PIKACHU")
    pokemonchoice = input("Which will you choose? \n").title()
    if pokemonchoice in pokedex:
        activepokemon = pokemonchoice
        print(activepokemon + "! Good choice!\n")
        if not activemove == None:
            if not activemove in pokedex[activepokemon]["moves"]:
                print("However, "+activepokemon+" cannot use "+
                      activemove.title() + ".\n")
                move()
        else:
            mainmenu()
    else:
        print("Invalid choice.")
        pokemon()
    
    
def move():
    if not activepokemon == None:
        print("Choose a move that "+ activepokemon +" can use.")
        for i in pokedex[activepokemon]["moves"]:
            print("-" + i.upper())
        movechoice = input("Which will you choose? \n").title()
        if movechoice in pokedex[activepokemon]["moves"]:
            activemove = movechoice
            print(activepokemon+" learned how to use "+activemove+".\n")
            mainmenu()
    else:
        print("Oops! You need to choose a Pokémon first!")
        pokemon()
    
    
def nickname():
    print("picking nickname")
    
    
def quit():
    print("quitting")
    

# Main ------------------------------------------------------------------------
menuchoices = {"pokemon": pokemon, "move": move,
               "nickname": nickname, "quit": quit}
introduction()
mainmenu()