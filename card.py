values = {'One':1,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
    'Jack':11,'Queen':12,'King':13}
suits=["Hearts","Spade","Diamond","Club"]
ranks=['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    
    def __str__(self):
        return self.rank+" of "+ self.suit

if __name__ == "__main__":
    c=Card('Hearts','Two')
    print(c)
