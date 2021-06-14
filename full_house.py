from pcard import *
from hand import Hand

def set_up(self, string):
    '''poker hand parser'''
    self.clear()
    for card in string.upper().split():
        try:
            self.append(PlayingCard(card[0], int(card[1:])))
        except ValueError:
            self.append(PlayingCard(
                card[0], PlayingCard.NUMBER_LIST.index(card[1:])))
        except:
            raise
Hand.set_up = set_up

def is_four_of_a_kind(self):
    self.sort()
    if self[0].number == self[3].number or self[1].number == self[4].number:
        return True
    else:
        return False

Hand.is_four_of_a_kind = is_four_of_a_kind


def is_straight_flush(self):
    if self.is_straight() and self.is_flush():
        return True
    else:
        return False
setattr(Hand, "is_straight_flush", is_straight_flush)


def is_full_house(self):
    self.sort()
    if (self[0].number ==self[1].number and  self[2].number ==self[4].number) or (self[0].number ==self[2].number and  self[3].number ==self[4].number):
        return True
    else:
        return False

Hand.is_full_house = is_full_house

def is_flush(self):
    self.sort
    if self[0].suit ==self[1].suit and self[1].suit ==self[2].suit \
       and self[2].suit ==self[3].suit and self[3].suit ==self[4].suit :
        return True
    else:
        return False

Hand.is_flush=is_flush

def is_straight(self):
    self.sort()

'''
is_three_of_a_kind
'''
def is_two_pair(self):
    self.sort
    if (self[0].number ==self[1].number and self[2].number ==self[3].number\
       and not(self[0].number==self[4].number or self[2].number ==self[4].number))\
       or(self[0].number ==self[1].number and self[3].number ==self[4].number\
       and not (self[0].number==self[2].number or self[2].number==self[4].number))\
       or(self[1].number ==self[2].number and self[3].number ==self[4].number\
       and not (self[0].number==self[1].number or self[0].number==self[3].number)):
        return True
    else:
        return False

Hand.is_two_pair=is_two_pair

'''
is_one_pair
'''
