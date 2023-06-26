import unittest

import sys
import os
from unittest.mock import patch, Mock

# getting the name of the directory where the this file is present
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present
parent = os.path.dirname(current)
# adding the parent directory to the sys.path
sys.path.append(parent)

from classes.rook import Rook
from classes.board import Board
from classes.match import Match
from classes.piece import Piece


class TestRook(unittest.TestCase):

    def setUp(self) -> None:
        self.tela = Mock()
        self.tam = Mock()
        self.rook = Rook("A1", True)
        self.board = Board(self.tela, self.tam)
        self.rook.board = self.board
        self.board.match = Match(self.board)
        self.board.match.passant_white = None

    def test_init(self):
        self.assertEqual(self.rook.rect.topleft, (0, round(68.75 * 7)))
        self.assertTrue(self.rook.is_white)
        self.assertEqual(self.rook.name, "r")
        self.assertFalse(self.rook.moved)

    def test_possible_moves(self):
        with patch.object(self.board, 'get_piece', return_value=None):
            self.rook.possible_moves(False)
            self.assertCountEqual(self.rook.moves, [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7 ,0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0 ,6), (0, 7)])

    def test_possible_moves_with_own_piece(self):
        with patch.object(self.board, 'get_piece', return_value=Piece("A2", True)):
            self.rook.possible_moves(False)
            self.assertCountEqual(self.rook.moves, [])

    def test_possible_moves_with_enemy_piece(self):
        self.board.get_piece = Mock(side_effect=self.__mock_get_piece)
        with patch.object(self.board, 'black' , return_value=[Piece("A2", False), Piece("B1", False)]):
            self.rook.possible_moves(False)
            self.assertCountEqual(self.rook.moves, [(0, 1), (1, 0)])

    def test_get_moved(self):
        self.assertFalse(self.rook.moved)
        self.rook.move((0, 2))
        self.assertTrue(self.rook.moved)

    # TODO: test_move

    # Mocks

    def __mock_get_piece(self, pos: tuple[int, int]):
        if pos == (1, 0):
            return Piece("A2", False)
        elif pos == (0, 1):
            return Piece("B1", False)
        else:
            return None

