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

from classes.king import King
from classes.board import Board
from classes.match import Match
from classes.piece import Piece


class TestKing(unittest.TestCase):
    def setUp(self) -> None:
        self.tela = Mock()
        self.tam = Mock()
        self.king = King("E1", True)
        self.board = Board(self.tela, self.tam)
        self.king.board = self.board
        self.board.match = Match(self.board)

    def test_init(self):
        self.assertEqual(self.king.rect.topleft, (round(68.75 * 4), round(68.75 * 7)))
        self.assertTrue(self.king.is_white)
        self.assertEqual(self.king.name, "k")
        self.assertFalse(self.king.moved)

    def test_possible_moves(self):
        with patch.object(self.board, 'get_piece', return_value=None):
            self.king.possible_moves(False)
            self.assertCountEqual(self.king.moves, [(1, 4), (0,5), (0, 3), (1, 3), (1, 5)])
        with patch.object(self.board, 'get_piece', return_value=Mock(is_white=True)):
            self.king.possible_moves(False)
            self.assertCountEqual(self.king.moves, [])
        self.board.get_piece = Mock(side_effect=self.__mock_get_piece)
        with patch.object(self.board, 'black' , return_value=[Piece("B2", False)]):
            self.king.possible_moves(False)
            self.assertCountEqual(self.king.moves, [(1, 4), (0,5), (0, 3), (1, 3), (1, 5)])

    def test_move(self):
        with patch.object(self.board, 'move_piece') as mock_move_piece:
            self.king.move((0, 5))
            mock_move_piece.assert_called_once_with((0, 4), (0, 5), mock=False)
            self.assertEqual(self.king.get_row(), 0)
            self.assertEqual(self.king.get_column(), 5)

    # Mocks

    def __mock_get_piece(self, pos: tuple[int, int]):
        if pos == (1, 4):
            return Piece("B2", False)
        if pos == (0, 5):
            return Piece("B2", False)
        if pos == (0, 3):
            return Piece("B2", False)
        if pos == (1, 3):
            return Piece("B2", False)
        if pos == (1, 5):
            return Piece("B2", False)
        else:
            return None

