projects = {}

class Project:
    """
    Represents a project containing tasks.
    
    Attributes:
    - name (str): Name of the project.
    - tasks (list): List of tasks in the project.
    """
    
    def __init__(self, name):
        self.name = name
        self.tasks = []
        projects.setdefault(name, self)

    def add_task(self, task):
        self.tasks.append(task)

    #return all tasks in the project
    def view_tasks(self):
       return self.tasks

    def remove_task(self, task):
        self.tasks.remove(task)

    def clear_tasks(self):
        self.tasks = []


class Task:

    def __init__(self, description, project=None):
        self.description = description
        if project is None:
            self.project = projects.get('General', Project('General'))
        else:
            self.project = project
        self.project.add_task(self)

    def view_task(self):
        return self.description
    
    def view_project(self):
        return self.project.name
    

# Create a task with a project
project1 = Project("Project 1")
task = Task("Task 1", project1)

# Create a task without a project
task2 = Task("Task 2")
task3 = Task("Task 3")

# print all projects and their tasks
print("Projects and their tasks:")
for project in projects.values():
    print(f"Project: {project.name}")
    for task in project.view_tasks():
        print(f"Task: {task.view_task()}")
