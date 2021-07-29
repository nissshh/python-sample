from card import Card
from random import shuffle
values = {'One':1,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
    'Jack':11,'Queen':12,'King':13}
suits=["Hearts","Spade","Diamond","Club"]
ranks=['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']

class Deck:
    def __init__(self):
        self.new_deck=[]
        for s in suits:
            for r in ranks:
                c=Card(s,r)
                self.new_deck.append(c)
    def shuffle_deck(self):
        shuffle(self.new_deck)

if __name__ == "__main__":
    d=Deck()
    d.shuffle_deck()
    print(d.new_deck[12])