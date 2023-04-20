import chess.pgn
import matplotlib.pyplot as plt
import numpy as np

pgn_game = open("lichess_db_standard_rated_2014-11.pgn")

"""
Created by Anthony Ha-Anh Pham on July 20, 2020
Completed July 20, 2020

This program was designed to graphically display
how players lose their game (resign, timeout, checkmate)
based on their color (white, black)
"""


def calculate_loss_percentage(loss_distribution):
    total_games_lost = sum(loss_distribution)
    checkmates = float(loss_distribution[0])/total_games_lost * 100
    resignations = float(loss_distribution[1])/total_games_lost * 100
    timeouts = float(loss_distribution[2])/total_games_lost * 100

    percentages = [checkmates, resignations, timeouts]
    return percentages


def get_loss_distribution():
    loss_distribution = {"White": [0, 0, 0], "Black": [0, 0, 0]}
    game = chess.pgn.read_game(pgn_game)

    while game is not None:
        key = "White"
        if game.headers["Result"] == "1-0":
            key = "Black"
        elif game.headers["Result"] == "1-1":
            game = chess.pgn.read_game(pgn_game)
            continue

        if game.headers["Termination"] == "Normal":
            if "#" in game.mainline_moves().__str__():
                loss_distribution[key][0] += 1
            else:
                loss_distribution[key][1] += 1
        else:
            loss_distribution[key][2] += 1

        game = chess.pgn.read_game(pgn_game)

    pgn_game.close()
    loss_distribution["White"] = calculate_loss_percentage(loss_distribution["White"])
    loss_distribution["Black"] = calculate_loss_percentage(loss_distribution["Black"])
    return loss_distribution


def plot_loss_distribution():
    loss_distribution = get_loss_distribution()
    plt.ylim(0, 100)

    # set width of bar
    bar_width = 0.25

    # set height of bar
    checkmates = [loss_distribution["White"][0], loss_distribution["Black"][0]]
    resignations = [loss_distribution["White"][1], loss_distribution["Black"][1]]
    timeouts = [loss_distribution["White"][2], loss_distribution["Black"][2]]

    # Set position of bar on X axis
    r1 = np.arange(len(checkmates))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]

    # Make the plot
    rects1 = plt.bar(r1, checkmates, color="#deebf7", width=bar_width, edgecolor="white", label="Checkmate")
    rects2 = plt.bar(r2, resignations, color="#9ecae1", width=bar_width, edgecolor="white", label="Resignations")
    rects3 = plt.bar(r3, timeouts, color="#3182bd", width=bar_width, edgecolor="white", label="Time Forfeit")

    plt.xticks([r + bar_width for r in range(len(checkmates))], ["White", "Black"])
    plt.yticks(np.arange(0, 101, 10))
    plt.subplots_adjust(bottom=0.15)

    plt.title("Percent Games Lost based on Method of Losing")
    plt.xlabel("Player Color")
    plt.ylabel("Percentage")

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    plt.legend()
    plt.show()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{:.2f}%'.format(height), xy=(rect.get_x() + rect.get_width() / 2 + 0.005, rect.get_height()), xytext=(0, 0),
                     textcoords="offset points", ha='center', va='bottom', rotation=0)


plot_loss_distribution()
