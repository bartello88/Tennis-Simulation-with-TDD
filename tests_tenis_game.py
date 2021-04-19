import unittest
from main import TennisGame


class TestTennisGame(unittest.TestCase):
    def setUp(self):
        self.game = TennisGame()

    def test_something(self):
        initial_score = self.game.score
        self.assertEqual('Love all', initial_score)

    def test_score_is_15_0_when_p1_scored_once(self):
        self.create_score(1,0)
        self.assertEqual('Fifteen Love', self.game.score)
    def test_score_is_15_15_when_both_players_scored_once(self):
        self.create_score(1,1)
        self.assertEqual('Fifteen All', self.game.score)

    def test_score_is_30_0_when_p1_scored_twice(self):
        self.create_score(2,0)
        self.assertEqual('Thirty Love', self.game.score)

    def test_score_is_30_30_when_both_players_scored_twice(self):
        self.create_score(2,2)
        self.assertEqual('Thirty All', self.game.score)

    def test_score_is_40_0_when_p1_scored_3_times(self):
        self.create_score(3 ,0)
        self.assertEqual('Fourty Love', self.game.score)

    def test_score_is_40_40_when_both_players_scored_3_times(self):
        self.create_score(3 ,3)
        self.assertEqual('Fourty All', self.game.score)

    def test_score_is_40_15_when_p1_scored_3_times_and_p2_scored_twice(self):
        self.create_score(3,1)
        self.assertEqual('Fourty Fifteen', self.game.score)

    def test_score_is_30_15_when_p1_scored_twice_and_p2_scored_once(self):
        self.create_score(2,1)
        self.assertEqual('Thirty Fifteen', self.game.score)

    def test_score_is_30_30_when_p1_scored_twice_and_p2_scored_twice(self):
        self.create_score(2,2)
        self.assertEqual('Thirty All', self.game.score)

    def test_score_is_40_30_when_p1_scored_3_times_and_p2_scored_2_twice(self):
        self.create_score(3,2)
        self.assertEqual('Fourty Thirty', self.game.score)

    def test_score_is_0_15_when_p2_scored_once(self):
        self.create_score(0,1)
        self.assertEqual('Love Fifteen', self.game.score)

    def test_gem_for_p1(self):
        self.create_score(4, 0)
        self.assertEqual(1, self.game._p1_gems)

    def test_gem_for_p2(self):
        self.create_score(0,4)
        self.assertEqual(1, self.game._p2_gems)

    def test_set_score_when_p1_got_gem(self):
        self.game.player_one_got_gem()
        self.assertEqual("1 - 0", self.game.gem_score)

    def test_set_score_when_p2_got_gem(self):
        self.game.player_two_got_gem()
        self.assertEqual("0 - 1", self.game.gem_score)

    def test_when_both_players_got_gem(self):
        self.game.player_one_got_gem()
        self.game.player_two_got_gem()
        self.assertEqual("1 - 1", self.game.gem_score)

    def create_score(self, player_one_scored, player_two_scored):
        for _ in range(player_one_scored):
            self.game.player_one_scored()
        for _ in range(player_two_scored):
            self.game.player_two_scored()

    def dual_score(self):
        self.create_score(4,4)
        self.assertEqual('Deuce', self.game.score)
