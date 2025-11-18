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
        self.price_by_quantity = 0
    
   # getting the name of the item
    def getItemName(self):
        print(f"This is the item name: {self.itemName}")
        return self.itemName
      
   #getting the price of the item 
    def getItemPrice():
        print(f"This is the item price: {self.itemPrice}")
        return self.itemPrice
      
   # getting the item quantity
    def getItemQuantity():
        print(f"This is the file quantity: {self.itemQuantity}")
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
   def get_total_per_item():
      return self.price_per_quantity
               
# PUT THIS IN ITS OWN FILE
#•••••••••••••••••••••••••••
#from Item import Item

class Cart:
    """Represents a shopping cart holding multiple Item objects."""

    def __init__(self, cart_total=0):
        # total might not be useful here
        self.cart_total = cart_total
        self.item_list = []

    def add_toCart(self, item: Item):
        """Adds an Item object to the cart."""
        self.item_list.append(item)
        print(f"This the status of the list")
       for itm in item_list:
          print(f"{itm}")

    def calc_total_per_item(self):
        """Calculate the total price of all items."""
        for item in self.item_list:
            item.get_total_per_item() = item.getItemPrice() * item.getItemQuantity()  # assuming Item has a price attribute
            print(f"{item} : total per item {item.get_total_per_item()}")
        return self.item_list
      
#class to simulate shopping
class shop:
   # ask user to add items
   def grocery_list(self):
      #get item name
      item_name = input("What item do you want?: ")
      
      # get the price...assume user will enter valid price
      item_price = float(input("Enter its price in the format 00.00: $"))
      
      #get the quantity..... assume user will enter valid number 
      item_quantity = int(input("How many " + item_name + "(s) do you want to purchase?: "))
      
      #create item object
      item = Item(item_name, item_price, item_quantity)
      print(f"Item: name -> {item.item_name}, {item.item_price}, {item.item_quantity}")
      
      # return the item object
      # we need to return the list in the cart
      print(f"Initializing cart ...... ")
      cart = Cart()
      cart.add_toCart(item)
      print("Items in the cart - NOT YET")
      
      return cart
# Put everything together
class Store:
   start_shopping = shop()
   start_shopping.grocery_list()
      
