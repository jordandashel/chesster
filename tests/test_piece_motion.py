import unittest
from piece import Piece
from piece import Motion, PawnMotion, RookMotion, BishopMotion, KnightMotion, KingMotion, QueenMotion

class MotionTestCase(unittest.TestCase):
    def test_indexed_file(self):
        self.assertEqual(0, Motion.indexed_file('a'))
        self.assertEqual(7, Motion.indexed_file('h'))

    def test_filed_index(self):
        self.assertEqual('a', Motion.filed_index(0))
        self.assertEqual('h', Motion.filed_index(7))

    def test_convert_to_cart_coords(self):
        self.assertEqual((0, 0), Motion.convert_to_cart_coords('a1'))
        self.assertEqual((3, 6), 
                Motion.convert_to_cart_coords(('d', 7)))

    def test_convert_to_notation(self):
        self.assertEqual(('a', 1), Motion.convert_to_notation(0, 0))

class RookMotionTestCase(unittest.TestCase):
    def test_rook_intermediate_squares(self):
        interm_sqs = RookMotion.intermediate_squares(('a', 1), ('a', 8))
        self.assertEqual(interm_sqs, [
            ('a', 2), 
            ('a', 3),
            ('a', 4),
            ('a', 5),
            ('a', 6),
            ('a', 7)
        ])
        interm_sqs = RookMotion.intermediate_squares(('a',1), ('g', 1))
        self.assertEqual(interm_sqs, [
            ('b', 1),
            ('c', 1),
            ('d', 1),
            ('e', 1),
            ('f', 1)
        ])

        interm_sqs = RookMotion.intermediate_squares(('g',1), ('a', 1))
        self.assertEqual(interm_sqs, [
            ('f', 1),
            ('e', 1),
            ('d', 1),
            ('c', 1),
            ('b', 1)
        ])

    def test_rook_intermediate_squares_will_be_0(self):
        interm_sqs = RookMotion.intermediate_squares(('a', 1), ('a', 2))
        self.assertEqual(0, len(interm_sqs))


    def test_valid_move(self):
        can_move_to_square = RookMotion.valid_move('a1', 'a8')
        self.assertTrue(can_move_to_square)
        can_move_to_square = RookMotion.valid_move('a1', 'h8')
        self.assertFalse(can_move_to_square)

    def test_valid_move__black_turn(self):
        # can_move_to_square = RookMotion.valid_move('a1', 
        pass

class BishopMotionTestCase(unittest.TestCase):
    def test_valid_move(self):
        can_move_to_square = BishopMotion.valid_move('a1', 'h8')
        self.assertTrue(can_move_to_square)
        can_move_to_square = BishopMotion.valid_move('a8', 'h1')
        self.assertTrue(can_move_to_square)
        can_move_to_square = BishopMotion.valid_move('a1', 'a8')
        self.assertFalse(can_move_to_square)
        can_move_to_square = BishopMotion.valid_move('d6', 'g3')
        self.assertTrue(can_move_to_square)

    def test_bishop_intermediate_squares_will_be_0(self):
        interm_sqs = BishopMotion.intermediate_squares(('a', 1), ('b', 2))
        self.assertEqual(0, len(interm_sqs))

    def test_bishop_intermediate_squares(self):
        interm_sqs = BishopMotion.intermediate_squares(('a', 1), ('h', 8))
        self.assertEqual(interm_sqs, [
            ('b', 2),
            ('c', 3),
            ('d', 4),
            ('e', 5),
            ('f', 6),
            ('g', 7)
        ])
        interm_sqs = BishopMotion.intermediate_squares(('b', 7), ('g', 2))
        self.assertEqual(interm_sqs, [
            ('c', 6),
            ('d', 5),
            ('e', 4),
            ('f', 3),
        ])
        
class QueenMotionTestCase(unittest.TestCase):
    def test_valid_move(self):
        can_move_to_square = QueenMotion.valid_move('a1', 'h8')
        self.assertTrue(can_move_to_square)
        can_move_to_square = QueenMotion.valid_move('a1', 'h7')
        self.assertFalse(can_move_to_square)

    def test_queen_intermediate_squares(self):
        interm_sqs = QueenMotion.intermediate_squares(('a', 1), ('h', 8))
        self.assertEqual(interm_sqs, [
            ('b', 2),
            ('c', 3),
            ('d', 4),
            ('e', 5),
            ('f', 6),
            ('g', 7)
        ])
        interm_sqs = QueenMotion.intermediate_squares(('a', 1), ('a', 8))
        self.assertEqual(interm_sqs, [
            ('a', 2), 
            ('a', 3),
            ('a', 4),
            ('a', 5),
            ('a', 6),
            ('a', 7)
        ])
        interm_sqs = QueenMotion.intermediate_squares(('a',1), ('g', 1))
        self.assertEqual(interm_sqs, [
            ('b', 1),
            ('c', 1),
            ('d', 1),
            ('e', 1),
            ('f', 1)
        ])

class KingMotionTestCase(unittest.TestCase):
    def test_valid_move(self):
        can_move_to_square = KingMotion.valid_move('a1', 'b2')
        self.assertTrue(can_move_to_square)
        can_move_to_square = KingMotion.valid_move('a1', 'a8')
        self.assertFalse(can_move_to_square)

    def test_king_intermediate_squares(self):
        interm_sqs = KingMotion.intermediate_squares(('a', 1), ('a', 2))
        self.assertEqual(interm_sqs, [ ])
        with self.assertRaises(AssertionError):
            interm_sqs = KingMotion.intermediate_squares(('a', 1), ('a', 8))


class KnightMotionTestCase(unittest.TestCase):
    def test_valid_move(self):
        can_move_to_square = KnightMotion.valid_move('a1', 'b3')
        self.assertTrue(can_move_to_square)
        can_move_to_square = KnightMotion.valid_move('e4', 'd2')
        self.assertTrue(can_move_to_square)
        can_move_to_square = KnightMotion.valid_move('e4', 'e5')
        self.assertFalse(can_move_to_square)

    def test_king_intermediate_squares(self):
        interm_sqs = KnightMotion.intermediate_squares(('a', 1), ('c', 2))
        self.assertEqual(interm_sqs, [ ])
        with self.assertRaises(AssertionError):
            interm_sqs = KingMotion.intermediate_squares(('a', 1), ('a', 8))


class PawnMotionTestCase(unittest.TestCase):
    def test_valid_first_move(self):
        can_move_to_square = PawnMotion.valid_move('a2', 'a3', Piece.WHITE, first_move=True)
        self.assertTrue(can_move_to_square)
        can_move_to_square = PawnMotion.valid_move('e2', 'e4', Piece.WHITE, first_move=True)
        self.assertTrue(can_move_to_square)
        can_move_to_square = PawnMotion.valid_move('a2', 'a5', Piece.WHITE, first_move=True)
        self.assertFalse(can_move_to_square)

    def test_capture(self):
        can_move_to_square = PawnMotion.valid_move('a3', 'b4', Piece.WHITE, capture=True)
        self.assertTrue(can_move_to_square)
        can_move_to_square = PawnMotion.valid_move('a3', 'c4', Piece.WHITE, capture=True)
        self.assertFalse(can_move_to_square)

    def test_valid_move(self):
        can_move_to_square = PawnMotion.valid_move('c3', 'c4', Piece.WHITE)
        self.assertTrue(can_move_to_square)
        can_move_to_square = PawnMotion.valid_move('c3', 'c5', Piece.WHITE)
        self.assertFalse(can_move_to_square)

    def test_valid_capture(self):
        can_move_to_square = PawnMotion.valid_move('c3', 'd4', Piece.WHITE, capture=True)
        self.assertTrue(can_move_to_square)
        can_move_to_square = PawnMotion.valid_move('c3', 'c4', Piece.WHITE, capture=True)
        self.assertFalse(can_move_to_square)

    def test_black_side_moves(self):
        can_move_to_square = PawnMotion.valid_move('a7', 'a6', Piece.BLACK)
        self.assertTrue(can_move_to_square)

