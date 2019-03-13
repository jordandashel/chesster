import unittest
from motion import *

class MotionTestCase(unittest.TestCase):
    def test_motion(self):
        # motion = RookMotion()
        can_move_to_square = RookMotion.valid_move('a1', 'a8')
        self.assertTrue(can_move_to_square)
        can_move_to_square = RookMotion.valid_move('a1', 'h8')
        self.assertFalse(can_move_to_square)

    def test_further_north(self):
        self.assertFalse(Motion.further_north(1, 8))
        self.assertTrue(Motion.further_north(4, 2))

    def test_further_south(self):
        self.assertFalse(Motion.further_south(8, 1))
        self.assertTrue(Motion.further_south(2, 4))
        
    def test_further_west(self):
        self.assertTrue(Motion.further_west('a', 'h'))
        self.assertFalse(Motion.further_west('e', 'd'))

    def test_further_east(self):
        self.assertFalse(Motion.further_east('a', 'h'))
        self.assertTrue(Motion.further_east('e', 'd'))

    def test_indexed_file(self):
        self.assertEqual(0, Motion.indexed_file('a'))
        self.assertEqual(7, Motion.indexed_file('h'))

    def test_filed_index(self):
        self.assertEqual('a', Motion.filed_index(0))
        self.assertEqual('h', Motion.filed_index(7))

    def test_rook_intermediate_squares(self):
        interm_sqs = RookMotion.intermediate_squares(('a', 1), ('a', 8))
        self.assertEqual(interm_sqs, [
            ('a', 2), 
            ('a', 3),
            ('a', 4),
            ('a', 5),
            ('a', 6),
            ('a', 7),
            ('a', 8)
        ])
        interm_sqs = RookMotion.intermediate_squares(('a',1), ('g', 1))
        self.assertEqual(interm_sqs, [
            ('b', 1),
            ('c', 1),
            ('d', 1),
            ('e', 1),
            ('f', 1),
            ('g', 1)
        ])

        interm_sqs = RookMotion.intermediate_squares(('g',1), ('a', 1))
        self.assertEqual(interm_sqs, [
            ('f', 1),
            ('e', 1),
            ('d', 1),
            ('c', 1),
            ('b', 1),
            ('a', 1)
        ])


class MotionLanguageTestCase(unittest.TestCase):
    def test_initialize_ml(self):
        test_rook_motion = 'N(+-)*'
        rook_motion = MotionLanguage(test_rook_motion)
