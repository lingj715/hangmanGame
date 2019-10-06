## This file is hangman object which stores hangman state

class Hangman():
    def __init__(self):
        self.game_state = ""
        self.token = ""
        self.remaining_guess = 0
        self.state = ""

    def set_game_state(self, game_state):
        self.game_state = game_state

    def set_token(self, token):
        self.token = token

    def set_remaining_guess(self, remain):
        self.remaining_guess = remain

    def set_state(self, state):
        self.state = state