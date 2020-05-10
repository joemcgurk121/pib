
#         __0__
#        |     |
#        5     1
#        |     |
#         --6--
#        |     |
#        4     2
#        |     |
#         --3--
#
#           0   1
#        11        2
#        10        3
#           12  13
#        9         4
#        8         5
#           7   6


number_to_segment = {
    '0': [0, 1, 2, 3, 4, 5],
    '1': [1, 2],
    '2': [0, 1, 3, 4, 6],
    '3': [0, 1, 2, 3, 6],
    '4': [1, 2, 5, 6],
    '5': [0, 2, 3, 5, 6],
    '6': [0, 2, 3, 4, 5, 6],
    '7': [0, 1, 2],
    '8': [0, 1, 2, 3, 4, 5, 6],
    '9': [0, 1, 2, 3, 5, 6],
    'A': [0, 1, 2, 4, 5, 6],
    'B': [0, 1, 2, 3, 4, 5, 6],
    'b': [2, 3, 4, 5, 6],
    'C': [0, 3, 4, 5],
    'c': [3, 4, 6],
    'D': [0, 1, 2, 3, 4],
    'd': [1, 2, 3, 4, 6],
    'E': [0, 3, 4, 5, 6],
    'e': [0, 1, 3, 4, 5, 6],
    'F': [0, 4, 5, 6],
    'f': [0, 4, 5, 6],
    'G': [0, 2, 3, 4, 5],
    'g': [0, 1, 2, 3, 5, 6],
    'H': [1, 2, 4, 5, 6],
    'h': [2, 4, 5, 6],
    'I': [4, 5],
    'i': [4],
    'J': [1, 2, 3, 4],
    'j': [1, 2, 3],
    'K': [1, 3, 4, 5, 6],
    'L': [3, 4, 5],
    'l': [4, 5],
    'N': [0, 1, 2, 4, 5],
    'n': [2, 4, 6],
    'O': [0, 1, 2, 3, 4, 5],
    'o': [2, 3, 4, 6],
    'P': [0, 1, 4, 5, 6],
    'p': [0, 1, 4, 5, 6],
    'q': [0, 1, 2, 5, 6],
    'R': [0, 1, 4, 5],
    'r': [4, 6],
    'S': [0, 2, 3, 5, 6],
    's': [0, 2, 3, 5, 6],
    'T': [0, 4, 5],
    't': [3, 4, 5, 6],
    'U': [1, 2, 3, 4, 5],
    'u': [2, 3, 4],
    'V': [1, 2, 3, 4, 5],
    'v': [2, 3, 4],
    'X': [1, 2, 4, 5, 6],
    'x': [1, 2, 4, 5, 6],
    'Y': [1, 2, 3, 5, 6],
    'y': [1, 2, 3, 5, 6],
    'Z': [0, 1, 3, 4, 6],
    'z': [0, 1, 3, 4, 6]
}

color_name_to_rgb_tuple = {
    'red': (1, 0, 0),
    'orange' : (1, .65, 0),
    'yellow': (1, 1, 0),
    'green': (0, 1, 0),
    'blue': (0, 0, 1),
    'purple': (1, 0, 1),
    'white': (1, 1, 1)
}