class Item:
    def __init__(self,itemName, itemPrice, itemQuantity):
        self.itemName = itemName
        self.itemPrice= itemPrice
        self.itemQuantity=itemQuantity
    
    def getItemName(self):
        return self.itemName
    