import tkinter as tk
from tkinter import messagebox, ttk
import datetime

def add_task():
    task = task_entry.get()
    category = category_dropdown.get()
    priority = priority_dropdown.get()
    deadline = deadline_entry.get()

    if task:
        task_info = f"{task} | {category} | {priority} | {deadline}"
        tasks_listbox.insert(tk.END, task_info)
        task_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def complete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, f"[Completed] {task}")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

root = tk.Tk()
root.title("To-Do List")
root.geometry("600x600")
root.configure(bg="#f0f4f8")

style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 14),
                padding=8,
                relief="flat",
                background="#2C3E50",  
                foreground="#000000")  
style.map("TButton", background=[("active", "#34495E")]) 

frame = tk.Frame(root, bg="#f0f4f8")
frame.pack(pady=20)

task_label = tk.Label(frame, text="Enter Task:", font=("Helvetica", 12), bg="#f0f4f8")
task_label.grid(row=0, column=0, padx=10, pady=10)
task_entry = tk.Entry(frame, width=40, font=("Helvetica", 16), bg="#ffffff", fg="#333333", relief="solid", bd=2)
task_entry.grid(row=1, column=0, padx=10, pady=10)

category_label = tk.Label(frame, text="Category:", font=("Helvetica", 12), bg="#f0f4f8")
category_label.grid(row=0, column=1, padx=10, pady=10)
category_dropdown = ttk.Combobox(frame, values=["Work", "Personal", "Urgent"], width=15, font=("Helvetica", 14))
category_dropdown.grid(row=1, column=1, padx=10, pady=10)
category_dropdown.set("Personal")

priority_label = tk.Label(frame, text="Priority:", font=("Helvetica", 12), bg="#f0f4f8")
priority_label.grid(row=0, column=2, padx=10, pady=10)
priority_dropdown = ttk.Combobox(frame, values=["High", "Medium", "Low"], width=15, font=("Helvetica", 14))
priority_dropdown.grid(row=1, column=2, padx=10, pady=10)
priority_dropdown.set("Medium")

deadline_label = tk.Label(frame, text="Deadline (YYYY-MM-DD):", font=("Helvetica", 12), bg="#f0f4f8")
deadline_label.grid(row=0, column=3, padx=10, pady=10)
deadline_entry = tk.Entry(frame, width=20, font=("Helvetica", 14), bg="#ffffff", fg="#333333", relief="solid", bd=2)
deadline_entry.grid(row=1, column=3, padx=10, pady=10)

add_button = ttk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=1, column=4, padx=10, pady=10)

tasks_listbox = tk.Listbox(root, width=70, height=15, font=("Helvetica", 14), bg="#ffffff", fg="#333333", selectbackground="#4CAF50", selectforeground="#ffffff", relief="solid")
tasks_listbox.pack(pady=20)

buttons_frame = tk.Frame(root, bg="#f0f4f8")
buttons_frame.pack()

complete_button = ttk.Button(buttons_frame, text="Mark as Completed", command=complete_task)
complete_button.grid(row=0, column=0, padx=10, pady=10)

delete_button = ttk.Button(buttons_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=1, padx=10, pady=10)

def alternate_row_colors():
    tasks = tasks_listbox.get(0, tk.END)
    for index, task in enumerate(tasks):
        if index % 2 == 0:
            tasks_listbox.itemconfig(index, {'bg': '#f9f9f9'})
        else:
            tasks_listbox.itemconfig(index, {'bg': '#ffffff'})

def on_add_task():
    add_task()
    alternate_row_colors()

add_button.config(command=on_add_task)

root.mainloop()
