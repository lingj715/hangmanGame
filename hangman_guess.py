## This file is logic about guess letter
import os
import json
import re
from collections import defaultdict
from string import punctuation

class HangManGuess():
    def __init__(self):
        # Store the data as {len(word): {word: frequency}}
        self.word_frequency = defaultdict(lambda: defaultdict(int))
        self.init_word_frequency()

    # Initialize self.word_frequency
    def init_word_frequency(self):
        # If Json file exists, read it
        if os.path.exists("processed_word_frequency.json"):
            with open("processed_word_frequency.json") as json_file:
                data = json.load(json_file)
                for key in data.keys():
                    self.word_frequency[int(key)] = data[key]
        # Else, get data from word_frequency.txt and process
        else:
            f_r = open("word_frequency.txt", "r")
            for line in f_r:
                word, frequency = line.split()
                self.word_frequency[len(word)][word.upper()] = int(frequency)
            with open("processed_word_frequency.json", "w", encoding='utf-8') as f_w:
                json.dump(self.word_frequency, f_w, ensure_ascii=False, indent=4)

    def guess(self, state):
        pattern = re.split(r'\W+', state)
        guess_pattern = self.guess_part(pattern)
        guess_result_list = self.guess_logic(guess_pattern, state)
        return guess_result_list

    def guess_part(self, pattern):
        guess_part = ""
        all_line = self.check_all_line(pattern)

        if all_line[0]: ## no clue at all, choose shortest one.
            guess_part = all_line[1]
        else: ## else check which part
            guess_part = self.which_part(pattern)
        return guess_part


    def check_all_line(self, pattern):
        result = ""
        for s in pattern:
            if s.count('_') != len(s):
                return (False, "")
            else:
                if result == "":
                    result = s
                elif len(result) > len(s):
                    result = s
        return (True, result)

    def which_part(self, pattern):
        rate = float('-inf')
        result = ""
        for s in pattern:
            underline = s.count('_')
            letter = len(s) - underline
            if underline != 0: ## Still need guess
                if result == "": ## First possible guess pattern
                    result = s
                    if underline < len(s):
                        rate = (letter*1.0)/(underline*1.0)
                else: ## may need update
                    if letter == 0:
                        if result.count('_') == len(result) and len(result) > len(s):
                            result = s
                    else:
                        temp = (letter*1.0)/(underline*1.0)
                        if temp > rate:
                            rate = temp
                            result = s
        return result


    def guess_logic(self, pattern, str):
        # candidates{word: frequency}, index(no need to guess), index(need to guess)
        candidates, fix, need_guess = self.choose_candidates(pattern)
        freq = defaultdict(int)
        most_candidate = sorted(candidates.items(), key=lambda x: x[1], reverse=True)
        candidate_letter = defaultdict(int)
        candidate_letter_2 = set()
        for pair in most_candidate:
            word, frequency = pair[0], pair[1]
            for i in need_guess:
                candidate_letter[word[i]] = max(candidate_letter[word[i]], frequency)
                candidate_letter_2.add(word[i])

        for item in most_candidate:
            word = item[0]
            for index in need_guess:
                if word[index] in candidate_letter_2:

                    key = tuple([word[index], candidate_letter[word[index]]])
                    freq[key] += 1
        temp_result = sorted(freq.items(), key=lambda x: (x[0][1], x[1]), reverse=True) #letter can choose: frequency high to low
        result = []
        for item in temp_result:
            result.append(item[0][0])
        return result



    def choose_candidates(self, pattern):
        fix = []
        need_guess = []
        candidates = defaultdict(int)
        for i in range(len(pattern)):
            if pattern[i] != '_':
                fix.append(i)
            else:
                need_guess.append(i)
        temp_candidates = self.word_frequency[len(pattern)]

        for word in temp_candidates:
            flag = True
            for index in fix:
                if pattern[index] != word[index]:
                    flag = False
            if flag:
                candidates[word] = temp_candidates[word]
        return (candidates, fix, need_guess)













