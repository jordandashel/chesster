import unittest
from unittest import mock
from unittest.mock import MagicMock
from gamemaster import GameMaster
from piece import Piece

class GameMasterTestCase(unittest.TestCase):

    # Smoke Test
    def test_set_board__sets_board(self):
        gm = GameMaster()
        gm.chessboard = MagicMock()
        gm.set_board()
        assert gm.chessboard.set_board().called_once

    def test_gm_can_report_piece_at_square(self):
        gm = GameMaster()
        gm.set_board()
        piece = gm.what_piece('d2')
        self.assertEqual(piece.name, Piece.PAWN)


    def test_move_piece(self):
        gm = GameMaster()
        gm.set_board()
        pawn = gm.what_piece("D2")
        self.assertEqual(pawn.name, Piece.PAWN)
        self.assertEqual(pawn.color, Piece.WHITE)
        gm.move_piece("P-D4", Piece.WHITE)
        pawn = gm.what_piece("D4")
        self.assertEqual(pawn.name, Piece.PAWN)
        self.assertEqual(pawn.color, Piece.WHITE)


    def test_parse_input(self):
        result = GameMaster.parse_input('d2')
        self.assertEqual(result, ('d', 2))


