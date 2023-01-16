# rlchess



NN guided MCTS for chess

Currently following https://github.com/DenseLance/mcts-simple/blob/main/examples/Chess%20(currently%20extremely%20slow)/Chess.ipynb



Working on pivoting this project. Use the same approach of NN-guided MCTS but not for chess. As I'm new to this type of approach, it was very helpful to reference other material but since that other material is also playing chess most of the work is just reproducing that work. 

Goals:
-Have a framework for NN-guided MCTS
-Implement a chess variant (duck chess/crazy house)
-Convert another goal into a "game" for the algorithm to play (much like AlphaTensor)
  -For example, can sorting algorithms be converted into a game? Find a sorting algorithm that works in place
  
  
Sorting Game:
-Convert a 1xn grid of numbers into a 1xn grid of sorted numbers
-Allowable moves: 
  -Switch any two elements
  -Pivoting? (arguably pivoting is just switching elements position based off another element)

