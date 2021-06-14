from pcard import *
from hand import Hand


def is_flush(self):
    
    for i in range(1,7):
        
        number=0
        if self[0].suit == self[i].suit:
            number += 1
        if number >= 4:
            return True
        
    for i in range(2,7):
        
        number=0
        if self[0].suit ==self[1].suit:
            number +=1
        if self[1].suit == self[i].suit:
            number += 1
        if number >= 4:
            return True
        
    for i in range(3,7):
        
        number=0
        if self[0].suit ==self[2].suit or self[1].suit == self[2].suit:
            number +=1
        if self[2].suit == self[i].suit:
            number += 1
        if number >= 4:
            return True
        
    for i in range(4,7):
        
        number=0
        if self[0].suit ==self[3].suit or self[1].suit == self[3].suit or self[2] ==self[3].suit:
            number +=1
        if self[3].suit == self[i].suit:
            number += 1
        if number >= 4:
            return True

    for i in range(0,4):
        
        number=0
        if self[4].suit ==self[5].suit or self[4].suit == self[6].suit:
            number +=1
        if self[i].suit == self[4].suit:
            number += 1
        if number >= 4:
            return True  

    for i in range(0,5):
        
        number=0
        if self[5].suit ==self[6].suit:
            number +=1
        if self[i].suit == self[5].suit:
            number += 1
        if number >= 4:
            return True

    for i in range(0,6):
        
        number=0
        if self[i].suit == self[6].suit:
            number += 1
        if number >= 4:
            return True
    return False

Hand.is_flush = is_flush
