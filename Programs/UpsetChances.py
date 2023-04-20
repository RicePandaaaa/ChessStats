import chess.pgn
import matplotlib.pyplot as plt
import numpy as np

pgn_game = open("lichess_db_standard_rated_2014-11.pgn")

"""
Created by Anthony Ha-Anh Pham on July 26, 2020
Completed July 27, 2020

This program was designed to graphically display
the chances of the lower rated player to win the match
based on color and rating difference
"""


def process_game():
    game = chess.pgn.read_game(pgn_game)

    rating_diff = {"1-10": [0, 0, 0, 0], "11-25": [0, 0, 0, 0],
                   "26-50": [0, 0, 0, 0], "51-99": [0, 0, 0, 0], "100+": [0, 0, 0, 0]}

    while game is not None:
        if game.headers["WhiteElo"] == "?" or game.headers["BlackElo"] == "?":
            game = chess.pgn.read_game(pgn_game)
            continue
            
        game_rating_diff = int(game.headers["WhiteElo"]) - int(game.headers["BlackElo"])
        index = 1 if game_rating_diff >= 0 else 0

        if 0 <= abs(game_rating_diff) <= 10:
            if (game.headers["Result"] == "1-0" and game_rating_diff < 0) or \
                    (game.headers["Result"] == "0-1" and game_rating_diff > 0):
                rating_diff["1-10"][index] += 1
            rating_diff["1-10"][index + 2] += 1
        elif 11 <= abs(game_rating_diff) <= 25:
            if (game.headers["Result"] == "1-0" and game_rating_diff < 0) or \
                    (game.headers["Result"] == "0-1" and game_rating_diff > 0):
                rating_diff["11-25"][index] += 1
            rating_diff["11-25"][index + 2] += 1
        elif 26 <= abs(game_rating_diff) <= 50:
            if (game.headers["Result"] == "1-0" and game_rating_diff < 0) or \
                    (game.headers["Result"] == "0-1" and game_rating_diff > 0):
                rating_diff["26-50"][index] += 1
            rating_diff["26-50"][index + 2] += 1
        elif 51 <= abs(game_rating_diff) <= 99:
            if (game.headers["Result"] == "1-0" and game_rating_diff < 0) or \
                    (game.headers["Result"] == "0-1" and game_rating_diff > 0):
                rating_diff["51-99"][index] += 1
            rating_diff["51-99"][index + 2] += 1
        elif 100 <= abs(game_rating_diff):
            if (game.headers["Result"] == "1-0" and game_rating_diff > 0) or \
                    (game.headers["Result"] == "0-1" and game_rating_diff < 0):
                rating_diff["100+"][index] += 1
            rating_diff["100+"][index + 2] += 1

    pgn_game.close()
    return rating_diff


def convert_rating_diff(rating_diff):
    for key in rating_diff.keys():
        values = rating_diff[key]
        rating_diff[key] = [float(values[0])/max(1, values[2]) * 100, float(values[1])/max(1, values[3]) * 100]
        
    return rating_diff


def plot_upset_chances():
    rating_diff = convert_rating_diff(process_game())
    plt.ylim(0, 100)

    # set width of bar
    bar_width = 0.25

    # set height of bar
    white = [value[0] for value in rating_diff.values()]
    black = [value[1] for value in rating_diff.values()]

    # Set position of bar on X axis
    r1 = [x + (bar_width/2) for x in range(1, len(white)+1)]
    r2 = [x + bar_width for x in r1]

    # Make the plot
    rects1 = plt.bar(r1, white, color="#deebf7", width=bar_width, edgecolor="white", label="White")
    rects2 = plt.bar(r2, black, color="#9ecae1", width=bar_width, edgecolor="white", label="Black")

    plt.xticks([r + bar_width for r in range(1, len(white)+1)], ["1-10", "11-25", "25-50", "51-99", "100+"])
    plt.yticks(np.arange(0, 101, 10))
    plt.subplots_adjust(bottom=0.15)

    plt.title("Chances of Winning Based on Rating Difference")
    plt.xlabel("Rating Difference")
    plt.ylabel("Percentage")

    autolabel(rects1)
    autolabel(rects2)

    plt.legend()
    plt.show()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{:.2f}%'.format(height), xy=(rect.get_x() + rect.get_width() / 2 + 0.005, 0.5),
                     xytext=(0, 0),
                     textcoords="offset points", ha='center', va='bottom', rotation=90)


plot_upset_chances()
