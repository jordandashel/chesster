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
        self.queen_side = True

    def abv_name(self, in_unicode=True):
        if self.name == self.PAWN:
            if in_unicode:
                return '\u2659 ' if self.is_white else '\u265F '
            else:
                return 'P '
        elif self.name == self.ROOK:
            if in_unicode:
                return '\u2656 ' if self.is_white else '\u265C '
            else:
                return 'R '
        elif self.name == self.KNIGHT:
            if in_unicode:
                return '\u2658 ' if self.is_white else '\u265E '
            else:
                return 'Kt'
        elif self.name == self.BISHOP:
            if in_unicode:
                return '\u2657 ' if self.is_white else '\u265D '
            else:
                return 'B '
        elif self.name == self.QUEEN:
            if in_unicode:
                return '\u2655 ' if self.is_white else '\u265B '
            else:
                return 'Q '
        elif self.name == self.KING:
            if in_unicode:
                return '\u2654 ' if self.is_white else '\u265A '
            else:
                return 'K '
        else:
            return '  ' 
