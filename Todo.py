
""" Task blue print and attributes """
class Task:
    #constructor that initializes a task and its description to default value
    def __init__(self, name, description ="no description"):
        self.name = name
        self.description = description
        
""" task blue print and actions """
# import the class: Task
#import Task
class Task_todo:
    #contructor for a task object
    def __init__(self, task_todo:Task):
        self.task_todo = task_todo
        #initially set it to false
        self.task_completed = False
        
    #getter ror task name
    def get_task_name(self):
        return self.task_todo.name
        
    #getter for description
    def get_task_description(self):
        return self.task_todo.description
    
    # setter for nmae
    def set_task_name(self, new_task_name):
        self.task_todo.name=new_task_name
        return self.task_todo.name
    
    #setter for description
    def set_task_description(self, new_task_description):
        self.task_todo.description = new_task_description
        return self.task_todo.description
    
    
    # check if task is completed
    def is_completed(self):
        return self.task_completed


""" Create a Todo list """
# imoort the class: Task_todo
#import Task_todo
class Todo_List:
    #constructor for a todo list item
    # initializez a dictionary
    def __init__(self,task_todo: Task_todo):
        self.task_todo = task_todo
        self.todo_dict = {}
        
    # method to create a todo item
    def create_todo_list_item(self):
        #prompt for task name
        task = input("Enter task name: ")

        #if nothing was provided simply return
        if not task.strip():
            print("Invalid task")
            return
            
        #assign the task to the name
        try:
            self.task_todo.name = task

        #get the task description
        self.task_todo.description = input("Enter task description: ")
       

        #print test the project
        print(f"Task: {self.task_todo.get_task_name()}\n"
                       f"Description: {self.task_todo.get_task_description()}\n"
                       f"Completed: {self.task_todo.is_completed()}")

    # add task to the dictionary
    self.todo_dict.update(
    self.task_todo.get_task_name(): self.task_todo.get_task_description())
    
     print(f"Dtctinary contents\n")
     for key, value in this.todo_dict.values:
        print(f"Name: {key}, description: {value}")

    # run the project
    if __name__ == "__main__":
        self.create_todo_list_item("Task 1")
    
