class Item:
   # Blueprint class to represent an item
   
    def __init__(self,itemName, itemPrice, itemQuantity):
      """
      Constructor for item object instances
      
      Args:
         itemName (String): name of the item
         itemPrice(Float): proce of the item
         itemQuantity (Integer): quantity of the items
      Methods:
         getItemName(): getter for item name
         getItemPrice(): getter for the price
         getItemQuantity(): getter for quantity
         changeItemQuantity(): setter for price
      Return:
         item instance
      """
        self.itemName = itemName
        self.itemPrice= itemPrice
        self.itemQuantity=itemQuantity
    
   # getting the name of the item
    def getItemName(self):
        return self.itemName
      
   #getting the price of the item 
    def getItemPrice():
        return self.itemPrice
      
   # getting the item quantity
    def getItemQuantity():
        return self.itemQuantity
      
   # changing the existing quantity of items
    def changeItemQuantity():
      
      # ask shopper id they want to add or sub
        change = int(
      input(
      "Do you want to\n1. Add?\n2.Substract ?"
      ))
      
      # return if user enters nothing
      if not change:
         return "You did not choose an option"
      if change == 1:
         
         # ask for how much to be added
         addition_qty = int(
         input(
         "Enter number if items to add: "
         )
         )
         
         # return existing quantity of no input
         if not addition_qty:
            print("No items were added.")
            return getItemQuantity()
         else:
            try:
               # add to the existing quantity
               return getItemQuantity + addition_qty
            except ValueError:
               # throw an error if an invalid input was obtained
               raise("Invalid quantity")
               
# PUT THIS IN ITS OWN FILE
#•••••••••••••••••••••••••••

#import Item
"""
class Cart(Item):
    # cart emulates the shopping cart
    def __init__(self,Item,cart_total=0):
        super()
        self.cart_total=cart_total
        self.item_list= []
    
    #add items
    def add_toCart(Item):
        self.item_list.append(Item)
        
    #calc total in the cart
    def calc_total():
        #TODO: implement logic later
        pass
"""
        
# WORKING VERSION
#•••••••••••••••••
#from Item import Item

class Cart:
    """Represents a shopping cart holding multiple Item objects."""

    def __init__(self, cart_total=0):
        self.cart_total = cart_total
        self.item_list = []

    def add_toCart(self, item: Item):
        """Adds an Item object to the cart."""
        self.item_list.append(item)

    def calc_total(self):
        """Calculate the total price of all items."""
        total = 0
        for item in self.item_list:
            total += item.price  # assuming Item has a price attribute
        return total