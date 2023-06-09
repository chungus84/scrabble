import string

letters = list(string.ascii_uppercase)
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Tracks the words from each player
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# Tracks the points for each player
player_to_points = {}

# combines letters and points into a dictionary
letters_to_points = {letter: point for letter, point in zip(letters, points)}

# add key:value for blank tile
letters_to_points[" "] = 0

def score_word(word):
    """takes a single parameter 'word' and calculates how much that word is
    worth comparing to letters_to_points dictionary"""
    point_total = 0
    for letter in word.upper():
        point_total += letters_to_points.get(letter, 0)
    return point_total


def play_word(player, word):
    """takes 2 arguments and either adds a word to the current list of an existing player
    or creates a new player with a new list in the values"""
    if player in player_to_words:
        player_to_words[player].append(word.upper())
    else:
        player_to_words[player] = [word]
    return update_points_total()


def update_points_total():
    """updates the points totals in player_to_points when called"""
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
    return player_to_points



print(update_points_total())

print(play_word("player1", "SNAKE"))
print(play_word("newPlayer", "SPIDER"))
print(play_word("newPlayer", "dogs"))

# testing the score_words function
# brownie_points = score_word("Brownie")

# print(brownie_points)
