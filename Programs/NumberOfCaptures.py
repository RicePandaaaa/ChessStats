import chess.pgn
import matplotlib.pyplot as plt
import re
import math

pgn_game = open("example.pgn")

"""
Created by Anthony Ha-Anh Pham on July 22, 2020
Completed July 24, 2020

This program was designed to graphically display
the number of captures within ranges of moves
"""


def return_number_of_captures_in_range(move_min, move_max, game):
    moves = re.split(r"\d+\.+ ", game.mainline_moves().__str__())[1:]

    if len(moves) > 0:
        if "%" in moves[0]:
            moves = [move for move in moves[move_min-1:min(move_max*2, len(moves))] if "x" in move]
            return len(moves)
        else:
            moves = [move for move in moves[move_min-1:min(move_max, len(moves))] if "x" in move]
            moves = [move.split() for move in moves]
            moves = [move for sublist in moves for move in sublist if "x" in move]
            return len(moves)

    return 0


def find_number_of_moves(game):
    moves = re.split(r"\d+\.+ ", game.mainline_moves().__str__())[1:]

    if len(moves) > 0:
        if "%" in moves[0]:
            return int(math.ceil(float(len(moves)) / 2))
        return len(moves)

    return 0


def get_captures_per_range():
    game = chess.pgn.read_game(pgn_game)
    captures_per_range = {"1-10": 0, "11-20": 0, "21-30": 0, "31-40": 0, "41-50": 0, "51+": 0}
    move_min, move_max = 1, 10

    while game is not None:
        if move_min < 51:
            captures_per_range[f"{move_min}-{move_max}"] += return_number_of_captures_in_range(move_min, move_max, game)
        else:
            captures_per_range["51+"] += return_number_of_captures_in_range(move_min, move_max, game)

        move_min += 10
        move_max += 10
        if move_min > find_number_of_moves(game):
            game = chess.pgn.read_game(pgn_game)
            move_min, move_max = 1, 10

    return captures_per_range


def plot_captures_per_range():
    captures_per_range = get_captures_per_range()

    x_labels = list(captures_per_range.keys())
    y_values = list(captures_per_range.values())
    x_values = list(range(1, len(x_labels) + 1))

    rects = plt.bar(x_values, y_values, color="#3182bd")
    plt.xticks(x_values, x_labels)

    plt.title("Number of Captures within Specific Move Ranges")
    plt.xlabel("Move Range")
    plt.ylabel("Number of Captures")
    autolabel(rects)

    plt.show()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate(f"{height}", xy=(rect.get_x() + rect.get_width() / 2, height), xytext=(0, 0),
                     textcoords="offset points", ha='center', va='bottom')


plot_captures_per_range()
