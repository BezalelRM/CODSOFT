import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        tk.Button(root, text="Add Task", width=15, command=self.addfunc).pack(pady=5)

        tk.Button(root, text="Mark as Done", width=15, command=self.markfunc).pack()

        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.status)

        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=5)

        tk.Button(root, text="Delete Selected Task", width=20, command=self.delete).pack(pady=5)

    def addfunc(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.updatelist()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter a task.")

    def delete(self):
        selected = self.listbox.curselection()
        if selected:
            del self.tasks[selected[0]]
            self.updatelist()
            self.status_label.config(text="")

    def markfunc(self):
        selected = self.listbox.curselection()
        if selected:
            i = selected[0]
            self.tasks[i]["done"] = not self.tasks[i]["done"]
            self.updatelist()
            self.status()

    def updatelist(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            mark = "[✓] " if task["done"] else "[ ] "
            self.listbox.insert(tk.END, mark + task["task"])

    def status(self, event=None):
        selected = self.listbox.curselection()
        if selected:
            task = self.tasks[selected[0]]
            status = "Status: Done ✅" if task["done"] else "Status: Not Done ⏳"
            self.status_label.config(text=status)

root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
