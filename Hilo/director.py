from card import *

class Director:

    def __init__(self):
        self.past_card = 0
        self.next_card = 0
        self.score = 300
        self.keep_playing = "y"
        self.current_score = 0

    def start_game(self):
        while self.score > 0:
            if self.keep_playing == "y":
                self.play()
                if self.current_score > 0:
                    self.keep_playing = input("Play again? [y/n] ")

    def play(self):
        card = Card()
        self.past_card = card.deal_card()
        print(f"The card is {self.past_card}")
        self.user_guess = input("Higher or lower? [h/l] ")
        self.next_card = card.deal_card()
        print(f"Next card was {self.next_card}")
        self.current_score = self.calculate()
        print(f"Your score is {self.current_score}")
        return self.current_score

    def calculate(self):
        card = Card()
        if self.user_guess == "h":
            if self.past_card < self.next_card:
                self.score = self.score + 100
            else:
                self.score = self.score - 75
        elif self.user_guess == "l":
            if self.past_card > self.next_card:
                self.score = self.score + 100
            else:
                self.score = self.score - 75
        else:
            print("Wrong typed")       
        return self.score