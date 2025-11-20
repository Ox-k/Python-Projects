class Item:
    def __init__(self, name="unknown", description = "no description"):
        self.name = name
        self.description = description
    def get_item_name(self):
        return self.name

    def get_description(self):
        return self.description

    def change_name(self, new_name):
        self.name = new_name
        return self.name

    def change_description(self, new_description):
        self.description = new_description
        return self.description

class Create_item:
    def __init__(self):
        pass
        
    def get_item_details(self):
        item_name = input("Enter the item name: ")
        if not item_name.strip():
            print("No name was provided")
            return 
        
        item_description = input("Enter the item description: ")
        item = Item(item_name, item_description)

        print(f"Item: {item.get_item_name()}")
        print(f"Description: {item.get_description()}")

        ask_user = input("Would you like make any changes to the item: ")
        if not ask_user.strip():
            print("Well alirght then 😊")
            return
            
        ask_user = int(ask_user)
        
        if ask_user == 1:
            new_name = input("Enter the new name: ")
            if not new_name.strip():
                print("Nothing was changed")
                return
            item.change_name(new_name)
        elif ask_user == 2:
            new_description = input("Enter the new description: ")
            if not new_description.strip():
                print("Nothing was changed")
                return
            item.change_description(new_description)
        print(f"Item (new): {item.get_item_name()}")
        print(f"Description (new): {item.get_description()}")

        return item

class Todo_list:
    def __init__(self):
        self.items = {}

    def add_items(self):
        create_item = Create_item()
        still_adding = input("Enter NO to quit")
        while still_adding != "NO":
            todo_list_item = create_item.get_item_details()
            if todo_list_item is None:
                print("Item was not created — skipping.")
                still_adding = input("Enter NO to quit: ")
                continue
                
            name = todo_list_item.get_item_name()
            description = todo_list_item.get_item_description()
            #self.items.update(name: description)
            self.items.update({name: description})
            # Ask again
            still_adding = input("Enter NO to quit: ")

        for key, value in self.items.items():
            print(f"Item: {key} -> Value: {value}")

            """
            Current bugs:
            dictionary is not printing
            Possibke cause: items are never added to it when i ask the user for changes
            investigate more
            """
            
            
if __name__ == "__main__":
    todo = Todo_list()
    todo.add_items()
