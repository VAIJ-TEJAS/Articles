# Introduction to Tkinter

Embarking on the journey of **Graphical User Interface (GUI)** development in **Python** opens up a realm of possibilities, with **Tkinter** emerging as a stalwart companion. Whether you're a novice programmer venturing into the world of GUIs or a seasoned developer seeking simplicity and efficiency, Tkinter is a reliable toolkit. In this article, we'll unravel the intricacies of Tkinter, explore its fundamental **widgets**, discuss its advantages and disadvantages, and equip you with the knowledge to excel in Python GUI development.


# Understanding Tkinter

Tkinter, short for **Tk interface**, is a built-in Python library designed for creating interactive GUI applications. Based on the Tk GUI toolkit, Tkinter simplifies the creation of windows, buttons, menus, and various graphical elements. As an integral part of the Python standard library, Tkinter seamlessly integrates with Python projects without the need of installing anything extra, offering a seamless and robust GUI development experience.


# Exploring Basic Widgets

Let's start by looking at some basic things you can create with Tkinter. The following snippets must be preceeded by:

    import tkinter as tk
    window = tk.Tk()
    window.geometry("457x335")

and followed by:

    window.mainloop()

## **Label**
Displays text or an image. It is a static element and doesn't allow user interaction.

        label = tk.Label(window, text="This is a Label")
        label.pack()

![label_output](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_label.png)

## **Button**
A clickable element that performs an action when pressed, such as submitting a form or triggering a function.

        def button_click():
            print("Button clicked")
        
        button = tk.Button(window, text="Click here!", command=button_click)
        button.pack()

![button](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_button.png)

After clicking the button:

![button_clicked](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_button_output.png)

## **Entry**
A text field where users can input text or numbers. It is often used for data entry or search functionality.

        entry = tk.Entry(window)
        entry.pack()

![entry](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_entry.png)

## **Text**
A text field that provides a multi-line text editing area for users to input or display text.

        text = tk.Text(window, height=5, width=30)
        text.pack()

![text](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_text.png)

## **Scale**
Allows users to select a value within a range by dragging a slider. It is useful for selecting values like volume, brightness, etc.

        def update_value(value):
            label.config(text=f"Volume Level: {value}")
        
        scale = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=update_value)     #create a scale to select values from 0 to 100
        scale.pack()
        label = tk.Label(window, text="Volume Level: ")
        label.pack()

![scale](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_scale.png)

## **Spinbox**
A numerical input field with up and down arrow buttons for incrementing or decrementing the value.

        spinbox = tk.Spinbox(window, from_=0, to=10)
        spinbox.pack()

![spinbox](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_spinbox.png)

## **Separator**
A horizontal or vertical line to visually separate sections or groups of widgets.

        from tkinter import ttk     #for themed widgets
        label1 = tk.Label(window, text="This is above the separator.")
        label1.pack()
        separator = ttk.Separator(window, orient=tk.HORIZONTAL)
        separator.pack(fill=tk.X)
        label2 = tk.Label(window, text="This is below the separator.")
        label2.pack()

![separator](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_separator.png)

## **Checkbutton**
A checkbox that allows users to select or deselect an option.

        check_var = tk.BooleanVar()     #To keep track of the checkbox's state (checked or unchecked)
        check_button = tk.Checkbutton(window, text="Checkbox", variable=check_var)
        check_button.pack()

![checkbox](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_checkbox.png)

## **Radiobutton**
A set of mutually exclusive buttons, allowing users to choose only one option from multiple choices.

        radio_var = tk.StringVar()     #To track which radio button is selected
        radio_button1 = tk.Radiobutton(window, text="Option 1", variable=radio_var, value="Option 1")
        radio_button2 = tk.Radiobutton(window, text="Option 2", variable=radio_var, value="Option 2")
        radio_button1.pack()
        radio_button2.pack()

![radiobutton](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_radiobutton.png)

## **Listbox**
A widget that displays a list of items from which users can select one or more options. It's often used for selecting items from a list or displaying results.
- **Scrollbar**: Allows users to scroll through content that exceeds the visible area of a widget, such as a text box or list.

        listbox = tk.Listbox(window)
        scrollbar = tk.Scrollbar(window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)     #scrollbar will be at the right side of the window and expands vertically 
        listbox.pack(side=tk.LEFT, fill=tk.BOTH)     #listbox will be at the left side of the window and expands horizontally and vertically 
        listbox.config(yscrollcommand=scrollbar.set)     #Attach scrollbar to listbox
        scrollbar.config(command=listbox.yview)
        for i in range(30):
            listbox.insert(tk.END, f"Item {i+1}")

![scroll_list1](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_scroll_list1.png)

![scroll_list2](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_scroll_list2.png)

## **ColorChooser**
A dialog for users to select a color. It provides a graphical interface for choosing colors using a palette or entering RGB values.

        from tkinter import colorchooser
        
        def choose_color():
            color = colorchooser.askcolor()
            print("Selected color:", color)
        
        button = tk.Button(window, text="Choose Color", command=choose_color)
        button.pack()

![color](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_color.png)

## **Frame**
A container used to group and organize other widgets. It is often used for layout purposes to create sections or divisions within a window.

        frame = tk.Frame(window, bg="lightblue", bd=5)
        frame.pack()
        label = tk.Label(frame, text="Inside the Frame", bg="lightblue")
        label.pack()

![frame](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_frame.png)

## **Canvas**
Provides a drawing area for creating graphics, shapes, and custom elements. It is used for creating diagrams, charts, and interactive visualizations.

        canvas = tk.Canvas(window, width=200, height=100, bg="white")
        canvas.pack()
        canvas.create_rectangle(50, 25, 150, 75, fill="red")     #draw a red-coloured rectangle

![canvas](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_canvas.png)

## **PanedWindow**
A container for arranging multiple panes or frames with adjustable sizes. It allows users to resize panes by dragging the divider between them.

        paned_window = tk.PanedWindow(window, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True)     #will expand both horizontally and vertically
        frame1 = tk.Frame(paned_window, width=228, height=200, background="red")
        frame2 = tk.Frame(paned_window, width=228, height=200, background="blue")
        paned_window.add(frame1)
        paned_window.add(frame2)

![panedwindow1](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_paned1.png)

After dragging the divider to the left:

![panedwindow2](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_paned2.png)

## **Menu**
Creates a menu bar or dropdown menu with options and commands. It is often used for adding navigation, settings, and other functionality to the application's interface.

        def print_something():
            print("You chose the first option")
        
        menu_bar = tk.Menu(window)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Print Something", command=print_something)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=window.quit)
        menu_bar.add_cascade(label="Click to see options", menu=file_menu)
        window.config(menu=menu_bar)

![menu](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_menu.png)

After selecting "Print Something":

![menu_output](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_menu_output.png)

These widgets form the core building blocks of Tkinter GUI applications and are commonly used in various projects to create user-friendly interfaces.


# Basic Functionalities

Let's dive into some code examples to see these concepts in action.

**1. Creating a Window**

    import tkinter as tk
    window = tk.Tk()
    window.title("Welcome to Tkinter")
    window.geometry("457x335")
    label = tk.Label(window, text="Hello World!")
    label.pack()
    window.mainloop()

![sample_window_output](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_1.png)

**Explanantion**

The first line `import tkinter as tk` imports the Tkinter module, which provides tools for creating GUI applications in Python. 
The second line `window = tk.Tk()` creates a new Tkinter window object named `window`. This window will serve as the main container for the GUI elements of our application.
The third line `window.title("Welcome to Tkinter")` sets the title of the window to "Welcome to Tkinter". This title will be displayed in the window's title bar.
The fourth line `window.geometry("900x700")` sets the size of the window to 900 pixels wide and 700 pixels tall. The format for specifying window size is `width x height`.
The fifth line `label = tk.Label(window, text="Hello World!")` creates a Label widget named `label` within the window. The label displays the text "Hello World!".
The sixth line `label.pack()` organizes the label within the window using the `pack()` method. Packing a widget places it in the window according to the layout manager's rules. In this case, it will be placed at the top-left corner of the window.
The last line `window.mainloop()` starts the Tkinter event loop. This method waits for events such as user input or interaction with GUI elements and responds to them accordingly. It keeps the GUI application running and responsive.

**2. Creating and Handling Button Clicks**

    import tkinter as tk

    def hello():
        name = entry.get()
        hello_label.config(text=f"Hello, {name}!")
    
    window = tk.Tk()
    window.title("Hello!")
    window.geometry("457x335")
    instruction_label = tk.Label(window, text="Enter your name:")
    instruction_label.pack()
    entry = tk.Entry(window)
    entry.pack(pady=10)
    button = tk.Button(window, text="Accept", command=hello)
    button.pack(pady=15)
    hello_label = tk.Label(window, text="")
    hello_label.pack()
    window.mainloop()

![sample_button_output1](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_2.png)

![sample_button_output2](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_3.png)

**Explanantion**

The function `hello()` is defined to be called when the button is clicked. It retrieves the text entered in the entry widget, constructs a greeting message using that text, and updates the text of the `hello_label` widget to display the greeting.
The following three lines perform the same actions as mentioned previously.
The line`instruction_label = tk.Label(window, text="Enter your name:")` creates a Label widget named instruction_label within the window. The label displays the text "Enter your name:".
The line `instruction_label.pack()` organizes the label within the window using the `pack()` method. It will be placed in the window.
The line `entry = tk.Entry(window)` creates a Text Entry widget named `entry` within the window, which allows users to input text.
`entry.pack(pady=10)` organizes the text entry widget within the window using the pack() method and adds vertical padding of 10 pixels above and below the widget.
`button = tk.Button(window, text="Accept", command=hello)` creates a Button widget named `button` within the window. The button displays the text "Accept" and is associated with the `hello()` function. When the button is clicked, the `hello()` function will be executed.
`hello_label = tk.Label(window, text="")` creates a Label widget named `hello_label` within the window, which will display the greeting message.


# Advanced Features

1. Tkinter can be integrated with other Python libraries and tools to enhance its functionality:
 - **Integration with Matplotlib**: You can make your Tkinter app more informative by adding interactive charts to display data trends or visualizations. By integrating Matplotlib, a popular Python library for creating charts and graphs, you can easily embed dynamic plots directly into your Tkinter windows.
 - **Integration with Requests**: If your Tkinter app needs to fetch data from the internet, you can use the Requests library to display weather information or stock prices. By integrating Requests, you can make HTTP requests to web APIs and fetch the required data.
 - **Integration with SQLite**: If your Tkinter app needs to store and manage data locally, you can use SQLite, a lightweight relational database. It can be used to store user preferences or application settings. By integrating SQLite, you can create a database within your app to store and retrieve data as needed.

2. Tkinter also provides advanced widgets beyond the basic ones, for example:
 - A **treeview** to display hierarchical data, like a file explorer.
        
        import tkinter as tk
        from tkinter import ttk     #for themed widgets
        window = tk.Tk()
        window.geometry("640x300")
        tree = ttk.Treeview(window)
        tree["columns"] = ("Fruits", "Quantity")
        tree.heading("#0", text="Sr. No.")     #First column (index=0) will be Sr. No.
        tree.heading("Fruits", text="Fruits")
        tree.heading("Quantity", text="Quantity (kg)")
        tree.insert("", tk.END, text="1", values=("Apple", 30))
        tree.insert("", tk.END, text="2", values=("Orange", 25))
        tree.insert("", tk.END, text="3", values=("Mango", 29))
        tree.pack()
        window.mainloop()
    
    ![trreview](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_treeview.png)
   
 - A **notebook** to organize your app into different tabs, like in a web browser.
        
        import tkinter as tk
        from tkinter import ttk     #for themed widgets
        window = tk.Tk()
        window.geometry("457x335")
        notebook = ttk.Notebook(window)
        tab1 = ttk.Frame(notebook)
        tab2 = ttk.Frame(notebook)
        tab3 = ttk.Frame(notebook)
        label1 = tk.Label(tab1, text="This is Tab 1")     #for tab 1
        label1.pack()
        entry2 = tk.Entry(tab2)     #for tab 2
        entry2.pack()
        check_var = tk.BooleanVar()
        check_button3 = tk.Checkbutton(tab3, text="This is Tab 3", variable=check_var)     #for tab 3
        check_button3.pack()
        notebook.add(tab1, text="Tab 1")
        notebook.add(tab2, text="Tab 2")
        notebook.add(tab3, text="Tab 3")
        notebook.pack()
        window.mainloop()
    
    ![Tab1](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_notebook1.png)
   
    ![Tab2](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_notebook2.png)
   
    ![Tab3](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_notebook3.png)
   
 - A **progressbar** to show how far along a task is, like when you're downloading a file.
    
        import tkinter as tk
        from tkinter import ttk
        import time
        
        def start_task():
            progress_bar.start(10)     #start the progressbar (animation is updated every 10 milliseconds)
            window.after(3000, stop_task)     #simulate task completion after 3 seconds
        
        def stop_task():
            progress_bar.stop()      #stop the progressbar
        
        window = tk.Tk()
        window.geometry("457x335")
        progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="indeterminate")
        progress_bar.pack()
        start_button = tk.Button(window, text="Start Task", command=start_task)
        start_button.pack(pady=20)
        window.mainloop()

    ![progressbar](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_progressbar.png)
   
 Whether you're building a game, a productivity tool, or a social networking app, there's a widget for every occasion.

3. Tkinter allows implementation of file handling features in your Tkinter application:
 - Tkinter comes with a handy tool called `filedialog`, which pops up a window where users can pick a file from their computer.
 - Your app can help users create, open, save, and even edit files like documents, images, or spreadsheets.

4. Advanced Layout Management can be used to make your Tkinter app look polished. Layout management helps you move widgets around and make your app look just the way you want using  `grid`, `place`, and `pack` managers.
 - **Grid**: You can place widgets in rows and columns, and they will organize neatly into place.
    
        import tkinter as tk
        window = tk.Tk()
        window.geometry("457x335")
        label1 = tk.Label(window, text="Subject")
        label2 = tk.Label(window, text="Marks")
        entry1 = tk.Entry(window)     #Widgets
        entry2 = tk.Entry(window)
        entry3 = tk.Entry(window)
        entry4 = tk.Entry(window)
        label1.grid(row=0, column=0)     #Layout
        label2.grid(row=0, column=1)
        entry1.grid(row=1, column=0)
        entry2.grid(row=1, column=1)
        entry3.grid(row=2, column=0)
        entry4.grid(row=2, column=1)
        window.mainloop()

    ![grid](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_grid.png)

## **Pack**
You can stack widgets on top of each other or arrange them side by side, and Tkinter will figure out how to fit them all in.
    
        import tkinter as tk
        window = tk.Tk()
        window.geometry("457x335")
        button1 = tk.Button(window, text="Left")     #Widgets
        button2 = tk.Button(window, text="Top")
        button3 = tk.Button(window, text="Right")
        button4 = tk.Button(window, text="Bottom")
        button1.pack(side=tk.LEFT)     #Layout
        button2.pack(side=tk.TOP)
        button3.pack(side=tk.RIGHT)
        button4.pack(side=tk.BOTTOM)
        window.mainloop()

    ![pack](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_pack.png)
   
## **Place**
You can specify exactly where you want each widget to go by giving it coordinates, like x and y coordinates on a graph.
    
        import tkinter as tk
        window = tk.Tk()
        window.geometry("457x335")
        label1 = tk.Label(window, text="x_50_y_50")     #Widgets
        label2 = tk.Label(window, text="x_200_y_200")
        label1.place(x=50, y=50)     #Layout
        label2.place(x=200, y=200)
        window.mainloop()
    
    ![place](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_place.png)


# Advantages

- Tkinter's user-friendly syntax and straightforward API make it approachable for beginners, allowing swift prototyping and development.
- Tkinter applications operate seamlessly across various operating systems.
- As an important component of the Python standard library, Tkinter seamlessly intertwines with Python code, streamlining development processes and upkeep.
- Tkinter offers an extensive collection of widgets, empowering developers to craft diverse and visually appealing interfaces as per their needs.


# Disadvantages

- Tkinter's built-in widgets offer limited customization options compared to modern GUI frameworks.
- In complex applications with extensive computations or intensive graphics, Tkinter's performance may lag behind more specialized GUI frameworks.


# Good Programming Practices for Tkinter

When working with Tkinter, adhering to good programming practices ensures that your code is organized, maintainable, and efficient. Some recommended practices are as follows:
- Modularize Your Code: Break your GUI application into smaller, reusable components. Breaking it into smaller, reusable parts makes it easier to work with.
- Use Descriptive Variable Names: Choose meaningful names for variables, functions, and widgets to enhance code readability. This helps you and others to understand the purpose of each component.
- Organize Your Layout: Using Tkinter's layout managers such as `pack()`, `grid()`, or `place()`, effectively organizes your widgets within the window and ensures a consistent and visually appealing layout.
- Handle Events Properly: Implement event handling using Tkinter's event-driven model and use event bindings or command callbacks to respond to user interactions.
- Error Handling: Implement error handling to gracefully handle unexpected errors and exceptions. Use `try` and `except` blocks to catch and handle exceptions, and provide informative error messages to the user when applicable.


# Conclusion

Tkinter is a versatile and user-friendly toolkit for Python GUI development, offering a rich set of widgets, cross-platform compatibility, and seamless integration with Python code. Despite its limitations, Tkinter remains a popular choice for developers looking for efficient creation of simple to moderately complex GUI applications.

Also see:
[Tkinter Documentation](https://docs.python.org/3/library/tk.html)
