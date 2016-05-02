#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tasks:"""


import time


class ChessPiece(object):
    prefix = ''

    def __init__(self, position):
        """Constructor"""
        if ChessPiece.is_legal_move(self, position):
            self.position = position
            self.moves = []
        else:
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        if len(tile) == 2:
            if (97 <= ord(tile[:1]) <= 104) and (49 <= ord(tile[-1:]) <= 56):
                row = tile[:1]
                col = tile[-1:]
                if row == 'a':
                    return (0, int(col)-1)
                elif row == 'b':
                    return (1, int(col)-1)
                elif row == 'c':
                    return (2, int(col)-1)
                elif row == 'd':
                    return (3, int(col)-1)
                elif row == 'e':
                    return (4, int(col)-1)
                elif row == 'f':
                    return (5, int(col)-1)
                elif row == 'g':
                    return (6, int(col)-1)
                elif row == 'h':
                    return (7, int(col)-1)
                else:
                    return None
        else:
            return None

    def is_legal_move(self, position):
        another = self.algebraic_to_numeric(position)
        if another is None:
            return False
        elif (0 <= another[0] <= 7) and (0 <= another[1] <= 7):
            return True
        else:
            return False

    def move(self, position):
        """function docstring"""
        if self.is_legal_move(position):
            movetup = (self.prefix + self.position, self.prefix + position,
                       time.time())
            self.moves.append(movetup)
            self.position = position
            return movetup
        else:
            return False


class Rook(ChessPiece):
    """Rook with subclass ChessPiece."""
    prefix = 'R'

    def __init__(self, position):
        """Constructor"""
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Function docstring"""
        if ChessPiece.is_legal_move(self, position):
            if self.position[0] is position[0]:
                if int(self.position[1]) != int(position[1]):
                    return True
            elif int(self.position[1]) == int(position[1]):
                return True
        else:
            return False


class Bishop(ChessPiece):
    """Bishop with subclass ChessPiece."""
    prefix = 'B'

    def __init__(self, position):
        """Constructor"""
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        if ChessPiece.is_legal_move(self, position):
            if abs(ord(self.position[0]) - ord(position[0])) != \
               abs(ord(self.position[1]) - ord(position[1])):
                return False
            else:
                return True


class King(ChessPiece):
    """A Chess Piece, King, subclassed from ChessPiece."""
    prefix = 'K'

    def __init__(self, position):
        """Constructor"""
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Method docstring"""
        if ChessPiece.is_legal_move(self, position):
            if (abs(ord(self.position[0]) - ord(position[0])) == 1) and \
               (ord(self.position[1]) == ord(position[1])):
                return True
            elif (ord(self.position[0]) == ord(position[0])) and \
                 (abs(ord(self.position[1]) - ord(position[1])) == 1):
                return True
            elif (abs(ord(self.position[0]) - ord(position[0])) == 1) and \
                 (abs(ord(self.position[1]) - ord(position[1])) == 1):
                return True
        else:
            return False


class ChessMatch(object):

    def __init__(self, pieces=None):
        """constructor"""
        if pieces is None:
            self.reset(pieces)
        else:
            self.pieces = pieces
            self.log = []

    def reset(self):
        self.pieces['Ra1'] = Rook('a1')
        self.pieces['Rh1'] = Rook('h1')
        self.pieces['Ra8'] = Rook('a8')
        self.pieces['Rh8'] = Rook('h8')
        self.pieces['Bc1'] = Bishop('c1')
        self.pieces['Bf1'] = Bishop('f1')
        self.pieces['Bc8'] = Bishop('c8')
        self.pieces['Bf8'] = Bishop('f8')
        self.pieces['Ke1'] = King('e1')
        self.pieces['Ke8'] = King('e8')
        return match

    def move(self, piecename, coord):
        if self.pieces[piecename].move(coord) == False:
            return False
        else:
           value = self.pieces[piecename].move(coord)
           self.pieces[value[1]] = self.pieces.pop(value[0])
           self.log.append(value)

        def __len__(self):
            return len(self.log)

