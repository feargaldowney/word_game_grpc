import random

# Generates a random phrase at the sart of the game
def gen_random_phrase():
    file = open("phrases.txt", "r")
    phrases = file.readlines()
    count = 0
    """
    NOTE:
    client file cant read phrases through import
    Holy shit am i a genius? wait .... Nope lol
    """

    # PHRASE_TESTER_TO_BE_REMOVED = ["ferg", "was", "'ere"] # DELETE THIS
    MyPhrases = []
    for phrase in phrases: #change back to phrases
        count += 1
        MyPhrases.append(phrase)
        # print("Phrase {}: {}".format(count, phrase.strip()))
    r = random.randint(0, (count -1))
    game_phrase = MyPhrases.pop(r)
    print("Game phrase = ", game_phrase) # DELETE THIS LINE - ONLY FOR DEBUGGING
    return game_phrase

def hide_game_phrase(game_phrase):
    current_game_phrase = ""
    hidden_game_phrase = ""
    for char in game_phrase:
        if char != ',' and char != '-' and char != '\'':
            current_game_phrase += char
    for x in current_game_phrase:
        if x == " ":
            hidden_game_phrase += (" ")
        else:
            hidden_game_phrase += ("_")

    guess_phrase = hidden_game_phrase[:-1] # removes last space as underscore
    # print(guess_phrase)
    return guess_phrase

        
        

# starts the game
def start():
    the_phrase = hide_game_phrase(gen_random_phrase())
    print(the_phrase)
    return the_phrase

