######################################################################
#
#   MOTION LANGUAGE:
#       
#       The chess board can be described like the first quarter of a
#       cartesian plane, and insted of `x` & `y`, I use North and West.
#
#       There are 2 Cardinal Directions: N, W
#       There are 2 Other Directions: NW, NE
#
#       This means a direction like SE is expressed as negative NW.
#
#       These directions can be used to describe all motion on the
#       chess board. In addition to direction, the motion vector needs
#       magnitude. This can be expressed with an integer, '2', to 
#       express a number of squares of movement or with a glob, '*', 
#       to express unlimited motion in a direction.
#
######################################################################

import re

# DUPLICATION -- find out where it belongs!!
files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ranks = [i for i in range(1, 9)]


class Motion:
    def __init__(self):
       pass

    def further_north(rank_1, rank_2):
        return rank_1 > rank_2

    def further_south(rank_1, rank_2):
        return rank_1 < rank_2

    def further_west(file_1, file_2):
        for f in files:
            if f == file_1 and not f == file_2:
                return True
            if f == file_2 and not f == file_1:
                return False
        return False

    def further_east(file_1, file_2):
        for f in files:
            if f == file_2 and not f == file_1:
                return True
            if f == file_1 and not f == file_2:
                return False
        return False
    
    def indexed_file(file_):
        i = 0
        while files[i] != file_:
            i += 1
        return i

    def filed_index(i):
        return files[i]

    def valid_move(start, end):
        return True
   
#MovementInterpreter?
class MotionLanguage:
    def __init__(self, motion_string):
        rexp = r'([A-Z])\(([+-]*)\)([0-9]\*)'
        pattern = re.compile(rexp)
        direction, pos_neg, magnitude = pattern.match(motion_string)


class RookMotion(Motion):
    # allowable_movement = ('N(+/-)*', 'W(+/-)*')
    # capturing_movement = allowable_movement
    def valid_move(start, destination):
        start_file, start_rank = start
        destination_file, destination_rank = destination
        if start_file == destination_file:
            return True
        elif start_rank == destination_rank:
            return True
        else:
            return False

    def intermediate_squares(start, destination):
        intermediate_squares = []
        if not Motion.valid_move(start, destination):
            return None

        start_file, start_rank = start
        destination_file, destination_rank = destination
        if Motion.further_north(start_rank, destination_rank):
            start_rank -= 1
            while start_rank >= destination_rank:
                intermediate_squares.append(
                        (start_file, start_rank))
        elif Motion.further_south(start_rank, destination_rank):
            start_rank += 1
            while start_rank <= destination_rank:
                intermediate_squares.append((start_file, start_rank))
                start_rank += 1
        elif Motion.further_west(start_file, destination_file):
            indexed_start_file = Motion.indexed_file(start_file) + 1
            indexed_destination_file = Motion.indexed_file(destination_file)
            while indexed_start_file <= indexed_destination_file:
                intermediate_squares.append((
                    Motion.filed_index(indexed_start_file), start_rank))
                indexed_start_file += 1
        elif Motion.further_east(start_file, destination_file):
            indexed_start_file = Motion.indexed_file(start_file) - 1
            indexed_destination_file = Motion.indexed_file(destination_file)
            while indexed_start_file >= indexed_destination_file:
                intermediate_squares.append((
                    Motion.filed_index(indexed_start_file), start_rank))
                indexed_start_file -= 1
        return intermediate_squares



            
class KnightMotion(Motion):
    allowable_movement = ('N(+/-)2,W(+/-)1', 'W(+/-)2,N(+/-)1')
    capturing_movement = allowable_movement

class BishopMotion(Motion):
    allowable_movement = ('NW(+/-)*', 'NE(+/-)*')
    capturing_movement = allowable_movement

class QueenMotion(Motion):
    allowable_movement = ('N(+/-)*', 'W(+/-)*', 'NW(+/-)*', 'NE(+/-)*')
    capturing_movement = allowable_movement

class KingMotion(Motion):
    allowable_movement = ('N(+/-)1', 'W(+/-)1', 'NW(+/-)1', 'NE(+/-)1')
    capturing_movement = allowable_movement

class PawnMotion(Motion):
    pass
    # if first_move:
    #     allowable_movement = ('N(+)1', 'N(+)2')
    # else:
    #     allowable_movement = ('N(+)1')

    # capturing_movement = ('N(+)1,W(+/-)1')

