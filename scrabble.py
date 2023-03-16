letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# combines letters and points into a dictionary
letters_to_points = {letter: point for letter, point in zip(letters, points)}

# add key:value for blank tile
letters_to_points[" "] = 0

def score_word(word):
    """takes a single parameter 'word' and calculates how much that word is
    worth comparing to letters_to_points dictionary"""
    point_total = 0
    for letter in word.upper():
        point_total += letters_to_points[letter]
    return point_total

print(score_word("Hello"))
