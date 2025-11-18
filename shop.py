class Item:
    # Blueprint class to represent an item

    def __init__(self, itemName, itemPrice, itemQuantity):
        """
        Constructor for item object instances
        """
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.itemQuantity = itemQuantity

    # getting the name of the item
    def getItemName(self):
        print(f"This is the item name: {self.itemName}")
        return self.itemName

    # getting the price of the item
    def getItemPrice(self):
        print(f"This is the item price: {self.itemPrice}")
        return self.itemPrice

    # getting the item quantity
    def getItemQuantity(self):
        print(f"This is the item quantity: {self.itemQuantity}")
        return self.itemQuantity

    # changing the existing quantity of items
    def changeItemQuantity(self):
        # ask shopper if they want to add or subtract
        change = input("Do you want to\n1. Add?\n2. Subtract ? ")

        if not change.strip():
            print("You did not choose an option")
            return self.itemQuantity

        try:
            change = int(change)
        except ValueError:
            print("Invalid option")
            return self.itemQuantity

        if change == 1:
            addition_qty = input("Enter number of items to add: ")

            if not addition_qty.strip():
                print("No items were added.")
                return self.itemQuantity

            try:
                addition_qty = int(addition_qty)
            except ValueError:
                print("Invalid quantity")
                return self.itemQuantity

            self.itemQuantity += addition_qty
            return self.itemQuantity

        elif change == 2:
            subtraction_qty = input("Enter number of items to subtract: ")

            if not subtraction_qty.strip():
                print("No items were subtracted.")
                return self.itemQuantity

            try:
                subtraction_qty = int(subtraction_qty)
            except ValueError:
                print("Invalid quantity")
                return self.itemQuantity

            self.itemQuantity = max(0, self.itemQuantity - subtraction_qty)
            return self.itemQuantity

        else:
            print("Invalid option")
            return self.itemQuantity

    def get_total_per_item(self):
        return self.itemPrice * self.itemQuantity


class Cart:
    """Represents a shopping cart holding multiple Item objects."""

    def __init__(self, cart_total=0):
        self.cart_total = cart_total
        self.item_list = []

    def add_toCart(self, item: Item):
        """Adds an Item object to the cart."""
        self.item_list.append(item)
        print("This is the status of the list")
        for itm in self.item_list:
            print(f"{itm.itemName} - qty {itm.itemQuantity} - price {itm.itemPrice}")

    def calc_total_per_item(self):
        """Print total price for each item and return list of totals."""
        totals = []
        for item in self.item_list:
            total = item.get_total_per_item()
            print(f"{item.itemName} : total per item {total}")
            totals.append(total)
        return totals

    def calc_cart_total(self):
        total = sum(item.get_total_per_item() for item in self.item_list)
        print(f"Cart total = {total}")
        return total


class Shop:
    # ask user to add items
    def grocery_list(self):
        # get item name
        item_name = input("What item do you want?: ")

        # get the price...assume user will enter valid price
        item_price = float(input("Enter its price in the format 00.00: $"))

        # get the quantity..... assume user will enter valid number
        item_quantity = int(input(f"How many {item_name}(s) do you want to purchase?: "))

        # create item object
        item = Item(item_name, item_price, item_quantity)
        print(f"Item: name -> {item.itemName}, price -> {item.itemPrice}, quantity -> {item.itemQuantity}")

        print("Initializing cart ...... ")
        cart = Cart()
        cart.add_toCart(item)
        print("Items in the cart:")
        cart.calc_total_per_item()
        cart.calc_cart_total()
        return cart


if __name__ == "__main__":
    Shop().grocery_list()
