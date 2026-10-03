import json
import os

class TaskManager:
    def __init__(self,filename="tasks.json"):
        self.filename = filename
        self.tasks = self._load_tasks()

    def _load_tasks(self)-> list:
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename,"r") as f:
                return json.load(f)
        except (json.JSONDecodeError,IOError):
            return []

    def _save_tasks(self):
        try:
            with open(self.filename,"w") as f:
                json.dump(self.tasks,f,indent=4)
        except IOError:
            print("Error saving a file.")

    def add_task(self,task:str):
        task = {"id":len(self.tasks)+1,"title":task,"completed":False}
        self.tasks.append(task)
        self._save_tasks()
        print(f"Task added: {task['title']}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("\n----TO-DO LIST----")
        for task in self.tasks:
            status = "Done" if task["completed"] else "Pending"
            print(f"{task['id']}. {task['title']} - {status}")

    def mark_task_completed(self,task_id:int):
        for task in self.tasks:
            if task["id"]==task_id:
                task["completed"]=True
                self._save_tasks()
                print(f"Task marked as completed: {task['title']}")
                return
        print(f"No task found with ID: {task_id}")

    def delete_task(self,task_id : int):
        for task in self.tasks:
            if task["id"]==task_id:
                self.tasks.remove(task)

                for idx,item in enumerate(self.tasks,1):
                    item["id"]=idx
                self._save_tasks()
                print(f"Task deleted: {task['title']}")
                return
        print(f"No task found with ID: {task_id}")

def main():
    task_manager = TaskManager()

    while True:
        print("\n---TO-DO-LIST MENU---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice(1-5): ").strip()
        if choice == "1":
            task_title = input("Enter task title : ").strip()
            if task_title:
                task_manager.add_task(task_title)
            else:
                print("Task title cannot be empty.")
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark as completed : "))
                task_manager.mark_task_completed(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete : "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()