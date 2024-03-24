


In this article, we'll explore **Tkinter**, a renowned GUI toolkit for Python, and leverage its features to develop a comprehensive **to-do list application**. I'll guide you through crafting a **user-friendly interface** and implementing essential functions such as **task creation**, **deletion**, and **prioritization**.

# Brief Overview of Tkinter
Tkinter, a popular Python library, makes GUI creation straightforward. It enables you to design interactive applications easily by providing tools for windows, buttons, labels, text boxes, and more.

Feel free to check out this article to discover more about [advanced Tkinter concepts][1].

# What is a To-Do List?

A to-do list serves as your personal task manager, allowing you to jot down everything from groceries to buy, assignments to complete, or calls to make. It keeps you organized, aiding in prioritization, focus, and a sense of accomplishment as tasks are checked off one by one.

This article will guide you through the process of creating an interactive to-do list using Tkinter, enabling you to effectively manage your tasks.

# Project Prerequisites

Before starting to build a to-do list app with Tkinter, make sure you have the following:

- Python Installed: Have Python installed on your computer. Tkinter comes included with Python, so no separate installation is needed.
  - **For Windows**: Download and install Python from the [official website][2].
  - **For Ubuntu**: You can download Python using the terminal:
  
		sudo apt update
		sudo apt install python3
  - **For MacOS**: You can download Python using Homebrew:

		brew install python3
	
To confirm the installation, enter `python3 --version` in the terminal.

- Text Editor or IDE: Select a preferred text editor or IDE, such as Visual Studio Code or PyCharm, to write and execute Python code.
- Tkinter Basics: Basic familiarity with Tkinter, including widgets and event handling, can be useful. You can learn through [Tkinter documentation][3] or [this article][4].

<div class="div-blue"> <span class="alert-header">Note:</span> <span class="alert-body"> This project assumes familiarity with Python fundamentals.</span> </div>

# Designing the User Interface

**Importing necessary Libraries**
Tkinter (`tk`) is the go-to module for GUI applications, complemented by `ttk` for themed widgets, offering a modern appearance. Utilizing the `messagebox` module enables the display of user interaction messages. Additionally, SQLite3, a lightweight database engine, handles local data storage and management for our tasks.

	import tkinter as tk
	from tkinter import ttk, messagebox
	import sqlite3

**Creating the Main Window**
We create the main window using Tkinter, set its size, and instantiate the `TodoListApp` class (discussed later) to integrate its functionalities. Finally, we start the event loop for user interaction.

	window = tk.Tk()
	window.geometry("457x335")
	app = TodoListApp(window)
	window.mainloop()

**Adding a Title and necessary Frames and Labels**
You can add a catchy title to your To-Do app. I have named it "Todo List App". The app features two frames: one for entering new tasks and another for displaying existing ones. The new task frame includes labels for "Task Name," "Priority," and "Deadline."

	self.window = window
	window.title("Todo List App")
	entry_frame = ttk.Frame(self.window)
    entry_frame.pack(padx=10, pady=10, fill=tk.X)
    ttk.Label(entry_frame, text="Task name:").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(entry_frame, text="Priority:").grid(row=1, column=0, padx=5, pady=5)
    ttk.Label(entry_frame, text="Deadline:").grid(row=2, column=0, padx=5, pady=5)
    self.task_list_frame = ttk.Frame(self.window)
    self.task_list_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

**Adding Widgets for Task Entry**
To add a new task, provide the task name, priority, and deadline. All tasks require a name and set priority. For urgent tasks, a deadline is mandatory.

	self.task_text = tk.StringVar()
    self.task_entry = ttk.Entry(entry_frame, textvariable=self.task_text)
    self.task_entry.grid(row=0, column=1, padx=5, pady=5)
    ttk.Radiobutton(entry_frame, text="Urgent", variable=self.priority_selection, value="Urgent").grid(row=1, column=1, padx=5, pady=5)
    ttk.Radiobutton(entry_frame, text="General", variable=self.priority_selection, value="General").grid(row=1, column=2, padx=5, pady=5)
    self.task_deadline = tk.StringVar()
    self.deadline_entry = ttk.Entry(entry_frame, textvariable=self.task_deadline)
    self.deadline_entry.grid(row=2, column=1, padx=5, pady=5)


This code snippet sets up the entry interface for users to input task details. It includes entry fields for users to specify the task name, radio buttons to specify the priority level (either "Urgent" or "General"), and another entry field for the deadline.

**Adding Buttons**
You will need 2 buttons to be included: one for adding a new task and another for deleting an existing task.

	add_button = ttk.Button(entry_frame, text="Add Task", command=self.add_task)
    add_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
    delete_button = ttk.Button(self.window, text="Delete Tasks", command=self.delete_tasks)
    delete_button.pack(pady=5)
Here, the first button, "Add Task," triggers the `add_task` method when clicked. The second button, "Delete Tasks," triggers the `delete_tasks` method upon activation.

**Displaying the List of Entered Tasks**
Every task entered into the database table is retrieved and processed. A separate frame is generated for each task, within which labels are utilized to showcase the task details. Furthermore, a checkbutton is included for every task, enabling users to mark tasks as complete once they are fulfilled.

	for task in tasks:
            task_id = task[0]
            task_text = task[1]
            task_priority = task[2]
            task_deadline = task[4]
            task_frame = ttk.Frame(self.task_list_frame)
            task_frame.pack(fill=tk.X, padx=5, pady=2)
            task_checkbutton = ttk.Checkbutton(task_frame, command=lambda id=task_id: self.select_task(id))
            task_checkbutton.grid(row=0, column=0)
            if task_priority == "Urgent" or (task_priority == "General" and task_deadline):
                task_label = ttk.Label(task_frame, text=(task_text+"    ("+task_deadline+")"))
            else:
                task_label = ttk.Label(task_frame, text=task_text)
            task_label.grid(row=0, column=1, padx=5)
For each task, relevant details like `ID`, `task`, `priority`, and `deadline` are extracted. Frames are created to organize task information neatly. `task_checkbutton` enable task completion marking, while task names are displayed as Labels. If urgent or with a deadline, task names include this information.

This represents the expected appearance of the GUI:

![todo_gui][5]

<div class="div-green"> <span class="alert-header">Tip:</span> <span class="alert-body"> Customize labels with different colors based on task priorities. See code at the end.</span> </div>


# Implementing Functionality

The following functions are defined in the `TodoListApp` class.

<div class="div-green"> <span class="alert-header">Tip:</span> <span class="alert-body"> It is best to encapsulate multiple functions in a class.</span> </div>

**Create a Table in the SQLite Database**
To store your tasks effectively, a database is necessary. We will proceed by creating a table within an SQLite database for this purpose.

	    self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
	                        id INTEGER PRIMARY KEY AUTOINCREMENT,
	                        task TEXT NOT NULL,
	                        priority TEXT,
	                        initial_priority TEXT,
	                        deadline TEXT
	                    )''')
	    self.conn.commit()
The `create_table` function sets up a table named `tasks` in the SQLite database. It includes columns for task details such as `ID`, `task` (name), `priority`, `initial priority`, and `deadline`. This function ensures that the necessary table structure exists for storing task information and commits the changes to the database.

<div class="div-red"> <span class="alert-header">Caution:</span> <span class="alert-body"> Ensure that there is no existing table named `tasks` in the database as it may lead to data loss or corruption if the existing table structure is overwritten or altered unintentionally.</span> </div>

**Function to Add Tasks**
To add a new task, provide the task name, priority, and deadline. All tasks require a name and set priority. For urgent tasks, a deadline is mandatory.

        task_text = self.task_text.get().strip()
        task_priority = self.priority_selection.get()
        task_deadline = self.task_deadline.get().strip()
        if task_text and (task_priority == "General" or (task_priority == "Urgent" and task_deadline)):
            self.c.execute("INSERT INTO tasks (task, priority, initial_priority, deadline) VALUES (?, ?, ?, ?)", (task_text, task_priority, task_priority, task_deadline))
            self.conn.commit()
            self.load_tasks()
            self.task_text.set("")
            self.priority_selection.set("")
            self.task_deadline.set("")
        else:
            messagebox.showwarning("Warning", "Task or Priority cannot be empty, and Urgent task must have a deadline.")
It collects task details from input fields. If the name isn't empty and the priority is valid, the task is added to the database. After insertion, the task list refreshes, and input fields reset. If inputs are invalid, a warning message appears.

If task name or priority or deadline for an urgent task is not entered:

![todo_error_insert][6]

After successfully entering a task:

![todo_insert][7]

**Function to Delete Tasks**
To delete tasks, you click the "Delete Tasks" button, opening a window where you select tasks for removal. At least one task must be chosen before clicking "Delete." After confirmation, the selected tasks are deleted from the SQLite table.

This opens a Toplevel window:  

        delete_window = tk.Toplevel(self.window)
        delete_window.geometry("457x335")
        delete_window.title("Delete Tasks")
        task_list_frame = ttk.Frame(delete_window)     #to contain the list of tasks
        task_list_frame.pack(padx=10, pady=10)
        self.c.execute("SELECT id, task FROM tasks")      #retrieve tasks from database
        tasks = self.c.fetchall()

This displays the retrieved tasks with checkboxes:

        for task_id, task_text in tasks:
            task_checkbutton = ttk.Checkbutton(task_list_frame, text=task_text, command=lambda id=task_id: update_selected_tasks(id))
            task_checkbutton.pack(anchor="w", padx=5, pady=2)

![todo_del_window1][8]

This function removes the selected tasks from the table after verifying that at least one task has been chosen:

	    if not selected_task_ids:
             messagebox.showwarning("Warning", "No tasks selected for deletion.")
             return
        for task_id in selected_task_ids:
             self.c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
         self.conn.commit()
         self.load_tasks()
If no task is selected:

![todo_del_window2][9]

Marking tasks 1 and 3 for deletion:

![todo_del_window3][10]

After successful deletion:

![todo_del_window4][11]

**Function to Mark Tasks as Complete**
When a task is marked as complete, it needs to be updated in the table as well.

	     self.c.execute("SELECT priority, initial_priority FROM tasks WHERE id=?", (task_id,))
	     row = self.c.fetchone()
	     if row:
	         current_priority, initial_priority = row
	         if current_priority == 'Completed':
	             new_priority = initial_priority
	         else:
	             new_priority = 'Completed'
	         self.c.execute("UPDATE tasks SET priority=? WHERE id=?", (new_priority, task_id))
	         self.conn.commit()
It fetches the task's `priority` and `initial_priority` from the database. If the task is marked as completed, it resets the priority to its initial state; otherwise, it marks the task as completed and updates its priority in the database.

![todo_complete][12]


# Code Sample
	import tkinter as tk
	from tkinter import ttk, messagebox
	import sqlite3

	class TodoListApp:
	    def __init__(self, window):
	        self.window = window
	        self.window.title("Todo List App")
	        self.conn = sqlite3.connect("todo.db")
	        self.c = self.conn.cursor()
	        self.create_table()
	        self.selected_tasks = []
	        self.priority_selection = tk.StringVar()
	        self.create_widgets()
	    
	    def create_table(self):
	        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
	                            id INTEGER PRIMARY KEY AUTOINCREMENT,
	                            task TEXT NOT NULL,
	                            priority TEXT,
	                            initial_priority TEXT,
	                            deadline TEXT
	                        )''')
	        self.conn.commit()
	    
	    def create_widgets(self):
	        entry_frame = ttk.Frame(self.window)
	        entry_frame.pack(padx=10, pady=10, fill=tk.X)
	        ttk.Label(entry_frame, text="Task name:").grid(row=0, column=0, padx=5, pady=5)
	        self.task_text = tk.StringVar()
	        self.task_entry = ttk.Entry(entry_frame, textvariable=self.task_text)
	        self.task_entry.grid(row=0, column=1, padx=5, pady=5)
	        ttk.Label(entry_frame, text="Priority:").grid(row=1, column=0, padx=5, pady=5)
	        ttk.Radiobutton(entry_frame, text="Urgent", variable=self.priority_selection, value="Urgent").grid(row=1, column=1, padx=5, pady=5)
	        ttk.Radiobutton(entry_frame, text="General", variable=self.priority_selection, value="General").grid(row=1, column=2, padx=5, pady=5)
	        ttk.Label(entry_frame, text="Deadline:").grid(row=2, column=0, padx=5, pady=5)
	        self.task_deadline = tk.StringVar()
	        self.deadline_entry = ttk.Entry(entry_frame, textvariable=self.task_deadline)
	        self.deadline_entry.grid(row=2, column=1, padx=5, pady=5)
	        add_button = ttk.Button(entry_frame, text="Add Task", command=self.add_task)
	        add_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
	        self.task_list_frame = ttk.Frame(self.window)
	        self.task_list_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
	        self.load_tasks()
	        delete_button = ttk.Button(self.window, text="Delete Tasks", command=self.delete_tasks)
	        delete_button.pack(pady=5)
	        
	    def load_tasks(self):
	        for widget in self.task_list_frame.winfo_children():
	            widget.destroy()
	        self.c.execute("SELECT * FROM tasks")
	        tasks = self.c.fetchall()
	        for task in tasks:
	            task_id = task[0]
	            task_text = task[1]
	            task_priority = task[2]
	            task_deadline = task[4]
	            task_frame = ttk.Frame(self.task_list_frame)
	            task_frame.pack(fill=tk.X, padx=5, pady=2)
	            task_checkbutton = ttk.Checkbutton(task_frame, command=lambda id=task_id: self.select_task(id))
	            task_checkbutton.grid(row=0, column=0)
	            if task_priority == "Urgent" or (task_priority == "General" and task_deadline):
	                task_label = ttk.Label(task_frame, text=(task_text+"    ("+task_deadline+")"))
	            else:
	                task_label = ttk.Label(task_frame, text=task_text)
	            task_label.grid(row=0, column=1, padx=5)
	            
	            if task_priority == "Urgent":
	                task_label.config(foreground="red")
	            else:
	                task_label.config(foreground="blue")
	            if task_priority == "Completed":
	                task_label.config(foreground="green")
	                task_checkbutton.state(['selected'])
	    
	    def add_task(self):
	        task_text = self.task_text.get().strip()
	        task_priority = self.priority_selection.get()
	        task_deadline = self.task_deadline.get().strip()
	        if task_text and (task_priority == "General" or (task_priority == "Urgent" and task_deadline)):
	            self.c.execute("INSERT INTO tasks (task, priority, initial_priority, deadline) VALUES (?, ?, ?, ?)", (task_text, task_priority, task_priority, task_deadline))
	            self.conn.commit()
	            self.load_tasks()
	            self.task_text.set("")
	            self.priority_selection.set("")
	            self.task_deadline.set("")
	        else:
	            messagebox.showwarning("Warning", "Task or Priority cannot be empty, and Urgent task must have a deadline.")
	    
	    def select_task(self, task_id):
	        self.c.execute("SELECT priority, initial_priority FROM tasks WHERE id=?", (task_id,))
	        row = self.c.fetchone()
	        if row:
	            current_priority, initial_priority = row
	            if current_priority == 'Completed':
	                new_priority = initial_priority
	            else:
	                new_priority = 'Completed'
	            self.c.execute("UPDATE tasks SET priority=? WHERE id=?", (new_priority, task_id))
	            self.conn.commit()
	            self.load_tasks()

	    def delete_tasks(self):
	        delete_window = tk.Toplevel(self.window)
	        delete_window.geometry("457x335")
	        delete_window.title("Delete Tasks")
	        task_list_frame = ttk.Frame(delete_window)
	        task_list_frame.pack(padx=10, pady=10)
	        self.c.execute("SELECT id, task FROM tasks")
	        tasks = self.c.fetchall()
	        selected_task_ids = []

	        def update_selected_tasks(task_id):
	            if task_id in selected_task_ids:
	                selected_task_ids.remove(task_id)
	            else:
	                selected_task_ids.append(task_id)

	        def delete_selected_tasks():
	            if not selected_task_ids:
	                messagebox.showwarning("Warning", "No tasks selected for deletion.")
	                return
	            for task_id in selected_task_ids:
	                self.c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
	            self.conn.commit()
	            self.load_tasks()
	            delete_window.destroy()

	        for task_id, task_text in tasks:
	            task_checkbutton = ttk.Checkbutton(task_list_frame, text=task_text, command=lambda id=task_id: update_selected_tasks(id))
	            task_checkbutton.pack(anchor="w", padx=5, pady=2)

	        delete_button = ttk.Button(delete_window, text="Delete", command=delete_selected_tasks)
	        delete_button.pack(side="left", padx=5, pady=5)
	        cancel_button = ttk.Button(delete_window, text="Cancel", command=delete_window.destroy)
	        cancel_button.pack(side="right", padx=5, pady=5)

	window = tk.Tk()
	window.geometry("457x335")
	app = TodoListApp(window)
	window.mainloop()


# Conclusion
In summary, crafting a Todo List App with Tkinter provides a practical introduction to Python GUI development. You've built an intuitive interface for a **To-Do list app** with **addition**, **deletion**, and **task completion** features. Using **SQLite** for **data storage**, you've showcased Python's **versatility**. This project offers insights into **user experience design**, beneficial for aspiring developers.


[1]: https://docs.python.org/3/library/tk.html
[2]: https://www.python.org/downloads/
[3]: https://docs.python.org/3/library/tkinter.html
[4]: https://coderlegion.com/190/introduction-to-tkinter-library-in-python
[5]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/ToDo%20List/todo_gui.png
[6]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/ToDo%20List/todo_error_insert.png
[7]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/ToDo%20List/todo_insert.png
[8]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/ToDo%20List/todo_del_window1.png
[9]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/ToDo%20List/todo_del_window2.png
[10]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/ToDo%20List/todo_del_window3.png
[11]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/ToDo%20List/todo_del_window4.png
[12]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/ToDo%20List/todo_complete.png
