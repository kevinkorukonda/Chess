


class Board:
    def __init__(self):
        self.board = {}
        self.empty()

    def empty(self):
        for col in 'abcdefgh':
            for row in '12345678':
                self.board[col + row] = ' '

    def set(self, pos, label):
        self.board[pos] = label

    def draw(self):

        def borders():
            print(' ', end='')
            for _ in range(8):
                print('+---', end='')
            print('+')

        def column_labels():
            print('   ', end='')
            for col in 'abcdefgh':
                print(f'{col}', end='   ')
            print()

        column_labels()

        borders()

        for row in '87654321':
            print(f'{row}', end='')
            for col in 'abcdefgh':
                print(f'| {self.board[col + row]} ', end='')
            print(f'|{row}')
            borders()

        column_labels()


class ChessPiece:
    def __init__(self, board, pos, color='white'):
        self.position = self.get_index(pos)
        self.color = color
        board.set(pos, self.get_name())

    def get_index(self, pos):
        return 'abcdefgh'.index(pos[0]), '12345678'.index(pos[1])

    def get_name(self):
        pass

    def moves(self, board):
        pass


class King(ChessPiece):
    def get_name(self):
        return 'K'

    def moves(self, board):
        coordinates = [(-1, - 1), (-1, 0), (-1, 1), (0, -1),
                       (0, 1), (1, -1), (1, 0), (1, 1)]
        col, row = self.position
        col_titles = 'abcdefgh'
        row_titles = '12345678'
        for col_inc, row_inc in coordinates:
            new_col = col + col_inc
            new_row = row + row_inc
            if 0 <= new_col < 8 and 0 <= new_row < 8:
                new_pos = f'{col_titles[new_col]}{row_titles[new_row]}'
                board.set(new_pos, 'x')


class Rook(ChessPiece):
    def get_name(self):
        return 'R'

    def moves(self, board):
        col, row = self.position
        col_titles = 'abcdefgh'
        row_titles = '12345678'
        for idx in range(8):
            if idx != row:
                current_pos = f'{col_titles[col]}{row_titles[idx]}'
                board.set(current_pos, 'x')
        for idx in range(8):
            if idx != col:
                current_pos = f'{col_titles[idx]}{row_titles[row]}'
                board.set(current_pos, 'x')


class Bishop(ChessPiece):
    def get_name(self):
        return 'B'

    def moves(self, board):
        col, row = self.position
        col_titles = 'abcdefgh'
        row_titles = '12345678'
        current_col, current_row = col, row
        while current_col < 8 and current_row >= 0:
            if current_col != col or current_row != row:
                current_pos = f'{col_titles[current_col]}{row_titles[current_row]}'
                board.set(current_pos, 'x')
            current_col += 1
            current_row -= 1
        current_col, current_row = col, row
        while current_col < 8 and current_row < 8:
            if current_col != col or current_row != row:
                current_pos = f'{col_titles[current_col]}{row_titles[current_row]}'
                board.set(current_pos, 'x')
            current_col += 1
            current_row += 1
        current_col, current_row = col, row
        while current_col >= 0 and current_row < 8:
            if current_col != col or current_row != row:
                current_pos = f'{col_titles[current_col]}{row_titles[current_row]}'
                board.set(current_pos, 'x')
            current_col -= 1
            current_row += 1
        current_col, current_row = col, row
        while current_col >= 0 and current_row >= 0:
            if current_col != col or current_row != row:
                current_pos = f'{col_titles[current_col]}{row_titles[current_row]}'
                board.set(current_pos, 'x')
            current_col -= 1
            current_row -= 1


class Queen(ChessPiece):
    def get_name(self):
        return 'Q'

    def moves(self, board):
        col, row = self.position
        col_titles = 'abcdefgh'
        row_titles = '12345678'
        current_col, current_row = col, row
        while current_col < 8 and current_row >= 0:
            if current_col != col or current_row != row:
                current_pos = f'{col_titles[current_col]}{row_titles[current_row]}'
                board.set(current_pos, 'x')
            current_col += 1
            current_row -= 1
        current_col, current_row = col, row
        while current_col < 8 and current_row < 8:
            if current_col != col or current_row != row:
                current_pos = f'{col_titles[current_col]}{row_titles[current_row]}'
            current_col += 1
            current_row += 1
            board.set(current_pos, 'x')
        current_col, current_row = col, row
        while current_col >= 0 and current_row < 8:
            if current_col != col or current_row != row:
                current_pos = f'{col_titles[current_col]}{row_titles[current_row]}'
                board.set(current_pos, 'x')
            current_col -= 1
            current_row += 1
        current_col, current_row = col, row
        while current_col >= 0 and current_row >= 0:
            if current_col != col or current_row != row:
                current_pos = f'{col_titles[current_col]}{row_titles[current_row]}'
                board.set(current_pos, 'x')
            current_col -= 1
            current_row -= 1
        for idx in range(8):
            if idx != row:
                current_pos = f'{col_titles[col]}{row_titles[idx]}'
                board.set(current_pos, 'x')
        for idx in range(8):
            if idx != col:
                current_pos = f'{col_titles[idx]}{row_titles[row]}'
                board.set(current_pos, 'x')


class Knight(ChessPiece):
    def get_name(self):
        return 'N'

    def moves(self, board):
        coordinates = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        col, row = self.position
        col_titles = 'abcdefgh'
        row_titles = '12345678'
        for col_inc, row_inc in coordinates:
            new_col = col + col_inc
            new_row = row + row_inc
            if 0 <= new_col < 8 and 0 <= new_row < 8:
                new_pos = f'{col_titles[new_col]}{row_titles[new_row]}'
                board.set(new_pos, 'x')


if __name__ == '__main__':
    b = Board()
    print('Welcome to the Chess Game!')
    b.draw()
    while True:
        piece = input('Enter a chess piece and its position or type X to exit: (Ex: Queen --> Qd4)\n').lower()
        if piece == 'x':
            print("Goodbye!")
            break
        if len(piece) == 3:
            initials, col, row = piece[0], piece[1], piece[2]
            if col in 'abcdefgh' and row in '12345678':
                if initials == 'k':
                    chess_piece = King(b, col + row)
                    chess_piece.moves(b)
                    b.draw()
                elif initials == 'q':
                    chess_piece = Queen(b, col + row)
                    chess_piece.moves(b)
                    b.draw()
                elif initials == 'r':
                    chess_piece = Rook(b, col + row)
                    chess_piece.moves(b)
                    b.draw()
                elif initials == 'n':
                    chess_piece = Knight(b, col + row)
                    chess_piece.moves(b)
                    b.draw()
                elif initials == 'b':
                    chess_piece = Bishop(b, col + row)
                    chess_piece.moves(b)
                    b.draw()

                b.empty()
    print('\n')



