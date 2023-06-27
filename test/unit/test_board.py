import unittest

import sys
import os
from unittest.mock import patch, mock_open, Mock, call

import pygame

# getting the name of the directory where the this file is present
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present
parent = os.path.dirname(current)
# adding the parent directory to the sys.path
sys.path.append(os.path.dirname(parent))

from classes.board import Board
from classes.pawn import Pawn
from classes.king import King
from classes.rook import Rook
from classes.bishop import Bishop
from classes.match import Match

STATE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "state1.txt")

class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.tela = pygame.surface.Surface((800, 800))
        self.tam = 100
        self.board = Board(self.tela, self.tam)
        self.board.match = Match(self.board)

    def test_init(self):
        self.assertEqual(self.board.linhas, 8)
        self.assertEqual(self.board.colunas, 8)
        self.assertEqual(len(self.board.white), 16)
        self.assertEqual(len(self.board.black), 16)
        self.assertEqual(len(self.board.white_group), 16)
        self.assertEqual(len(self.board.black_group), 16)
        self.assertIsInstance(self.board.white[8], Pawn)
        self.assertIsInstance(self.board.black[12], King)

    def test_get_piece(self):
        piece = self.board.get_piece((0, 0))
        self.assertIsInstance(piece, Rook)
        self.assertEqual(piece.get_row(), 0)
        self.assertEqual(piece.get_column(), 0)
        piece = self.board.get_piece((4, 4))
        self.assertIsNone(piece)

    def test_move_piece(self):
        self.board.move_piece((0, 0), (1, 0))
        self.assertIsNone(self.board.get_piece((0, 0)))
        self.assertIsInstance(self.board.get_piece((1, 0)), Rook)

    def test_promotion(self):
        self.assertIsInstance(self.board.get_piece((7, 0)), Rook)
        self.board.promotion(Bishop("A8", True), (7, 0))
        self.assertIsInstance(self.board.get_piece((7, 0)), Bishop)

    def test_init_loading_state(self):
        self.tela = pygame.surface.Surface((800, 800))
        self.tam = 100
        self.board = Board(self.tela, self.tam, STATE_PATH)
        self.board.match = Mock()
        self.assertEqual(self.board.linhas, 8)
        self.assertEqual(self.board.colunas, 8)
        self.assertEqual(len(self.board.white), 16)
        self.assertEqual(len(self.board.black), 16)
        self.assertEqual(len(self.board.white_group), 16)
        self.assertEqual(len(self.board.black_group), 16)
        self.assertIsInstance(self.board.get_piece((2, 0)), Pawn)
        self.assertEqual(self.board.get_king(True).get_pos_str(), "E4")

    def test_save_state(self):
        with patch('builtins.open', mock_open()) as mock_file:
            self.board.save_state('test.txt', [True, False], 2)
            mock_file.assert_called_once_with('test.txt', 'w')
            handle = mock_file()
            handle.write.assert_has_calls([
                call('r'),
                call('n'),
                call('b'),
                call('q'),
                call('k'),
                call('b'),
                call('n'),
                call('r'),
                call('\n'),
                call('p'),
                call('p'),
                call('p'),
                call('p'),
                call('p'),
                call('p'),
                call('p'),
                call('p'),
                call('\n'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('\n'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('\n'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('\n'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('-'),
                call('\n'),
                call('P'),
                call('P'),
                call('P'),
                call('P'),
                call('P'),
                call('P'),
                call('P'),
                call('P'),
                call('\n'),
                call('R'),
                call('N'),
                call('B'),
                call('Q'),
                call('K'),
                call('B'),
                call('N'),
                call('R'),
                call('\n'),
                call('F'),
                call('F'),
                call('F'),
                call('F'),
                call('F'),
                call('F'),
                call('\n'),
                call('--'),
                call('--'),
                call('\n'),
                call('0'),
                call('\n'),
                call('T'),
                call('F'),
                call('\n'),
                call('2'),
            ])
