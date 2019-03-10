class Square:
    WHITE = 'w'
    BLACK = 'b'

    def __init__(self, color, piece=None):
        self.color = color
        self.piece = piece

    def is_white(self):
       return True if self.color == self.WHITE else False
