from pcard import *


class Hand(Deck):
    """definition of Deck"""
    def __init__(self):
        super().__init__()
        self.clear()

    def set_up(self, string):
        '''poker hand parser'''
        self.clear()
        for card in string.upper().split():
            try:
                self.append(PlayingCard(card[0], int(card[1:])))
            except ValueError:
                self.append(PlayingCard(
                    card[0], PlayingCard.NUMBER_LIST.index(card[1:])))

    def sort(self):
        super().sort(key=lambda x: (x.number, x.suit))
