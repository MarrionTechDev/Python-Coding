
# =========================
# IMPORTS
# =========================

import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime, timedelta
from ToDoList import ToDoListApp
import random

# =========================
# CONSTANTS
# =========================

DEFAULT_FONT = ("Arial", 11)

# =========================
# APP SETUP
# =========================

root = tk.Tk()
root.title("DailyToDoListApp")
root.resizable(False,False)

# Size and position on Right of desktop
window_width = 390
window_height = 430

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

right_margin = 30
top_margin = 25

x = screen_width - window_width - right_margin
y = top_margin

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

todo = ToDoListApp()

# Tracks which task is being edited.
# None indicates we're creating a new task.
editing_task_index = None


# =========================
# HELPER FUNCTIONS
# ========================

def get_current_date():
    return datetime.now().strftime("%A, %B %d, %Y")

def tasks_to_complete():
    tasks = todo.get_tasks()
    completed_tasks = 0

    for task in tasks:
        if task["done"]:
            completed_tasks += 1
    total_tasks = len(tasks)
    return f"{completed_tasks}/{total_tasks}"

def update_task_count():
    task_count_label.config(
        text=f"{tasks_to_complete()} completed")
    
def load_notes():
    notes = todo.load_notes()
    notebox.insert(tk.END, notes)

def save_notes():
    full_text = notebox.get("1.0", tk.END)
    todo.save_notes(full_text)

def on_closing():
    save_notes()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)

# =========================
# BUTTON FUNCTIONS
# =========================

def load_and_refresh_tasks():

    listbox.delete(0, tk.END)

    tasks = todo.load_file()

    completed_tasks = 0

    for i, task in enumerate(tasks, start = 1):
        if task["done"]:
            status = "✔"
            completed_tasks += i
        else:
            status = " "
        listbox.insert(tk.END, f"{i}) [{status}] {task['task_item']}")
        update_task_count()

def add_on_press(event=None):
    global editing_task_index
    if editing_task_index == None:
        task = task_input.get()
        if task == "":
            return
        listbox.insert(tk.END,f"[ ] {task}")
        task_input.delete(0,tk.END)
        listbox.see(tk.END)
        update_task_count()
    else:
        task = task_input.get()
        listbox.delete(editing_task_index)
        listbox.insert(editing_task_index,f"[ ] {task}")
        task_input.delete(0,tk.END)
        listbox.see(editing_task_index)
        
    todo.add_task(task, editing_task_index)
    editing_task_index = None
    load_and_refresh_tasks()

def toggle_day():
    global current_day_offset

def delete_selected(event=None):
    selected = listbox.curselection()
    if not selected:
        return
    index = selected[0]
    listbox.delete(index)
    todo.remove_task(index)
    update_task_count()
    load_and_refresh_tasks()

def edit_selected(event=None):
    global editing_task_index
    selected = listbox.curselection()
    if not selected:
        return
    editing_task_index = selected[0]
    editing_task = listbox.get(editing_task_index)
    editing_task = editing_task[4:]
    print(editing_task)

    task_input.delete(0, tk.END)
    task_input.insert(0, editing_task)

def on_double_click(event):
    selection = listbox.curselection()
    if selection:
        marked = selection[0]
        todo.mark_task(marked)
        load_and_refresh_tasks()

def random_task():
    tasks = todo.get_tasks()
    if tasks:
        random_index = random.randrange(len(tasks))
        listbox.see(random_index)
        listbox.selection_clear(0, "end")
        listbox.selection_set(random_index)

        # Clear hightlight after 10s
        listbox.after(10000, lambda:listbox.selection_clear(0, "end"))

# =========================
# GUI CREATION
# =========================

# Date and Task Completion frame
top_frame = tk.Frame(root)
top_frame.pack(pady=6)

task_count_label = tk.Label(top_frame, text="0/0 completed", font=("Arial",10))
task_count_label.pack(side=tk.RIGHT)

# Listbox and Scrollbar list frame
task_frame = tk.Frame(root)
task_frame.pack(side="top", fill="both", expand=True, padx=15, pady=10)

# Listbox to display tasks with scrollbar
scrollbar = tk.Scrollbar(task_frame)

listbox = tk.Listbox(task_frame, height=7, yscrollcommand=scrollbar.set, font=DEFAULT_FONT)

scrollbar.config(command=listbox.yview)
scrollbar.pack(side="right", fill="y")
listbox.pack(side="left", fill="x", expand=True, padx=(0, 5))


# Notes
notebox = scrolledtext.ScrolledText(root, font=DEFAULT_FONT, wrap=tk.WORD, width= 40, height=10)
notebox.pack(padx=10, pady=5)

# Task input frame
input_frame = tk.Frame(root)
input_frame.pack(fill="x", padx=20)

# Task label
input_label = tk.Label(input_frame, text = "Enter task:", font=("Arial",10))
input_label.pack(side="left", padx=(0, 5))

# Button frame
bottom_frame = tk.Frame(root)
bottom_frame.pack(side='bottom', padx=15, pady=5)

# Entry for task input
task_input = tk.Entry(input_frame, width=15)
task_input.pack(side="left",fill="x",expand=True)

# Date
date_label = tk.Label(top_frame, text= get_current_date(), font=("Arial", 10, "bold"))
date_label.pack(side="right", padx=20)

    
# =========================
# EVENT BINDINGS
# =========================

task_input.bind("<Return>", add_on_press)
listbox.bind("<Double-Button-1>", on_double_click)

# =========================
# BUTTONS
# =========================

add_btn = tk.Button(bottom_frame, text = "Add", width= 6, command = add_on_press)
add_btn.pack(side="left", padx=4)

delete_btn = tk.Button(bottom_frame, text = "Delete", width= 6, command = delete_selected)
delete_btn.pack(side="left", padx=4)

edit_btn = tk.Button(bottom_frame, text = "Edit", width= 6, command = edit_selected)
edit_btn.pack(side="left", padx=4)

random_btn = tk.Button(bottom_frame, text = "Random Task", width=12, command = random_task)
random_btn.pack(side="left", padx=4)


# =========================
# INITIALIZATION
# =========================

load_and_refresh_tasks()
load_notes()

# =========================
# MAIN LOOP
# =========================

root.mainloop()

