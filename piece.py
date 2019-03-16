from motion import *

class Piece:
    WHITE = 'w'
    BLACK = 'b'

    PAWN = 'pawn'
    ROOK = 'rook'
    KNIGHT = 'knight'
    BISHOP = 'bishop'
    QUEEN = 'queen'
    KING = 'king'

    def __init__(self):
        self.name = ''
        self.color = ''

    def is_white(self):
        return True if self.color == self.WHITE else False

    def motion(self):
        if self.name == self.PAWN:
            return PawnMotion
        if self.name == self.ROOK:
            return RookMotion
        if self.name == self.KNIGHT:
            return KnightMotion
        if self.name == self.BISHOP:
            return BishopMotion
        if self.name == self.QUEEN:
            return QueenMotion
        if self.name == self.KING:
            return KingMotion

    def abv_name(self, in_unicode=True):
        if self.name == self.PAWN:
            if in_unicode:
                return '\u2659 ' if self.is_white() else '\u265F '
            else:
                return self.color + 'P '
        elif self.name == self.ROOK:
            if in_unicode:
                return '\u2656 ' if self.is_white() else '\u265C '
            else:
                return self.color + 'R '
        elif self.name == self.KNIGHT:
            if in_unicode:
                return '\u2658 ' if self.is_white() else '\u265E '
            else:
                return self.color + 'Kt'
        elif self.name == self.BISHOP:
            if in_unicode:
                return '\u2657 ' if self.is_white() else '\u265D '
            else:
                return self.color + 'B '
        elif self.name == self.QUEEN:
            if in_unicode:
                return '\u2655 ' if self.is_white() else '\u265B '
            else:
                return self.color + 'Q '
        elif self.name == self.KING:
            if in_unicode:
                return '\u2654 ' if self.is_white() else '\u265A '
            else:
                return self.color + 'K '
        else:
            return '   ' 
