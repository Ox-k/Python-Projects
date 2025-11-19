""" task blue print and actions """
class Task_todo:
    #contructor for a task object
    def __init__(self, task_todo:Task):
        self.task_todo = task_todo
        #initially set it to false
        self.task_completed = false
        
    #getter ror task name
    def get_task_name(self):
        return self.task_todo.name
        
    #getter for description
    def get_task_description(self):
        return self.task_todo.description
    
    # setter for nmae
    def set_task_name(self, new_task_name):
        return 
        self.task_todo.name=new_task_name
    
    #setter for description
    def set_task_description(
        self, new_task_description):
        return self.task_todo.description
        = new_task_description
    
    
    # check if task is completed
    def is_completed(self) -> bool:
        return self.task_completed



""" Task blue print and attributes """
class Task:
    #constructor that initializes a task and its description to default value
    def __init__(self, name, description ="no description"):
        self.name = name
        self.description = description






""" Create a Todo list """
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
        print(f"Task: {self.task_todo.get_task_name()}\n
                       Description: {self.task_todo.get_task_description()}\n
                       Completed: {self.task_todo.is_completed()}")

    # test method 
    def test_project():
        create_todo_list_item()

    # run the project
    if __main__ == "__main__":
        test_project()
    
