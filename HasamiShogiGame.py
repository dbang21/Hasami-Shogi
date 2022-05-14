# Author: Dionne Bang
# Date: 12/3/21
# Description: Write a class named HasamiShogiGame for playing an abstract board game called hasami shogi.

class HasamiShogiGame:
    """
    HasamiShogiGame class to represent Hasami Shogi game, played by two players, Red and Black. Black always starts first. Returns True if is a valid move, updates board state, current player, and game state (unfinished if it is ongoing, winner if game is completed).
    """
    def __init__(self):
        """Takes no parameters. Initializes the board with all the rows and player pieces in correct positions, game state, active player, number of pieces captured per player, and what occupies what square on the board. All data members are private."""
        self._board =[['R','R','R','R','R','R','R','R','R'],['.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.'],['B','B','B','B','B','B','B','B','B']]
        self._game_state = 'UNFINISHED'
        self._active_player = 'BLACK'
        self._num_captured_pieces = 0
        self._captured_red_pieces = 0
        self._captured_black_pieces = 0
        self._square_occupant = None
        self._move_validity = None
        self._previous_square = None
        self._current_square = None

    def print_board(self):
        """Prints the current board state."""
        columns = ['1','2','3','4','5','6','7','8','9']
        print(' ', *columns)
        print('a', *self._board[0])
        print('b', *self._board[1])
        print('c', *self._board[2])
        print('d', *self._board[3])
        print('e', *self._board[4])
        print('f', *self._board[5])
        print('g', *self._board[6])
        print('h', *self._board[7])
        print('i', *self._board[8])

    def get_game_state(self):
        """Returns the current state of the game."""
        return self._game_state

    def set_game_state(self):
        """ sets the current state of the game. """
        if self._num_captured_pieces < 8:
            self._game_state = 'UNFINISHED'

        if self._num_captured_pieces >= 8:
            if self._active_player == 'RED':
                self._game_state = 'RED_WON'
            else:
                self._game_state = 'BLACK_WON'

    def get_active_player(self):
        """Returns whose turn it is."""
        return self._active_player

    def set_active_player(self):
        """ sets new active player. """
        if self._game_state == 'UNFINISHED' and self._move_validity==True:
            if self._active_player == 'RED':
                self._active_player = 'BLACK'
            else:
                self._active_player = 'RED'
        elif self._game_state == 'UNFINISHED' and self._move_validity==False:
            return self._active_player
        else:
            return self._game_state

    def get_num_captured_pieces(self, captured):
        """Returns the number of pieces of that color that have been captured."""
        if captured == 'BLACK':
            self._num_captured_pieces=self._captured_black_pieces
            return self._num_captured_pieces
        if captured == 'RED':
            self._num_captured_pieces=self._captured_red_pieces
            return self._num_captured_pieces

    def set_num_captured_pieces(self, captured):
        """Sets the number of pieces of that color that have been captured."""
        count=0
        square_row, square_col = self._current_square
        row = ord(square_row) - 97
        col = int(square_col) - 1
        if captured == 'RED':
            self._num_captured_pieces = self._captured_red_pieces
            # check 'to' square sides
            if (col-1)>=0 and self._board[row][col-1] =='R':
                col_1=col
                # keep checking row until it hits black piece or empty square
                while self._board[row][col - 1] == 'R' and col>1:
                    col-=1
                    count+=1
                if self._board[row][col - 1] == '.':
                    self._num_captured_pieces += 0
                    count=0
                    col=col_1
                elif self._board[row][col - 1] == 'B':
                    while col!=col_1:
                        self._board[row][col] = '.'
                        col +=1
                    self._num_captured_pieces += count
                    count=0
                else:
                    count=0
                    col=col_1
                    self._num_captured_pieces += 0
            if (col+1)<9 and self._board[row][col+1] =='R':
                col_1=col
                # keep checking row until it hits black piece or empty square
                while self._board[row][col+1] == 'R' and (col+1)<8:
                    col+=1
                    count+=1
                if self._board[row][col+1] == '.':
                    self._num_captured_pieces += 0
                    count=0
                    col=col_1
                elif self._board[row][col+1] == 'B':
                    while col!=col_1:
                        self._board[row][col] = '.'
                        col -=1
                    self._num_captured_pieces += count
                    count=0
                else:
                    count = 0
                    col=col_1
                    self._num_captured_pieces += 0
            if (row-1)>=0 and self._board[row-1][col] =='R':
                row_1=row
                # keep checking column until it hits black piece or empty square
                while self._board[row-1][col] == 'R'and row>1:
                    row -= 1
                    count += 1
                if self._board[row-1][col] == '.':
                    self._num_captured_pieces += 0
                    count=0
                    row=row_1
                elif self._board[row-1][col] == 'B':
                    while row!=row_1:
                        self._board[row][col] = '.'
                        row +=1
                    self._num_captured_pieces += count
                    count=0
                else:
                    count = 0
                    row=row_1
                    self._num_captured_pieces += 0
            if (row+1)<9 and self._board[row+1][col] =='R':
                row_1=row
                # keep checking row until it hits black piece or empty square
                while self._board[row+1][col] == 'R' and (row+1)<8:
                    row+=1
                    count+=1
                if self._board[row+1][col] == '.':
                    self._num_captured_pieces += 0
                    count=0
                    row=row_1
                elif self._board[row+1][col] == 'B':
                    while row!=row_1:
                        self._board[row][col] = '.'
                        row -=1
                    self._num_captured_pieces += count
                    count=0
                else:
                    count = 0
                    row=row_1
                    self._num_captured_pieces += 0
            self._captured_red_pieces = self._num_captured_pieces
            return

        if captured == 'BLACK':
            self._num_captured_pieces = self._captured_black_pieces
            # check 'to' square sides
            if (col-1)>=0 and self._board[row][col-1] =='B':
                col_1=col
                # keep checking row until it hits black piece or empty square
                while self._board[row][col - 1] == 'B' and col>1:
                    col-=1
                    count+=1
                if self._board[row][col - 1] == '.':
                    self._num_captured_pieces += 0
                    count=0
                    col=col_1
                elif self._board[row][col - 1] == 'R':
                    while col!=col_1:
                        self._board[row][col] = '.'
                        col +=1
                    self._num_captured_pieces += count
                    count=0
                else:
                    count = 0
                    col=col_1
                    self._num_captured_pieces += 0
            if (col+1)<9 and self._board[row][col+1] =='B':
                col_1=col
                # keep checking row until it hits black piece or empty square
                while self._board[row][col+1] == 'B' and (col+1)<8:
                    col+=1
                    count+=1
                if self._board[row][col+1] == '.':
                    self._num_captured_pieces += 0
                    count=0
                    col=col_1
                elif self._board[row][col+1] == 'R':
                    while col!=col_1:
                        self._board[row][col] = '.'
                        col -=1
                    self._num_captured_pieces += count
                    count=0
                else:
                    count = 0
                    col=col_1
                    self._num_captured_pieces += 0
            if (row-1)>=0 and self._board[row-1][col] =='B':
                row_1=row
                # keep checking column until it hits black piece or empty square
                while self._board[row-1][col] == 'B'and row>1:
                    row -= 1
                    count += 1
                if self._board[row-1][col] == '.':
                    self._num_captured_pieces += 0
                    count=0
                    row=row_1
                elif self._board[row-1][col] == 'R':
                    while row!=row_1:
                        self._board[row][col] = '.'
                        row +=1
                    self._num_captured_pieces += count
                    count=0
                else:
                    count = 0
                    row=row_1
                    self._num_captured_pieces += 0
            if (row+1)<9 and self._board[row+1][col] =='B':
                row_1=row
                # keep checking row until it hits black piece or empty square
                while self._board[row+1][col] == 'B' and (row+1)<8:
                    row+=1
                    count+=1
                if self._board[row+1][col] == '.':
                    self._num_captured_pieces += 0
                    count=0
                    row=row_1
                elif self._board[row+1][col] == 'R':
                    while row!=row_1:
                        self._board[row][col] = '.'
                        row -=1
                    self._num_captured_pieces += count
                    count=0
                else:
                    count = 0
                    row=row_1
                    self._num_captured_pieces += 0
            else:
                self._num_captured_pieces += 0
            self._captured_black_pieces = self._num_captured_pieces
            return

    def check_corner_capture(self, captured):
        square_row, square_col = self._current_square
        row = ord(square_row) - 97
        col = int(square_col) - 1
        #if to capture is red
        if captured == 'RED':
            self._num_captured_pieces = self._captured_red_pieces
            #check sides of current square for red
            if (col-1)>=0 and self._board[row][col-1] =='R':
                #check if side is in corners
                #check if other side of corner has a black
                if row==0 and (col - 1)==0:
                    if self._board[1][0]=='B':
                        # capture corner
                        self._board[0][0] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
                if row==8 and (col - 1)==0:
                    if self._board[7][0]=='B':
                        # capture corner
                        self._board[8][0] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
            if (col+1)<9 and self._board[row][col+1] =='R':
                #check if side is in corners
                #check if other side of corner has a black
                if row==0 and (col+1)==8:
                    if self._board[1][8]=='B':
                        # capture corner
                        self._board[0][8] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
                if row==8 and (col+1)==8:
                    if self._board[7][8]=='B':
                        # capture corner
                        self._board[8][8] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
            if (row-1)>=0 and self._board[row-1][col] =='R':
                #check if side is in corners
                #check if other side of corner has a black
                if (row-1)==0 and col==0:
                    if self._board[0][1]=='B':
                        # capture corner
                        self._board[0][0] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
                if (row-1)==0 and col==8:
                    if self._board[0][7]=='B':
                        # capture corner
                        self._board[0][8] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
            if (row+1)<9 and self._board[row+1][col] =='R':
                #check if side is in corners
                #check if other side of corner has a black
                if (row+1)==8 and col==0:
                    if self._board[8][1]=='B':
                        # capture corner
                        self._board[8][0] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
                if (row+1)==8 and col==8:
                    if self._board[8][7]=='B':
                        # capture corner
                        self._board[8][8] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
            self._captured_red_pieces = self._num_captured_pieces
            return
        #if to capture is black
        if captured == 'BLACK':
            self._num_captured_pieces = self._captured_black_pieces
            if (col-1)>=0 and self._board[row][col-1] =='B':
                #check if side is in corners
                if row==0 and (col - 1)==0:
                    if self._board[1][0]=='R':
                        # capture corner
                        self._board[0][0] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
                if row==8 and (col - 1)==0:
                    if self._board[7][0]=='R':
                        # capture corner
                        self._board[8][0] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
            if (col+1)<9 and self._board[row][col+1] =='B':
                #check if side is in corners
                if row==0 and (col+1)==8:
                    if self._board[1][8]=='R':
                        # capture corner
                        self._board[0][8] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
                if row==8 and (col+1)==8:
                    if self._board[7][8]=='R':
                        # capture corner
                        self._board[8][8] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
            if (row-1)>=0 and self._board[row-1][col] =='B':
                #check if side is in corners
                if (row-1)==0 and col==0:
                    if self._board[0][1]=='R':
                        # capture corner
                        self._board[0][0] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
                if (row-1)==0 and col==8:
                    if self._board[0][7]=='R':
                        # capture corner
                        self._board[0][8] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
            if (row+1)<9 and self._board[row+1][col] =='B':
                #check if side is in corners
                if (row+1)==8 and col==0:
                    if self._board[8][1]=='R':
                        # capture corner
                        self._board[8][0] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
                if (row+1)==8 and col==8:
                    if self._board[8][7]=='R':
                        # capture corner
                        self._board[8][8] = '.'
                        self._num_captured_pieces+=1
                    else:
                        return
            self._captured_black_pieces = self._num_captured_pieces
            return

    def make_move(self, from_str, to_str):
        """Returns True or False based on whether move is possible, moves piece and captures accordingly, then updates game state and player’s turn."""
        self._previous_square = from_str
        self._current_square = to_str
        from_row, from_col = from_str
        to_row, to_col = to_str
        # check if black is occupying the from square
        if self.get_game_state()=='UNFINISHED':
            if self._active_player == 'BLACK' and self.get_square_occupant(from_str)=='BLACK':
                # check if it's possible to move to 'to' square:
                if self.get_square_occupant(to_str)=='NONE':
                    # path is clear
                    # direction is horizontal or vertical
                    if from_row == to_row and from_col != to_col:
                        orig_from=from_col
                        from_col=int(from_col)
                        to_col=int(to_col)
                        while from_col != to_col:
                            if from_col>to_col:
                                from_col=from_col-1
                                square = from_row, str(from_col)
                                if self.get_square_occupant(square) == 'NONE':
                                    from_col-=1
                                else:
                                    return False
                                break
                            elif from_col<to_col:
                                from_col=from_col+1
                                square = from_row, str(from_col)
                                if self.get_square_occupant(square) == 'NONE':
                                    from_col+=1
                                else:
                                    return False
                                break
                            else:
                                self._move_validity = False
                                return False
                        to_row = ord(to_row) - 97
                        to_col = int(to_col) - 1
                        from_row = ord(from_row) - 97
                        from_col = int(orig_from) - 1
                        self._board[to_row][to_col] = 'B'
                        self._board[from_row][from_col] = '.'
                        self.set_num_captured_pieces('RED')
                        self.check_corner_capture('RED')
                        self._move_validity = True
                        self.set_game_state()
                        self.set_active_player()
                        return True

                    elif from_col == to_col and from_row != to_row:
                        from_ind = ord(from_row) - 97
                        to_ind = ord(to_row) - 97
                        while from_ind != to_ind:
                            if from_ind>to_ind:
                                square = chr(from_ind + 96), from_col
                                if self.get_square_occupant(square) == 'NONE':
                                    from_ind-=1
                                else:
                                    self._move_validity = False
                                    return False
                            elif from_ind<to_ind:
                                square = chr(from_ind + 98), from_col
                                if self.get_square_occupant(square) == 'NONE':
                                    from_ind+=1
                                else:
                                    self._move_validity = False
                                    return False
                            else:
                                self._move_validity = False
                                return False
                        to_row = to_ind
                        to_col = int(to_col) - 1
                        from_row= ord(from_row) - 97
                        from_col=int(from_col) - 1
                        self._board[to_row][to_col] = 'B'
                        self._board[from_row][from_col] = '.'
                        self.set_num_captured_pieces('RED')
                        self.check_corner_capture('RED')
                        self._move_validity = True
                        self.set_game_state()
                        self.set_active_player()
                        return True

                    else:
                        self._move_validity = False
                        return False
                else:
                    self._move_validity = False
                    return False

            elif self._active_player == 'RED' and self.get_square_occupant(from_str)=='RED':
                if self.get_square_occupant(to_str)=='NONE':
                    # path is clear
                    # direction is horizontal or vertical
                    if from_row == to_row and from_col != to_col:
                        orig_from=from_col
                        from_col=int(from_col)
                        to_col=int(to_col)
                        while from_col != to_col:
                            if from_col>to_col:
                                from_col=from_col-1
                                square = from_row, str(from_col)
                                if self.get_square_occupant(square) == 'NONE':
                                    from_col-=1
                                else:
                                    return False
                                break
                            elif from_col<to_col:
                                from_col=from_col+1
                                square = from_row, str(from_col)
                                if self.get_square_occupant(square) == 'NONE':
                                    from_col+=1
                                else:
                                    return False
                                break
                            else:
                                self._move_validity = False
                                return False
                        to_row = ord(to_row) - 97
                        to_col = int(to_col) - 1
                        from_row = ord(from_row) - 97
                        from_col = int(orig_from) - 1
                        self._board[to_row][to_col] = 'R'
                        self._board[from_row][from_col] = '.'
                        self.set_num_captured_pieces('BLACK')
                        self.check_corner_capture('BLACK')
                        self._move_validity = True
                        self.set_game_state()
                        self.set_active_player()
                        return True

                    elif from_col == to_col and from_row != to_row:
                        from_ind = ord(from_row) - 97
                        to_ind = ord(to_row) - 97
                        while from_ind != to_ind:
                            if from_ind>to_ind:
                                square = chr(from_ind + 96), from_col
                                if self.get_square_occupant(square) == 'NONE':
                                    from_ind-=1
                                else:
                                    self._move_validity = False
                                    return False
                            elif from_ind<to_ind:
                                square = chr(from_ind + 98), from_col
                                if self.get_square_occupant(square) == 'NONE':
                                    from_ind+=1
                                else:
                                    self._move_validity = False
                                    return False
                            else:
                                self._move_validity = False
                                return False
                        to_row = to_ind
                        to_col = int(to_col) - 1
                        from_row= ord(from_row) - 97
                        from_col=int(from_col) - 1
                        self._board[to_row][to_col] = 'R'
                        self._board[from_row][from_col] = '.'
                        self.set_num_captured_pieces('BLACK')
                        self.check_corner_capture('BLACK')
                        self._move_validity = True
                        self.set_game_state()
                        self.set_active_player()
                        return True
                    else:
                        self._move_validity = False
                        return False
                else:
                    self._move_validity = False
                    return False
            else:
                self._move_validity = False
                return False
        else:
            self._move_validity = False
            return False

    def get_square_occupant(self, square):
        """Returns who is occupying a specified square."""
        square_row, square_col = square
        row=ord(square_row)-97
        col=int(square_col)-1
        if row>=0 and row<9:
            if col>=0 and col<9:
                occupant = self._board[row][col]
                if occupant == 'B':
                    self._square_occupant = 'BLACK'
                if occupant == 'R':
                    self._square_occupant = 'RED'
                if occupant == '.':
                    self._square_occupant = 'NONE'
                return self._square_occupant
            else:
                return "Not a valid board square."
        else:
            return "Not a valid board square."

def main():
    game = HasamiShogiGame()

    move_result = game.make_move('i9', 'b9')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("RED"))

    move_result = game.make_move('a8', 'h8')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("BLACK"))

    move_result = game.make_move('i7', 'b7')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("RED"))

    move_result = game.make_move('a4', 'h4')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("BLACK"))

    move_result = game.make_move('i3', 'b3')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("RED"))

    move_result = game.make_move('a2', 'h2')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("BLACK"))

    move_result = game.make_move('b3', 'b4')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("RED"))

    move_result = game.make_move('h8', 'h7')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("BLACK"))

    move_result = game.make_move('b4', 'a4')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("RED"))

    move_result = game.make_move('h4', 'h3')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("BLACK"))

    move_result = game.make_move('b7', 'b8')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("RED"))

    move_result = game.make_move('h3', 'i3')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("BLACK"))

    move_result = game.make_move('b8', 'a8')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("RED"))

    move_result = game.make_move('h7', 'h9')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("BLACK"))

    move_result = game.make_move('b9', 'b1')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("RED"))

    move_result = game.make_move('h9', 'i9')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("BLACK"))

    move_result = game.make_move('a8', 'h8')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("RED"))

    move_result = game.make_move('h2', 'h7')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("BLACK"))

    move_result = game.make_move('i2', 'a2')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("RED"))

    move_result = game.make_move('h7', 'i7')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("BLACK"))

    move_result = game.make_move('h8', 'i8')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("RED"))

    move_result = game.make_move('i3', 'i6')
    print(move_result)
    print(game.get_active_player())
    print(game.get_num_captured_pieces("BLACK"))



    print(game.get_game_state())
    game.print_board()



if __name__ == '__main__':
    main()