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

from classes.pawn import Pawn
from classes.board import Board
from classes.match import Match
from math import ceil


class TestPawn(unittest.TestCase):
    def setUp(self) -> None:
        self.tela = Mock()
        self.tam = Mock()
        self.pawn = Pawn("A2", True)
        self.board = Board(self.tela, self.tam)
        self.pawn.board = self.board
        self.board.match = Match(self.board)

    def test_init(self):
        self.assertEqual(self.pawn.rect.topleft, (0, ceil(68.75 * 6)))
        self.assertTrue(self.pawn.is_white)
        self.assertEqual(self.pawn.name, "p")

    def test_possible_moves(self):
        with patch.object(self.board, 'get_piece', return_value=None):
            self.pawn.possible_moves(False)
            self.assertCountEqual(self.pawn.moves, [(2, 0), (3, 0)])
        with patch.object(self.board, 'get_piece', return_value=Mock(is_white=True)):
            self.pawn.possible_moves(False)
            self.assertCountEqual(self.pawn.moves, [])

    def test_possible_moves_not_in_original_position(self):
        with patch.object(self.board, 'get_piece', return_value=None):
            with patch.object(self.pawn, 'get_pos', return_value=(3, 0)):
                self.pawn.possible_moves(False)
                self.assertCountEqual(self.pawn.moves, [(4, 0)])

    def test_possible_moves_in_original_position(self):
        with patch.object(self.board, 'get_piece', return_value=None):
            with patch.object(self.pawn, 'get_pos', return_value=(1, 0)):
                self.pawn.possible_moves(False)
                self.assertCountEqual(self.pawn.moves, [(2, 0), (3, 0)])

    def test_move(self):
        with patch.object(self.board, 'move_piece') as mock_move_piece:
            self.pawn.move((2, 0))
            mock_move_piece.assert_called_once_with((1, 0), (2, 0), mock=False)
            self.assertEqual(self.pawn.get_row(), 2)
            self.assertEqual(self.pawn.get_column(), 0)

