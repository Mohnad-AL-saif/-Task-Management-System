"# -Task-Management-System" 
Project Explanation: Task Management System

This project is a simple Task Management System that allows users to add tasks to a list, mark tasks as complete, view the tasks, and quit the program. The project is implemented using Python.

The project starts by initializing a list called `tasks`. Each task in the list is represented by a dictionary with two keys: "task" (representing the task description) and "completed" (a boolean value indicating whether the task is completed or not).

The main functionality of the project is implemented in the `main()` function. It displays a menu to the user with four options: add a task, mark a task as complete, view the tasks, and quit the program.

1. Add Task:
   - The `add_task()` function is called when the user selects the option to add a task.
   - The user is prompted to enter the task description.
   - A new dictionary is created with the task description and a default value of `False` for the "completed" key.
   - The new task dictionary is appended to the `tasks` list.
   - A success message is printed to indicate that the task has been added.

2. Mark Task as Complete:
   - The `mark_task_complete()` function is called when the user selects the option to mark a task as complete.
   - It first checks if there are any incomplete tasks in the `tasks` list.
   - If there are no incomplete tasks, a message is printed to indicate that there are no tasks to mark as complete.
   - Otherwise, the incomplete tasks are displayed to the user, along with their corresponding numbers.
   - The user is prompted to enter the number of the task they want to mark as complete.
   - The input is validated to ensure it is a valid number within the range of the incomplete tasks.
   - The selected task is marked as complete by updating the value of the "completed" key to `True`.
   - A message is printed to indicate that the task has been marked as complete.

3. View Tasks:
   - The `view_tasks()` function is called when the user selects the option to view the tasks.
   - If there are no tasks in the `tasks` list, a message is printed to indicate that there are no tasks to view.
   - Otherwise, each task in the `tasks` list is displayed along with its corresponding number and a status indicator (✔️ for completed tasks, ❌ for incomplete tasks).

4. Quit:
   - If the user selects the option to quit, the program breaks out of the while loop in the `main()` function, and the program terminates.

The project demonstrates the use of functions, lists, dictionaries, loops, conditionals, and user input handling to create a basic Task Management System. Users can add tasks, mark them as complete, view the tasks, and exit the program.

