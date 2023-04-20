import chess.pgn
import matplotlib.pyplot as plt
import numpy as np

"""
Created by Anthony Ha-Anh Pham on July 16, 2020
Completed July 16, 2020

This program was designed to graphically display White's win percentage
based on only their first move.
"""

pgn_file = open("lichess_db_standard_rated_2014-11.pgn")


def calc_average_win_percentage(results):
    return float(results[0]) / sum(results) * 100


def process_winning_first_moves():
    first_moves_results = {}

    game = chess.pgn.read_game(pgn_file)

    while game is not None:
        moves = game.mainline_moves().__str__().split(" ")
        if len(moves) < 2:
            game = chess.pgn.read_game(pgn_file)
            continue
        first_move = moves[1]
        if first_move not in first_moves_results.keys():
            first_moves_results[first_move] = [0, 0, 0]

        if game.headers["Result"] == "1-0":
            first_moves_results[first_move][0] += 1
        elif game.headers["Result"] == "1/2-1/2":
            first_moves_results[first_move][1] += 1
        elif game.headers["Result"] == "0-1":
            first_moves_results[first_move][2] += 1

        game = chess.pgn.read_game(pgn_file)

    for key in first_moves_results:
        first_moves_results[key] = calc_average_win_percentage(first_moves_results[key])

    first_moves_results = {k: v for k, v in sorted(first_moves_results.items(), key=lambda item: item[1], reverse=True)}
    pgn_file.close()
    return first_moves_results


def plot_winning_percentages():
    first_moves_results = process_winning_first_moves()
    x_labels = list(first_moves_results.keys())
    y_values = list(first_moves_results.values())
    x_values = list(range(1, len(x_labels) + 1))
    plt.ylim(0, 100)

    colors = []
    for percentage in y_values:
        if percentage >= 50:
            colors.append("green")
        else:
            colors.append("red")

    rects = plt.bar(x_values, y_values, color=colors)
    plt.xticks(x_values, x_labels)
    plt.yticks(np.arange(0, 101, 10))
    plt.subplots_adjust(bottom=0.15)

    plt.tick_params(axis="x", pad=5, rotation=90)

    plt.title("Percent Games Won based on First Move")
    plt.xlabel("First Move")
    plt.ylabel("Win Percentage")
    plt.axhline(50, color="black", lw=0.5)
    autolabel(rects)

    plt.show()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{:.4f}%'.format(height), xy=(rect.get_x() + rect.get_width() / 2, 2), xytext=(0, 0),
                     textcoords="offset points", ha='center', va='bottom', rotation=90)


plot_winning_percentages()
