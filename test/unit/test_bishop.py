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

from classes.bishop import Bishop
from classes.board import Board
from classes.match import Match
from classes.piece import Piece


class TestBishop(unittest.TestCase):

    def setUp(self) -> None:
        self.tela = Mock()
        self.tam = Mock()
        self.bishop = Bishop("A1", True)
        self.board = Board(self.tela, self.tam)
        self.bishop.board = self.board
        self.board.match = Match(self.board)
        self.board.match.passant_white = None

    def test_init(self):
        self.assertEqual(self.bishop.rect.topleft, (0, round(68.75 * 7)))
        self.assertTrue(self.bishop.is_white)
        self.assertEqual(self.bishop.name, "b")

    def test_possible_moves(self):
        with patch.object(self.board, 'get_piece', return_value=None):
            self.bishop.possible_moves(False)
            self.assertCountEqual(self.bishop.moves, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7 ,7)])

    def test_possible_moves_with_own_piece(self):
        with patch.object(self.board, 'get_piece', return_value=Piece("A2", True)):
            self.bishop.possible_moves(False)
            self.assertCountEqual(self.bishop.moves, [])

    def test_possible_moves_with_enemy_piece(self):
        self.board.get_piece = Mock(side_effect=self.__mock_get_piece)
        with patch.object(self.board, 'black' , return_value=[Piece("B2", False)]):
            self.bishop.possible_moves(False)
            self.assertCountEqual(self.bishop.moves, [(1, 1)])


    # TODO: test_move

    # Mocks

    def __mock_get_piece(self, pos: tuple[int, int]):
        if pos == (1, 1):
            return Piece("B2", False)
        else:
            return None

