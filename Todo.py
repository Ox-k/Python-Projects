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