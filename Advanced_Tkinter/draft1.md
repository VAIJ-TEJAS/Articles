In this article, we'll delve into some of the more intricate aspects of **Tkinter**, exploring advanced techniques that will empower you to create even more powerful and polished GUI applications. Throughout our exploration, we'll uncover invaluable tools such as the **`ttk` module** for enhanced widget styling, the **Canvas** widget for versatile graphics rendering, and the **Grid** geometry manager for precise layout control.  From **custom themes** to **file handling strategies**, gear up to elevate your Tkinter expertise to the next level.


<div class="div-green"> <span class="alert-header">Tip:</span> <span class="alert-body"> If you are unfamiliar with or new to Tkinter, it is highly recommended to thoroughly review  <a href=[1]> this article</a> or the <a href=[18]>official documentation</a>. Familiarizing yourself with its contents will provide a solid foundation for understanding and effectively utilizing Tkinter in GUI development.</span> </div>


# Custom Styles and Themes
Tkinter offers the flexibility to tailor the visual presentation of your application through the use of custom styles and themes. Utilizing the `ttk module` enables the creation of widgets with personalized designs, ensuring a unified user experience across various platforms.

To deepen our understanding, let's personalize our textbox, button, and label by customizing their appearance:

	import tkinter as tk
	from tkinter import ttk

	def submit_text():
	    text = text_entry.get()
	    text_label.config(text=text, font=("Times New Roman", 12, "bold"), foreground="green")     #customize label

	window = tk.Tk()
	window.geometry("457x335")
	window.title("Custom Styles")

	style = ttk.Style()     #to define custom styles
	style.configure("Custom.TEntry", foreground="blue", fieldbackground="lightblue")     #customize textbox
	style.configure("Custom.TButton", foreground="red", background="red")     #customize button

	text_entry = ttk.Entry(window, width=30, style="Custom.TEntry")
	text_entry.pack(padx=10, pady=10)
	submit_button = ttk.Button(window, text="Submit", command=submit_text, style="Custom.TButton")     #sends entered text to the submit_text() function
	submit_button.pack(padx=10, pady=5)
	text_label = ttk.Label(window)
	text_label.pack(padx=10, pady=10)
	window.mainloop()

![custom_styles][2]


# Integration with Python Libraries

 Tkinter can be integrated with other Python libraries and tools to enhance its functionality:
 - **Integration with Matplotlib**: You can make your Tkinter app more informative by adding interactive charts to display data trends or visualizations. By integrating Matplotlib, a popular Python library for creating charts and graphs, you can easily embed dynamic plots directly into your Tkinter windows.
 
<div class="div-blue"> <span class="alert-header">Note:</span><span class="alert-body"> In order to install matplotlib library locally, run the command: `pip install matplotlib`</span> </div>

 - **Integration with Scikit-learn**: You can combine Tkinter with Scikit-learn to develop GUI applications for machine learning tasks such as classification, regression, and clustering. This integration enables us to build interactive interfaces for training models, evaluating performance, and making predictions.

<div class="div-blue"> <span class="alert-header">Note:</span><span class="alert-body"> In order to install sklearn library locally, run the command: `pip install scikit-learn`</span> </div>
 
<div class="div-red"> <span class="alert-header">Caution:</span> <span class="alert-body">Make sure you have `matplotlib` and `matplotlib.backends.backend_tkagg` installed to run this code locally.</span> </div>

Let's delve into the concept using an example of Linear Regression applied to predict outcomes for the Diabetes dataset:

	import tkinter as tk
	from tkinter import ttk     #for themed widgets
	import matplotlib.pyplot as plt
	from sklearn.datasets import load_diabetes
	from sklearn.model_selection import train_test_split
	from sklearn.linear_model import LinearRegression
	from sklearn.metrics import mean_squared_error

	diabetes = load_diabetes()     #Load the dataset
	X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.2, random_state=42)

	window = tk.Tk()
	window.geometry("650x500")
	window.title("Diabetes Linear Regression")

	def train_and_plot():
	    model = LinearRegression()
	    model.fit(X_train, y_train)     #train
	    y_pred_train = model.predict(X_train)     #predict
	    y_pred_test = model.predict(X_test)
	    mse_train = mean_squared_error(y_train, y_pred_train)     #calculate mean squared error
	    mse_test = mean_squared_error(y_test, y_pred_test)
	    
	    plt.figure(figsize=(8, 6))     #create the plot
	    plt.scatter(y_test, y_pred_test, color='blue')
	    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
	    plt.xlabel("Actual")
	    plt.ylabel("Predicted")
	    plt.title("Linear Regression Graph")
	    plt.grid(True)
	    plt.tight_layout()     #ensures the plot fits within the Tkinter window
	    result_label.config(text=f"Train MSE: {mse_train:.2f}\tTest MSE: {mse_test:.2f}")
	    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)     #converts the plot into a format that can be displayed in the Tkinter window
	    canvas.draw()
	    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)     #adds the canvas widget to the Tkinter window.

	train_button = ttk.Button(window, text="Train and Plot", command=train_and_plot)
	train_button.pack(pady=10)
	result_label = ttk.Label(window, text="")
	result_label.pack()
	window.mainloop()

![integrations][3]


# Advanced Widgets
Tkinter provides a wide range of widgets beyond the basic ones like labels and buttons. You can explore and utilize widgets like treeview, notebook, progressbar, etc. to create sophisticated user interfaces.
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
    
    ![treeview][4]
   
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
    
    ![Tab1][5]
   
    ![Tab2][6]
   
    ![Tab3][7]
   
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

    ![progressbar][8]
   
 Whether you're building a game, a productivity tool, or a social networking app, there's a widget for every occasion.


# Advanced Layout Management
Advanced Layout Management can be used to make your Tkinter app look polished. Layout management helps you move widgets around and make your app look just the way you want using  `grid`, `place`, and `pack` managers.
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

    ![grid][9]

- **Pack**
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

    ![pack][10]
   
 - **Place**
You can specify exactly where you want each widget to go by giving it coordinates, like x and y coordinates on a graph.
    
        import tkinter as tk
        window = tk.Tk()
        window.geometry("457x335")
        label1 = tk.Label(window, text="x_50_y_50")     #Widgets
        label2 = tk.Label(window, text="x_200_y_200")
        label1.place(x=50, y=50)     #Layout
        label2.place(x=200, y=200)
        window.mainloop()
    
    ![place][11]
    

# File Handling

 Tkinter allows implementation of file handling features in your Tkinter application. Tkinter comes with a handy tool called `filedialog`, which pops up a window where users can pick a file from their computer. Your app can help users create, open, save, and even edit files like documents, images, or spreadsheets.
  
Let's understand this using an example:

	import tkinter as tk
	from tkinter import filedialog

	def open_file():
	    file_path = filedialog.askopenfilename()     #opens a dialog window to select an existing file or create a new one
	    if not file_path:
	        return
	    with open(file_path, 'a+') as file:     #'a+' to append the text to the file
	        file.write("January\n")
	        file.write("February\n")
	        file.write("March\n")
	        file.write("April\n")
	        file.write("May\n")
	    status_label.config(text=f"File '{file_path}' has been written and closed.")

	window = tk.Tk()
	window.geometry("457x335")
	window.title("File Writer")
	open_button = tk.Button(window, text="Open a File", command=open_file)
	open_button.pack(pady=20)
	status_label = tk.Label(window, text="")
	status_label.pack()
	root.mainloop()

![file][12]

![file_dialogbox][13]

![file_written_text][14]

<div class="div-blue"> <span class="alert-header">Note:</span>  <span class="alert-body"> The file will automatically be closed when the `with` block is exited. However, you may explicitly close the file by calling `file.close()`.</span> </div>


# Modal and Modeless Dialogs
Tkinter supports both modal and modeless dialogs, allowing you to create pop-up windows for user input, confirmation messages, or notifications. You can use the tkinter.messagebox module to create standard message boxes or create custom dialog windows using Toplevel widgets.
- **Modal dialogs** are windows that require the user to interact with them before returning to the main application window. They typically block interaction with other windows in the application until they are closed and include alert messages, confirmation dialogs, etc.

		import tkinter as tk
		from tkinter import messagebox

		def show_modal_dialog():
		    messagebox.showinfo("Modal Dialog", "Pay attention to this dialog box!")     #does not let you proceed until you click the "OK" button

		window = tk.Tk()
		window.geometry("457x335")
		window.title("Modal Dialog Example")
		modal_button = tk.Button(window, text="Click me", command=show_modal_dialog)
		modal_button.pack(padx=20, pady=10)
		window.mainloop()
		
	![modal_dialog][15]

- **Modeless dialogs** are windows that allow the user to interact with both the dialog and the main application window simultaneously. They do not block interaction with other windows in the application, allowing the user to switch between them freely and include property editors, tool palettes, etc.

		import tkinter as tk

		def show_modeless_dialog():
		    modeless_dialog = tk.Toplevel(window)     #allows you to interact with other open windows
		    modeless_dialog.title("Modeless Dialog")
		    modeless_dialog.geometry("250x100")
		    label = tk.Label(modeless_dialog, text="Have a nice day!")
		    label.pack(padx=20, pady=10)

		window = tk.Tk()
		window.geometry("457x335")
		window.title("Modeless Dialog Example")
		modeless_button = tk.Button(window, text="Click me", command=show_modeless_dialog)
		modeless_button.pack(padx=20, pady=10)
		window.mainloop()

	![modeless_dialog][16]


<div class="div-green"> <span class="alert-header">Tip:</span> <span class="alert-body"> Using a class for modeless dialogs can organize and encapsulate dialog functionality, particularly for more intricate dialogs with multiple components and interactions.</span> </div>


# Threading in Tkinter
Python's threading module enables the creation of supplementary threads, other than the existing GUI thread. Additional threads enable us to execute concurrent tasks alongside the GUI thread, ensuring smooth interaction and responsiveness.

Whenever the "Open a Modeless Dialog" button is clicked in the provided example, a fresh thread is generated:

	import tkinter as tk
	from tkinter import ttk
	import threading

	def submit_text():
	    start_thread(submit_text_thread)

	def open_modeless_dialog():
	    start_thread(open_modeless_dialog_thread)

	def start_thread(func):
	    thread = threading.Thread(target=func)
	    thread.start()

	def submit_text_thread():
	    text = text_entry.get()
	    text_label.config(text=text)

	def open_modeless_dialog_thread():
	    modeless_dialog = tk.Toplevel(window)
	    modeless_dialog.title("Modeless Dialog")
	    modeless_dialog.geometry("200x100")
	    label = tk.Label(modeless_dialog, text="This created a new thread!")
	    label.pack(padx=20, pady=10)

	window = tk.Tk()
	window.geometry("457x335")
	window.title("Thread Example")
	input_frame = ttk.Frame(window)     #frame for input
	input_frame.pack(padx=20, pady=10)
	text_entry = ttk.Entry(input_frame, width=30)
	text_entry.pack(side=tk.LEFT)
	submit_button = ttk.Button(input_frame, text="Submit", command=submit_text)
	submit_button.pack(side=tk.LEFT, padx=5)
	text_label = ttk.Label(window, text="")     #creates a label
	text_label.pack(padx=20, pady=10)
	modeless_button = ttk.Button(window, text="Open a Modeless Dialog", command=open_modeless_dialog)     #creates a button to open a modeless dialog box
	modeless_button.pack(padx=20, pady=5)
	window.mainloop()

![threads][17]

<div class="div-red"> <span class="alert-header">Caution:</span> <span class="alert-body"> Tkinter lacks thread safety and trying to alter GUI components from alternate threads can result in unexpected outcomes and application crashes. To update the GUI from these threads, alternative mechanisms such as event queues or the `after()` method are commonly utilized.</span> </div>


# Conclusion
Tkinter serves as a versatile framework for Python GUI development, offering a range of functionalities to enhance user interaction and application functionality. Through custom themes, threading capabilities, file handling, modal and modeless dialogs, layout management, advanced widgets, and integration with libraries like Matplotlib and scikit-learn, Tkinter enables developers to craft dynamic and user-friendly desktop applications tailored to their specific needs. By leveraging these features, developers can create unique and engaging GUIs that elevate the overall user experience, making Tkinter a preferred choice for Python GUI development projects.


[1]: https://coderlegion.com/190/introduction-to-tkinter-library-in-python
[2]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_custom.png
[3]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_interface.png
[4]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_treeview.png
[5]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_notebook1.png
[6]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_notebook2.png
[7]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_notebook3.png
[8]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_progressbar.png
[9]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_grid.png
[10]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_pack.png
[11]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_place.png
[12]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_file.png
[13]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_file_open1.png
[14]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_file_open2.png
[15]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_modal_dialog.png
[16]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_modeless_dialog.png
[17]: https://github.com/VAIJ-TEJAS/LogicLair_Articles/blob/main/Advanced_Tkinter/Tkinter_threads.png
[18]: https://docs.python.org/3/library/tkinter.html
