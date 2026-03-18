class Item:
    def __init__(self, name, price, fragile):
        self.__name = name
        self.price = price
        self.fragile = fragile

    def getname(self):
        return self.name
    
    def setname(self, NewName):
        if len(NewName) == 0:
            return
        self.name = NewName


    
    def getAttribute(self, attribute):
        
        return self.attribute
    


apple = Item('Apple' , 1.50 , False)

    
        
print(apple.getname())
