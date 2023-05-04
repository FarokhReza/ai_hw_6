from Tile import Tile
from Board import Board
class Agent:

    MIN_VALUE = -1000000
    MAX_VALUE= 1000000

    def __init__(self, game, color, max_depth):
        self.game = game
        self.color = color
        self.max_depth = max_depth
    

    def do_min_max(self, current_board):
        move, value = self.max_value(current_board, self.color, 0, self.MIN_VALUE, self.MAX_VALUE)
 
        return move
    

    def max_value(self, current_board, current_color, depth, alpha, beta):
        # if depth == self.max_depth or self.game.check_terminal(current_board, current_color):
        #     return None, self.game.evaluate(current_board, current_color, -100000)
        
        if self.game.check_terminal(current_board, current_color):
            return None, self.game.evaluate(current_board, current_color, -1000)
            
        # estimate the evaluate func score in maximum depth
        if depth == self.max_depth:
            return None, self.game.evaluate(current_board, current_color)
        
        value = float("-inf")
        best_move = None
        moves = self.game.generate_all_possible_moves(current_board, current_color)


        for move in moves:
            new_board = current_board.next_board(current_color, move)
            _, new_value = self.min_value(new_board, self.game.opponent(current_color)  ,depth+1,alpha, beta)
            if new_value > value:
                best_move = move
                value = new_value
            
            if value >= beta:
                break
                # return best_move, value

            alpha = max(alpha, value)

        return best_move, value

   
    def min_value(self, current_board, current_color, depth, alpha, beta):
        if self.game.check_terminal(current_board, current_color):
            return None, self.game.evaluate(current_board, current_color, -1000)
        
        if depth == self.max_depth:
            return None, self.game.evaluate(current_board, current_color)

        value = float("+inf")
        best_move = None
        moves = self.game.generate_all_possible_moves(current_board, current_color)
        for move in moves:
            new_board = current_board.next_board(current_color, move)
            _, new_value = self.max_value(new_board, current_color, depth+1, alpha, beta)
            
            if new_value < value:
                best_move = move
                value = new_value
            if value <= alpha:
                # return best_move, value
                break
            beta = min(beta, value)
        return best_move, value
