import json
import os

JSON_FILE = "DailyTasks.json"
NOTES_FILE = "notebook.txt"

class ToDoListApp:

    def __init__(self):
        self.tasks = self.load_file()

    def load_file(self):
        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, "r") as file:
                return json.load(file)
        else:
            return []
        
    def save_file(self):
        with open(JSON_FILE, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task, editing_task_index):        
        if editing_task_index is None:
            self.tasks.append({"task_item": task, "done": False})
        else:
            self.tasks[editing_task_index] = {"task_item": task, "done": False}
        self.save_file()

    def get_tasks(self):
        return self.tasks
    
    def mark_task(self, marked):
        self.tasks[marked]["done"] = not self.tasks[marked]["done"]
        self.save_file()

    def remove_task(self,selected):
        self.tasks.pop(selected)
        self.save_file()
    
    def load_notes(self):
        try:
            if os.path.exists(NOTES_FILE): 
                with open(NOTES_FILE, "r", encoding="utf-8") as f: 
                    notes = f.read().strip() 
                    return notes
            return ""
        except FileNotFoundError:
            return ""

    def save_notes(self, text_content): 
        with open(NOTES_FILE, "w", encoding="utf-8") as f: 
            f.write(text_content)
