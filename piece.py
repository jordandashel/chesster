class Piece:
    PAWN = 'pawn'
    ROOK = 'rook'
    KNIGHT = 'knight'
    BISHOP = 'bishop'
    QUEEN = 'queen'
    KING = 'king'

    def __init__(self):
        self.name = ''
        self.is_white = True

    def abv_name(self, in_unicode=True):
        color = 'w' if self.is_white else 'b'
        if self.name == self.PAWN:
            if in_unicode:
                return '\u2659 ' if self.is_white else '\u265F '
            else:
                return color + 'P '
        elif self.name == self.ROOK:
            if in_unicode:
                return '\u2656 ' if self.is_white else '\u265C '
            else:
                return color + 'R '
        elif self.name == self.KNIGHT:
            if in_unicode:
                return '\u2658 ' if self.is_white else '\u265E '
            else:
                return color + 'Kt'
        elif self.name == self.BISHOP:
            if in_unicode:
                return '\u2657 ' if self.is_white else '\u265D '
            else:
                return color + 'B '
        elif self.name == self.QUEEN:
            if in_unicode:
                return '\u2655 ' if self.is_white else '\u265B '
            else:
                return color + 'Q '
        elif self.name == self.KING:
            if in_unicode:
                return '\u2654 ' if self.is_white else '\u265A '
            else:
                return color + 'K '
        else:
            return '   ' 
