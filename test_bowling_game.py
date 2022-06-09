import unittest
from Bowling import Bowling_Game


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Bowling_Game()

    # A gutter game (20 times 0 pin) should score 0
    def test_gutter_game(self):
        self._roll_many(0, 20)
        self.assertEqual(0, self.game.final_score())

    # An all one game (20 times 1 pin) should score 20
    def test_all_ones(self):
        self._roll_many(1, 20)
        self.assertEqual(20, self.game.final_score())

    # A spare followed by a 3 should score 16
    def test_one_spare(self):
        self._roll_spare()
        self.game.roll(3)
        self._roll_many(0, 17)
        self.assertEqual(16, self.game.final_score())

    # A strike followed by a 3 and a 4 should score 24
    def test_one_strike(self):
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self._roll_many(0, 16)
        self.assertEqual(24, self.game.final_score())

    # The perfect game (12 times 10) should score 300
    def test_all_strikes(self):
        self._roll_many(10, 12)
        self.assertEqual(300, self.game.final_score())

    # Bowling score : 1 – 4, 4 – 5, 6 - /, 5 - /, X, 0 – 1, 7 - /, 6 - /, X, 2 - / - 6
    def test_simple_game(self):
        for pins in [1, 4, 4, 5, 6, 4, 5, 5,
                     10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6]:
            self.game.roll(pins)
        self.assertEqual(133, self.game.final_score())

    # All spares
    def test_all_spare(self):
        self._roll_many(5, 21)
        self.assertEqual(150, self.game.final_score())

    def _roll_many(self, pins, num):
        for i in range(num):
            self.game.roll(pins)

    def _roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)


if __name__ == '__main__':
    unittest.main()
