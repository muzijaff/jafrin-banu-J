import tkinter as tk
from tkinter import messagebox
class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []
        
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)
        add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_task_button.grid(row=0, column=1, padx=10, pady=10)
        
        remove_task_button = tk.Button(root, text="remove Task", command=self.remove_task)
        remove_task_button.grid(row=1, column=1, padx=10, pady=10)
        
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10)
        
        self.refresh_tasks()
        
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.refresh_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("warning","please enter a task")
    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.refresh_tasks()
        except IndexError:
            messagebox.showwarning("warning", "please remove any task")
    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
def main():
    try:
        root = tk.Tk()
        TodoListApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An error occured: {str(e)}")
if __name__== "__main__":
    main()
                