class ToDoList:
    def __init__(self):
        self.tasks = {}
    def display_tasks(self):
        print("\nTo-Do List:")
        for task_id, task in self.tasks.items():
            status = "Done" if task["completed"] else "Pending"
            print(f"{task_id}. {task['name']} - {status}")
    def add_task(self):
        task_name = input("Enter task name: ")
        self.tasks[len(self.tasks) + 1] = {"name": task_name, "completed": False}
        print("Task added successfully!")
    def update_task(self):
        self.display_tasks()
        task_id = int(input("Enter task ID to update: "))
        if task_id in self.tasks:
            task_status = input("Mark as (D)one or (P)ending? ").upper()
            if task_status == "D":
                self.tasks[task_id]["completed"] = True
            elif task_status == "P":
                self.tasks[task_id]["completed"] = False
            print("Task updated successfully!")
        else:
            print("Invalid task ID.")
    def delete_task(self):
        self.display_tasks()
        task_id = int(input("Enter task ID to delete: "))
        if task_id in self.tasks:
            del self.tasks[task_id]
            print("Task deleted successfully!")
        else:
            print("Invalid task ID.")
def main():
    todo = ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            todo.display_tasks()
        elif choice == "2":
            todo.add_task()
        elif choice == "3":
            todo.update_task()
        elif choice == "4":
            todo.delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()



