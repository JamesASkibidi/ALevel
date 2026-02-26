import random


class Card:
    def __init__ (self):
        self.suit = ''
        self.value = ''
        self.type = ''
        self.name = ''

    def createCard(self, givenSuit ,givenSymbol, givenType, givenValue ):
        self.suit = givenSuit
        self.value = givenValue
        self.type = givenType
        self.symbol = givenSymbol
        self.name = (self.type + ' of ' + self.suit)

    def printName(self):
        print(self.name)

        

class Deck:
    def __init__ (self):
        self.size = 52
        self.realDeck = []

    def createDeck(self):

        for i in suits:
            
            for j in cardTypes:
                newcard = Card()
                newcard.createCard(i[0], i[1] , j[0] ,j[1])
                newcard.printName()
                self.realDeck.append(newcard)
                random.shuffle(self.realDeck)

class Hand:
    def __init__ (self):
        self.hand = []

    def addCard(self , newCard):
        self.hand.append(newCard)
              
       



cardTypes = [['A' , 1],['Two' , 2],['Three' , 3],['Four' , 4],['Five' , 5],['Six' , 6],['Seven' , 7],['Eight' , 8],['Nine' , 9],['Ten' , 10],['J' , 11],['Q' , 12],['K' , 13]]

suits = [['Hearts' ,"\N{Black Heart Suit}" ],['Clubs' ,"\N{Black Club Suit}" ],['Spades' ,"\N{Black Spade Suit}" ],['Diamonds' ,"\N{Black Diamond Suit}" ]]





deck = Deck()

deck.createDeck()

