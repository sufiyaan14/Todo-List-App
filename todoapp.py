import tkinter as tk
from tkinter import messagebox, filedialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")

        self.tasks = []

        self.task_entry = tk.Entry(root, font=("Arial", 14))
        self.task_entry.pack(pady=10)

        self.add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_btn.pack()

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Arial", 12), width=40, height=15)
        self.task_listbox.pack(pady=10)

        self.delete_btn = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_btn.pack()

        self.save_btn = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_btn.pack()

        self.load_btn = tk.Button(root, text="Load Tasks", command=self.load_tasks)
        self.load_btn.pack()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        else:
            messagebox.showwarning("Selection Error", "No task selected!")

    def save_tasks(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
        if file:
            with open(file, "w") as f:
                for task in self.tasks:
                    f.write(task + "\n")
            messagebox.showinfo("Success", "Tasks saved successfully!")

    def load_tasks(self):
        file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file:
            with open(file, "r") as f:
                self.tasks = f.read().splitlines()
            self.task_listbox.delete(0, tk.END)
            for task in self.tasks:
                self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
