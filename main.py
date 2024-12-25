import json
import os

# Define the file where tasks will be stored
tasks_file = "tasks.json"


# Load tasks from the file
def load_tasks():
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file, "r") as file:
        return json.load(file)


# Save tasks to the file
def save_tasks(tasks):
    with open(tasks_file, "w") as file:
        json.dump(tasks, file, indent=4)


# Display all tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "[X]" if task["completed"] else "[ ]"
            print(f"{idx}. {status} {task['title']}")


# Add a new task
def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print("Task added successfully!")
    else:
        print("Task title cannot be empty.")


# Update a task
def update_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter task number to update: "))
        if 1 <= task_number <= len(tasks):
            new_title = input("Enter new title: ").strip()
            if new_title:
                tasks[task_number - 1]["title"] = new_title
                print("Task updated successfully!")
            else:
                print("Task title cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Mark a task as complete
def mark_task_complete(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_task_complete(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
