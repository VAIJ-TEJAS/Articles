
In this article, we'll dive into the world of **Tkinter**, a popular GUI (Graphical User Interface) toolkit for Python, and harness its capabilities to build a robust **to-do list application** from scratch. We'll walk you through each step, from designing a **user-friendly interface** to adding crucial functions like **task creation**, **deletion** and **prioritization**.

# Brief Overview of Tkinter
Tkinter is a popular Python library for creating graphical user interfaces. It provides a simple but powerful way to design and implement interactive applications with ease. With Tkinter, you can create windows, buttons, labels, text boxes, and other GUI elements to build intuitive and user-friendly interfaces for your Python programs.

Feel free to check out this article to discover more about [advanced Tkinter concepts][1].

# What is a To-Do List?

A to-do list is like your personal task manager. It's a simple way to jot down all the things you need to do, whether it's groceries to buy, assignments to finish, or calls to make. It helps to keep you organized and on track. Instead of trying to remember everything in your head, you can write it down on your list. It helps you prioritize, stay focused, and feel accomplished as you tick off tasks one by one.

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

Tkinter comes pre-installed with Python. Hence, you need not download it again.
	
<div class="div-blue"> <span class="alert-header">Note:</span> <span class="alert-body"> You can verify the installation by typing `python3 --version` in the terminal.</span> </div>

- Text Editor or IDE: Choose a text editor or IDE you're comfortable with, such as Visual Studio Code or PyCharm, for writing and running Python code.
- Basic Python Skills: Understand basic Python concepts like variables, data types, functions, and control flow.
- Tkinter Basics: Knowing the basics of Tkinter, such as widgets and event handling, can be helpful. You can learn through [Tkinter documentation][3] or [this article][4].

With these basics in place, you'll be ready to create your own to-do list app using Tkinter.


# Designing the User Interface
**Importing necessary Libraries**
Tkinter (`tk`) is the primary module for building GUI applications, while `ttk` provides themed widget components for a more modern and customized look. The `messagebox` module allows you to display various types of message boxes for user interaction. We shal be using SQLite3 for storing our tasks. It is a lightweight database engine used for storing and managing data locally.

	import tkinter as tk
	from tkinter import ttk, messagebox
	import sqlite3

**Creating the Main Window**
First, we create the main window for the Todo List App with Tkinter, setting its size and geometry. Then, we instantiate the TodoListApp class to integrate its functionalities (discussed later) into the window. Finally, we start the event loop to ensure the application responds to user interactions.

	window = tk.Tk()
	window.geometry("457x335")
	app = TodoListApp(window)
	window.mainloop()

**Adding a Title and necessary Frames and Labels**
You can add a catchy title to your To-Do app. Here, I have named it "Todo List App". The app features two frames: one for entering new tasks and another for displaying existing ones. The new task frame includes labels for "Task Name," "Priority," and "Deadline."

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
Following that, we require a text field where users can input a name for a new task. Additionally, users should be able to choose one of two priorities: "Urgent" or "General." In the case of an urgent task, users will also need a text field to input the deadline.

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
For each task, `task_id`, `task_text`, `task_priority`, and `task_deadline` is extracted. Then, it creates a frame to contain the task details, ensuring visual separation and organization. `task_checkbutton` is created for each task, allowing users to mark tasks as complete. Additionally, the task name is displayed as a Label within the frame. If the task is urgent or has a deadline, the task name is appended with the deadline information.

This represents the expected appearance of the GUI:

![todo_gui][5]

<div class="div-green"> <span class="alert-header">Tip:</span> <span class="alert-body"> Customize the labels to give different colours for tasks having different priorities. The code for the same is provided at the end.</span> </div>


# Implementing Functionality
<div class="div-blue"> <span class="alert-header">Note:</span> <span class="alert-body"> The following functions are defined in the `TodoListApp` class.</span> </div>

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
To input a new task, you need to provide task details including the task name, priority, and deadline. All tasks should have a name and its priority must be set. It's important to note that a deadline is required for urgent tasks.

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
It collects task details such as name, priority, and deadline from input fields. If the name is not empty and the priority is either "General" or "Urgent" with a specified deadline, the task is added to the database. After insertion, the task list updates, and input fields reset. If the description or priority is empty, or an urgent task lacks a deadline, a warning message appears.

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
        task_list_frame = ttk.Frame(delete_window)
        task_list_frame.pack(padx=10, pady=10)
        self.c.execute("SELECT id, task FROM tasks")
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
In summary, crafting a Todo List App with Tkinter provides a hands-on introduction to Python GUI development. You've successfully built an intuitive interface for a **To-Do list app**, highlighting Python's **versatility** for practical applications. Through this project, you gain insights into **user experience design**, making it an ideal starting point for aspiring developers.


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
