## This file is hangman game runner. Main game interface.
import sys
import requests
from hangman import Hangman
from hangman_guess import HangManGuess

class Runner():
    def __init__(self, api, times):
        self.fail = 0
        self.success = 0
        self.api = api
        self.times = times

    def runner(self):
        for i in range(self.times):
            try:
                hangman = Hangman()
                hangman_guess = HangManGuess()
                self.start(hangman)

                guess_result_list = []
                index = 0

                while hangman.game_state == "ALIVE":
                    if guess_result_list == []:
                        guess_result_list = hangman_guess.guess(hangman.state)


                    guess_result = guess_result_list[index]


                    r = requests.get("http://gallows.hulu.com/play?code={}&token={}&guess={}".format(self.api, hangman.token, guess_result))
                    response = r.json()

                    if response['state'] == hangman.state: ## False Guess
                        index += 1
                    else: ## Rright Guess
                        hangman.set_game_state(response['status'])
                        hangman.set_remaining_guess(response['remaining_guesses'])
                        hangman.set_state(response['state'])
                        hangman.set_token(response['token'])
                        guess_result_list = []
                        index = 0

                if hangman.game_state == "DEAD":
                    print("Turn {}, Fail.".format(i+1))
                    self.fail += 1

                if hangman.game_state == "FREE":
                    print("Turn {}, Success.".format(i+1))
                    self.success += 1


            except:
                print("Turn {}, Fail.".format(i+1))
                self.fail += 1

        print("FINISH!! Success: {}, Fail: {}, Success Rate: {}".format(self.success, self.fail, self.success/int(times)))


    def start(self, hangman):
        r = requests.get("http://gallows.hulu.com/play?code=lij007@eng.ucsd.edu")
        response = r.json()
        hangman.set_game_state(response['status'])
        hangman.set_remaining_guess(response['remaining_guesses'])
        hangman.set_state(response['state'])
        hangman.set_token(response['token'])


if __name__ == "__main__":
    api, times = sys.argv[1], sys.argv[2]

    if api != "lij007@eng.ucsd.edu":
        print("API is incorrect")

    if times.isdigit() == False or int(times) <= 0:
        print("Please enter positive running times")

    runner = Runner(api, int(times))
    runner.runner()
