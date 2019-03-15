######################################################################
#
#   MOTION LANGUAGE:
#       
#       Files/ranks are largely ignored at this level. It is much
#       simpler to convert to cartesian coordinates and work with
#       those.
#
#       I /know/ there is an elegant regexe-esque language to be
#       developed here but that is for another day.
#       
#
######################################################################

import re
import math

# DUPLICATION -- find out where it belongs!!
files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ranks = [i for i in range(1, 9)]


class Motion:
    def __init__(self):
       pass
    
    def indexed_file(file_):
        i = 0
        while files[i] != file_:
            i += 1
        return i

    def filed_index(i):
        return files[i]

    def convert_to_cart_coords(file_rank):
        file_, rank = file_rank
        x = Motion.indexed_file(file_)
        y = int(rank) - 1
        return x, y

    def convert_to_notation(x, y):
        file_ = Motion.filed_index(x)
        rank = y + 1
        return file_, rank

class RookMotion(Motion):
    # allowable_movement = ('N(+/-)*', 'W(+/-)*')
    # capturing_movement = allowable_movement
    def valid_move(start, destination):
        x_1, y_1 = Motion.convert_to_cart_coords(start)
        x_2, y_2 = Motion.convert_to_cart_coords(destination)

        return x_1 == x_2 or y_1 == y_2

    def intermediate_squares(start, destination):
        if not RookMotion.valid_move(start, destination):
            return None

        assert RookMotion.valid_move(start, destination)
        x_1, y_1 = Motion.convert_to_cart_coords(start)
        x_2, y_2 = Motion.convert_to_cart_coords(destination)

        intermediate_sqs = []

        # vertical mvmt
        if x_1 == x_2:
            direction = 1 if y_1 < y_2 else -1
            y_1 += direction
            # y_2 += direction
            for i in range(y_1, y_2, direction):
                intermediate_sqs.append(
                        Motion.convert_to_notation(x_1, i))
        # lateral mvmt
        else:
            direction = 1 if x_1 < x_2 else -1
            x_1 += direction
            # x_2 += direction
            for i in range(x_1, x_2, direction):
                intermediate_sqs.append(
                        Motion.convert_to_notation(i, y_1))

        return intermediate_sqs

            
class KnightMotion(Motion):
    # allowable_movement = ('N(+/-)2,W(+/-)1', 'W(+/-)2,N(+/-)1')
    # capturing_movement = allowable_movement
    def valid_move(start, destination):
        x_1, y_1 = Motion.convert_to_cart_coords(start)
        x_2, y_2 = Motion.convert_to_cart_coords(destination)
        if math.fabs(x_1 - x_2) == 1 and math.fabs(y_2 - y_1) == 2:
            return True
        if math.fabs(x_1 - x_2) == 2 and math.fabs(y_2 - y_1) == 1:
            return True
        return False

    def intermediate_squares(start, destination):
        assert KnightMotion.valid_move(start, destination)
        return []

class BishopMotion(Motion):
    def valid_move(start, destination):
        x_1, y_1 = Motion.convert_to_cart_coords(start)
        x_2, y_2 = Motion.convert_to_cart_coords(destination)

        return math.fabs(x_1 - x_2) == math.fabs(y_1 - y_2)

    def intermediate_squares(start, destination):
        assert BishopMotion.valid_move(start, destination)
        x_1, y_1 = Motion.convert_to_cart_coords(start)
        x_2, y_2 = Motion.convert_to_cart_coords(destination)

        intermediate_sqs = []
        intermediate_x = []

        if x_1 > x_2:
            x_2 += 1 # don't report destination square
            while x_1 > x_2:
                x_1 -= 1
                intermediate_x.append(x_1)
        else:
            x_2 -= 1 # don't report destination square
            while x_1 < x_2:
                x_1 += 1
                intermediate_x.append(x_1)

        if y_1 > y_2:
            for x in intermediate_x:
                y_1 -= 1
                sq = Motion.convert_to_notation(x, y_1)
                intermediate_sqs.append(sq)
        else:
            for x in intermediate_x:
                y_1 += 1
                sq = Motion.convert_to_notation(x, y_1)
                intermediate_sqs.append(sq)

        return intermediate_sqs
                

class QueenMotion(Motion):
    # allowable_movement = ('N(+/-)*', 'W(+/-)*', 'NW(+/-)*', 'NE(+/-)*')
    # capturing_movement = allowable_movement
    def valid_move(start, destination):
        return RookMotion.valid_move(start, destination) \
                or BishopMotion.valid_move(start, destination)

    def intermediate_squares(start, destination):
        if RookMotion.valid_move(start, destination):
            return RookMotion.intermediate_squares(start, destination)
        elif BishopMotion.valid_move(start, destination):
            return BishopMotion.intermediate_squares(start, destination)
        else:
            return None

class KingMotion(Motion):
    # allowable_movement = ('N(+/-)1', 'W(+/-)1', 'NW(+/-)1', 'NE(+/-)1')
    # capturing_movement = allowable_movement
    def valid_move(start, destination):
        return QueenMotion.valid_move(start, destination) \
          and len(QueenMotion.intermediate_squares(start, destination)) == 0

    # King never has intermediate sqs bc she can only move one sq
    def intermediate_squares(start, destination):
        assert KingMotion.valid_move(start, destination)
        return []

class PawnMotion(Motion):
    def valid_move(start, destination, first_move=False, capture=False, en_passant=False):
        x_1, y_1 = Motion.convert_to_cart_coords(start)
        x_2, y_2 = Motion.convert_to_cart_coords(destination)
        if capture:
            return y_1 + 1 == y_2 and (x_1 + 1 == x_2 or x_1 - 1 == x_2)
        if first_move:
            return y_1 + 1 == y_2 or y_1 +2 == y_2 and x_1 == x_2
        elif en_passant:
            # TO BE IMPLEMENTED
            # not sure if it even belongs here yet but ???
            pass
        elif not first_move:
            return x_1 == x_2 and y_1 + 1 == y_2

