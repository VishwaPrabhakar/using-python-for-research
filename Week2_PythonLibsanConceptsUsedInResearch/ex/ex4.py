# Create a function random_place(board, player) that places a
# marker for the current player at random among all the available
# positions (those currently set to 0).
# board is already defined from previous exercises.
# Call random_place(board, player) to place a random marker for Player 2, and
# store this as board to update its value.


# Ex4
import numpy as np
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex2 import create_board, place
from Week2_PythonLibsanConceptsUsedInResearch.ex.ex3 import possibilities
def random_place(board, player):
    possible_placements = possibilities(board)
    if len(possible_placements) > 0:
        possible_placements = random.choice(possible_placements)
        place(board, player, possible_placements)
    return board

random_place(board, 2)
