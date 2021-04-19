class TennisGame():
    def __init__(self):
        self._score = 'Love all'
        self._p1_score = 0
        self._p2_score = 0
        self._p1_gems = 0
        self._p2_gems = 0
        self.gem_score = "0 - 0"
    @property
    def score(self):
        return self._score

    def player_one_scored(self):
        self._p1_score += 1
        self.__calculate_score()

    def player_two_scored(self):
        self._p2_score += 1
        self.__calculate_score()

    def player_one_got_gem(self):
        self._p1_gems = +1
        self.__calculate_sets()

    def player_two_got_gem(self):
        self._p2_gems = +1
        self.__calculate_sets()

    def __calculate_score(self):
        first_result, second_result = "", ""

        if self._p1_score == 4 and self._p2_score == 4:
            self._score =  'Deuce'
            return

        if self._p1_score == 0:
            first_result = "Love"
        elif self._p1_score == 1:
            first_result = 'Fifteen'
        elif self._p1_score == 2:
            first_result = 'Thirty'
        elif self._p1_score == 3:
            first_result = 'Fourty'
        elif self._p1_score == 4:
            self._score = 'Grm for p1'
            self.player_one_got_gem()
            return

        if self._p2_score == 0:
            second_result = "Love"
        elif self._p2_score == 1:
            second_result = 'Fifteen'
        elif self._p2_score == 2:
            second_result = 'Thirty'
        elif self._p2_score == 3:
            second_result = 'Fourty'
        elif self._p2_score == 4:
            self._score = 'Gem for p2'
            self.player_two_got_gem()
            return



        if self._p1_score == self._p2_score:
            self._score = f"{first_result} All"
        else:
            self._score = f"{first_result} {second_result}"

    def __calculate_sets(self):
        self.gem_score = f"{self._p1_gems} - {self._p2_gems}"
