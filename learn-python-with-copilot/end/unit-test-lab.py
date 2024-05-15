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
       """
       Removes a task from the project.
       
       Args:
       - task (Task): Task to remove.
       
       Returns:
       - None

       :Examples:
         >>> project = Project("Project 1")
         >>> task = Task("Task 1", project)
         >>> project.remove_task(task)
       """
       #Alternative code:
         #if task in self.tasks:
        #   self.tasks.remove(task)
        #else:
        #   raise ValueError("Task not in project")
       self.tasks.remove(task)

    def clear_tasks(self):
        self.tasks = []


class Task:
    def __init__(self, description, project=None):
        self.description = description
        if project is None:
            # If no project is provided, add the task to the General project
            self.project = projects.get('General', Project('General'))
        else:
            self.project = project
        self.project.add_task(self)

    def view_task(self):
        return self.description
    
    def view_project(self):
        return self.project.name
    
    # TODO: Export list of tasks to an excel file
    
"""***************************
Add Tests Below
***************************"""

import unittest
import pytest
from unittest.mock import MagicMock

class TestTask(unittest.TestCase):

    # Test suggestion: Test that a task with no project is added to the General project
    def test_task_with_no_project_is_added_to_general(self):
        task = Task('Test Task')
        self.assertEqual(task.project, projects.get('General', Project('General')))

    # Use Pytest to generate test for the add_task method in the Project class
    @pytest.mark.parametrize('task_description', [
        'Task 1',
        'Task 2'])
    def test_add_task(task_description):
        project = Project('Project 1')
        task = Task(task_description, project)
        assert (task in project.tasks)

# use unittest to generate tests for the remove_task method in the Project class
class TestProject(unittest.TestCase):
    # Test suggestion: Test that a task is removed from the project
    def test_remove_task(self):
        project = Project('Project 1')
        task = Task('Task 1', project)
        project.remove_task(task)
        self.assertNotIn(task, project.tasks)

#use unittest to generate tests for the remove_task function
class TestProject2(unittest.TestCase):
    def setUp(self):
        self.project = Project("Project 1")
        self.task = Task("Test task", self.project)
        self.task2 = Task("Test task 2", self.project)
        self.task3 = Task("Test task 3", self.project)

    def test_remove_task(self):
        self.project.remove_task(self.task)
        self.assertEqual(len(self.project.tasks), 2)
        self.project.remove_task(self.task2)
        self.assertEqual(len(self.project.tasks), 1)
        self.project.remove_task(self.task3)
        self.assertEqual(len(self.project.tasks), 0)

    def tearDown(self) -> None:
        return super().tearDown()

#use magic mock object to test the add_task method
class TestProject3(unittest.TestCase):
    def test_remove_task(self):
    #Create a mock object for the project class using magic mock and populate the tasks list with mock tasks
        project = MagicMock()
        project.tasks = [MagicMock(), MagicMock(), MagicMock()]
        task = MagicMock()
        project.remove_task(task)
        #Check if the task was removed from the project
        self.assertNotIn(task, project.tasks)

# test that the valueerror in the add_task method is raised
class TestProject4(unittest.TestCase):
    def test_exception_raised(self):
        project = Project("Project 1")
        task = Task("Task 1", project)
        with self.assertRaises(ValueError):
         project.remove_task(Task("Task 2"))

