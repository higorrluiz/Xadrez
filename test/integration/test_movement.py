import unittest
import pygame
import sys
import os

# getting the name of the directory where the this file is present
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present
parent = os.path.dirname(current)
# adding the parent directory to the sys.path
sys.path.append(os.path.dirname(parent))

STATE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "state2.txt")

from classes.board import Board
from classes.pawn import Pawn
from classes.match import Match

class TestMovementIntegration(unittest.TestCase):
    def setUp(self):
        self.tela = pygame.surface.Surface((800, 800))
        self.tam = 100
        self.board = Board(self.tela, self.tam, STATE_PATH)
        self.piece = Pawn("A1", True)
        self.board.matrix[0][0] = self.piece
        self.board.white.append(self.piece)
        self.board.white_group.add(self.piece)
        self.piece.board = self.board
        self.board.match = Match(self.board)

    def test_piece_movement(self):
        self.assertEqual(self.board.get_piece((0,0)), self.piece)
        self.assertIsNone(self.board.get_piece((1,0)))
        self.piece.move((1,0))
        self.assertEqual(self.board.get_piece((1,0)), self.piece)
        self.assertIsNone(self.board.get_piece((0,0)))

    def test_piece_capture(self):
        piece2 = Pawn("B2", False)
        piece2.board = self.board
        self.board.matrix[2][1] = piece2
        self.board.black.append(self.board.matrix[2][1])
        self.board.black_group.add(self.board.matrix[2][1])
        self.assertEqual(self.board.get_piece((0,0)), self.piece)
        self.assertIsNone(self.board.get_piece((1,0)))
        self.assertEqual(self.board.get_piece((2,1)), piece2)
        self.piece.move((1,0))
        self.assertEqual(self.board.get_piece((1,0)), self.piece)
        self.assertIsNone(self.board.get_piece((0,0)))
        self.assertEqual(self.board.get_piece((2,1)), piece2)
        self.piece.move((2,1))
        self.assertIsNone(self.board.get_piece((1,0)))
        self.assertEqual(self.board.get_piece((2,1)), self.piece)
        self.assertIsNone(self.board.get_piece((0,0)))

