
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime, timedelta

# ==== GUI Setup ====
root = tk.Tk()
root.title("DailyToDoListApp")
root.geometry("400x410")

# Date and Task Completion frame
top_frame = tk.Frame(root)
top_frame.pack(fill=tk.X, padx=10, pady=5)

task_count_label = tk.Label(top_frame, text=" 1/3 completed", font= ("Arial",10))
task_count_label.pack(side=tk.RIGHT)

# Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Listbox to display tasks
listbox = tk.Listbox(root, width=40, height= 7, yscrollcommand=scrollbar.set, font = ("Arial",11))
listbox.pack(fill="x", expand=True, padx=5, pady=5)

# Textbox
notebox = scrolledtext.ScrolledText(root, font=("Arial", 11), wrap=tk.WORD, width= 40, height=10)
notebox.pack(padx=10, pady=8)

# Add the scrollbar to listbox
scrollbar.config(command=listbox.yview)

# Task input and button frame
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.X, padx=10, pady=10)

# Entry for task input
task_input = tk.Entry(bottom_frame, width = 25)
task_input.pack(side=tk.LEFT, fill=tk.X, expand=True)


# Tracks which task is being edited.
# None indicates we're creating a new task.
editing_task_index = None

# BUTTON FUNCTIONS
def get_current_date():
    return datetime.now().strftime("%A, %B %d, %Y")


def add_on_press(event=None):
    global editing_task_index

    if editing_task_index == None:
        output = task_input.get()

        if output == "":
            return
        listbox.insert(tk.END,output)
        task_input.delete(0,tk.END)

    else:
        output = task_input.get()
        print(editing_task_index)

        listbox.delete(editing_task_index)
        listbox.insert(editing_task_index,output)
        task_input.delete(0,tk.END)
        editing_task_index = None


def delete_selected(event=None):
    selected = listbox.curselection()
    if not selected:
        return
    index = selected[0]
    listbox.delete(index)


def edit_selected(event=None):
    global editing_task_index
    selected = listbox.curselection()
    if not selected:
        return
    editing_task_index = selected[0]
    editing_task = listbox.get(editing_task_index)

    task_input.delete(0, tk.END)
    task_input.insert(0, editing_task)

    
task_input.bind("<Return>", add_on_press)


# Buttons
add_btn = tk.Button(bottom_frame, text = "Add", width= 6, command = add_on_press)
add_btn.pack(side=tk.LEFT, padx= 3)

delete_btn = tk.Button(bottom_frame, text = "Delete", width= 6, command = delete_selected)
delete_btn.pack(side=tk.LEFT,padx= 3)

checked_btn = tk.Button(bottom_frame, text = "Check", width= 6, command = add_on_press)
checked_btn.pack(side=tk.LEFT, padx= 3)

edit_btn = tk.Button(bottom_frame, text = "Edit", width= 6, command = edit_selected)
edit_btn.pack(side=tk.LEFT, padx= 3)

date_label = tk.Label(top_frame, text= get_current_date(), font=("Arial", 10, "bold"))
date_label.pack(side="right", padx= 20)

root.mainloop()
