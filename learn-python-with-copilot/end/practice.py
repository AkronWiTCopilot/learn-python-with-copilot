# Task 1: Learning Relevant Python Concepts
print("Hello, world!")

x = 5

if x == 5:
    print("x is 5.")

for i in range(10):
    print(i)

# Task 2: Data types in Python
tasks = ["Task 1", "Task 2", "Task 3"]
print(tasks)

# Add a task to the list
tasks.append('Task 4')

# View tasks in the list
print(tasks)  # Outputs: ['Task 1', 'Task 2', 'Task 3', 'Task 4']
print(tasks[0])  # Outputs: Task 1

# Remove a task from the list
tasks.remove('Task 1')  # removes 'Task 1' from the list
print(tasks)  # Outputs: ['Task 2', 'Task 3', 'Task 4']

tasks.pop(0)  # removes the first task from the list
print(tasks)  # Outputs: ['Task 3', 'Task 4']

# Task 3: Classes and Methods in Python
class MyClass:
    def greet(self, name):
        return f"Hello, {name}!"
    
# Create an instance of MyClass
my_instance = MyClass()

# Call the greet function
greeting = my_instance.greet("Jane")

print(greeting)  # Outputs: Hello, Your Name!