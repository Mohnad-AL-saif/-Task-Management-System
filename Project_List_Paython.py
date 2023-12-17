# 1- add task to list
# 2- mark task as complete
# 3- view tasks
# 4- Quit
tasks = [{"task":"Quran", "completed":True}, {"task":"Salah", "completed":True}, 
         {"task":"Study", "completed":False}, {"task":"Exercise", "completed":True}, 
         {"task":"Sleep", "completed":False}, {"task":"Visit Hamada", "completed":True}]


def main():
    message = '''1 - add tasck to list
2- mark task as complete
3- view tasks
4- Quit'''


    while True:
        print(message)
        choice = input("Enter your choice: ")

        if choice == "1":
            # add task to tasks list
            add_task()
        elif choice == "2":
            mark_task_complete()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            break
        else:
            print("invalid choice, please enter a number between 1 and 4")
    
def add_task():
    # get task from user
    task =input("Enter task: ")
    # difline task status
    task_info={"task":task, "completed" : False}
    # add task to the list of tasks 
    tasks.append(task_info)
    print("Task added to the list successifuly")

def mark_task_complete():
    # get list of incomplete tasks
    incomplete_tasks = [task for task in tasks if task["completed"] == False]
    
    if not incomplete_tasks:
        print("no tasks to mark as complete: ")
        return


    # show them to the user 
    for i, task in enumerate(incomplete_tasks):
        print(f'{i+1}- {task["task"]}')
        print("-"*30)
        
    # get the task from the user
    try:
        task_number = int(input("choos the task number to complete: "))

        if task_number < 1 or task_number >len(incomplete_tasks):
            print("invalid Task Number")
            return
        # mark the task as completed
        incomplete_tasks[task_number - 1]["completed"] = True

        # print a message to the uesr
        print("Task marked completed")
    except ValueError:
        print("invalid input, please enter a numbar")
    except IndexError:
        print("Plase choose from the available tasks")
def view_tasks():
    # if there are no tasks, print messag and return
    if not tasks: 
        print("No tasks to view")
        return

        
    

    for i, task in enumerate(tasks):
        status = "✔️" if task["completed"] else "❌"

        print(f'{i+1}. {task["task"]} {status}')


    # 1.Read quran ✔️
    # 2.salah ✔️
    # 3.visit muhannad ❌
    
    
main()