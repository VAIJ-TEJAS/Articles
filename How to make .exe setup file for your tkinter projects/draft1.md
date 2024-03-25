In this article, you will learn how to distribute a **Tkinter** project an as **.exe** setup file using **PyInstaller**. This converts Python scripts into **standalone executables** and makes it easy for people to install and use your applications. Users don't need to worry about installing Python or managing dependencies. This way, your programs can be easily moved between different computers and run securely. Plus, it gives your projects a more polished and professional look.

#  Environment Setup

- Python: Ensure that Python is installed on your system, which includes Tkinter by default. 
	- **For Windows**: Download and install Python from the [official website][1].
	- **For Ubuntu**: You can download Python using the terminal:

			sudo apt update
			sudo apt install python3
	- **For MacOS**: You can download Python using Homebrew:

			brew install python3
Confirm the installation by typing `python3 --version` in the terminal.
- PyInstaller: It is necessary for converting Python scripts into executable files. Open your terminal or command prompt and run the following:

		pip install pyinstaller
- IDE or Text Editor: Choose a preferred text editor or IDE like Visual Studio Code for coding.
- Tkinter: Basic understanding of Tkinter, including widgets and event handling, is beneficial. Refer to the [Tkinter documentation][2] or [this article][3] for learning.

<div class="div-blue"> <span class="alert-header">Note:</span> <span class="alert-body"> This project expects familiarity with basic Python concepts.</span> </div>

# Developing a Tkinter Project
Do check out [the documentation][4] to learn more about GUI using Tkinter.

We will create a simple calculator application using Tkinter in Python. It allows you to input two numbers and select an operation (addition, subtraction, multiplication, or division) using radio buttons. Upon clicking the "Calculate" button, the program performs the selected operation on the input numbers and displays the result in a modeless dialog box.

	import tkinter as tk
	from tkinter import messagebox
	
	def  calculate():
		num1 = float(entry1.get())
		num2 = float(entry2.get())
		if operation.get() == 1:     # Add
			result = num1 + num2
		elif operation.get() == 2:     # Subtract
			result = num1 - num2
		elif operation.get() == 3:     # Multiply
			result = num1 * num2
		elif operation.get() == 4:     # Divide
			if num2 == 0:
				messagebox.showerror("Error", "Cannot divide by zero")
					return
				result = num1 / num2
		result_window = tk.Toplevel(window)     # Modeless dialog box
		result_window.geometry("200x100")
		result_window.title("Result")
		result_label = tk.Label(result_window, text=f"The result is: {result}")     # Label widget
		result_label.pack()

	window = tk.Tk()     # Main window
	window.geometry("457x335")
	window.title("Calculator")
	
	frame_numbers = tk.Frame(window)     # Frame
	frame_numbers.pack()
	label1 = tk.Label(frame_numbers, text="Number 1:")     # Labels and Entry widgets
	label1.grid(row=0, column=0)
	entry1 = tk.Entry(frame_numbers)
	entry1.grid(row=0, column=1)
	label2 = tk.Label(frame_numbers, text="Number 2:")
	label2.grid(row=1, column=0)
	entry2 = tk.Entry(frame_numbers)
	entry2.grid(row=1, column=1)
	frame_operations = tk.Frame(window)     # Frame
	frame_operations.pack()
	operation = tk.IntVar()     # Radiobuttons
	addition = tk.Radiobutton(frame_operations, text="Addition", variable=operation, value=1)
	addition.grid(row=0, column=0, sticky="w")
	subtraction = tk.Radiobutton(frame_operations, text="Subtraction", variable=operation, value=2)
	subtraction.grid(row=1, column=0, sticky="w")
	multiplication = tk.Radiobutton(frame_operations, text="Multiplication", variable=operation, value=3)
	multiplication.grid(row=2, column=0, sticky="w")
	division = tk.Radiobutton(frame_operations, text="Division", variable=operation, value=4)
	division.grid(row=3, column=0, sticky="w")
	error_label = tk.Label(window, fg="red")     # Error label
	error_label.pack()
	calculate_button = tk.Button(window, text="Calculate", command=calculate)     # Button
	calculate_button.pack()
	window.mainloop()
- Firstly, import the Tkinter module and create a main window using `tk.Tk()`. 
- Two frames, `frame_numbers` and `frame_operations`, are created to organize the layout of the widgets.
- Labels and Entry widgets are placed inside `frame_numbers` to allow users to input two numbers.
- Radiobuttons, `addition`, `subtraction`, `multiplication`, and `division`, are placed inside `frame_operations` to select the desired operation.
- A `messagebox` is created to display error messages, such as division by zero.
- The `calculate()` function is defined to perform the calculation based on user input. It retrieves the input numbers and selected operation, calculates the result, and creates a modeless dialog box `result_window` using `tk.Toplevel()` to display the result.
- Finally, the main event loop `window.mainloop()` is started to run the application.

![pyinstl_calculator][5]

<div class="div-green"> <span class="alert-header">Tip:</span> <span class="alert-body"> It is best to encapsulate functions and shared variables within a class.</span> </div>

# Installing PyInstaller
To install PyInstaller using pip, follow these steps:

- Open your terminal or command prompt on your computer.
- Type the following command and press Enter:
   
		pip install pyinstaller
- Once the installation is complete, you can verify that PyInstaller has been installed correctly by running:

		pyinstaller --version

   This command will display the version of PyInstaller installed on your system.

Here's how PyInstaller converts python scripts to executable files:
- PyInstaller analyzes Python scripts and their dependencies.
- It bundles all dependencies, including the Python interpreter, into a single package.
- It creates standalone executables that can run independently on compatible systems.
- The tool optimizes and compresses the executable for efficient distribution.

<div class="div-blue"> <span class="alert-header">Note:</span> <span class="alert-body"> PyInstaller is cross-platform, supporting Windows, macOS, and Linux.</span> </div>

# Converting Tkinter Project to .exe File
Let's convert our calculator script to a .exe file.

- Open a command prompt or terminal window.
- Navigate to the directory containing your Python script.
- Run the following command:

		pyinstaller --onefile --windowed calculator.py
	`--onefile` bundles everything into a single executable and `--windowed` creates a GUI application without a console window.
- PyInstaller will analyze your script and create a `dist` directory in the same location, containing the converted .exe file (calculator.exe).
- Once the process is complete, you can find the `calculator.exe` file in the `dist` directory.

<div class="div-red"> <span class="alert-header">Caution:</span> <span class="alert-body"> Ensure that the Tkinter module has been installed.</span> </div>

Possible Errors that you may encounter:
- **ModuleNotFoundError**: To resolve PyInstaller's inability to locate some imported modules or dependencies, ensure all required modules are installed and accessible. You can install missing modules using pip.
- **Large Executable Size**: Optimize PyInstaller options to reduce .exe size. Use `--onefile` for a single executable or `--exclude-module` to exclude modules.
- **PermissionError**: Ensure you have write permissions for the output directory to avoid permission errors during PyInstaller execution.
- **Anti-virus False Positives**: Anti-virus programs may flag the .exe file as suspicious due to file bundling. To fix, whitelist the .exe or sign it with a digital signature.

# Customizing the .exe Setup File

To customize the .exe file generated by PyInstaller, you can add a custom icon, metadata using specific options, window size and title of the .exe file.

- **Custom Icon**: Utilize the `--icon` option followed by the path to your icon file (.ico). This sets the icon for the executable.

		pyinstaller --onefile --icon=calculator_icon.ico calculator.py
- **Metadata**: Craft a version file (.rc or .ini) containing metadata like file description, product name, and version information. Then, use the `--version-file` option to specify the path to this file.

		pyinstaller --onefile --version-file=calculator_version.rc calculator.py

   Example of calculator_version.rc:

		1 VERSIONINFO
		FILEVERSION 1,0,0,0
		PRODUCTVERSION 1,0,0,0
		FILEDESCRIPTION "Calculator Application"
		PRODUCTNAME "Calculator"
		ICON "calculator_icon.ico"
- **Window Size**: Use `--windowed` to create a GUI application without a console window. `--noconsole` can also be utilized, but it simply hides the console window and there might be a brief appearance of it. You can also set the window size in your Tkinter code.
    
- **Title of the .exe file**: Specify the executable name with `--name`.

		pyinstaller --onefile --name=SimpleCalculator calculator.py

# Testing the .exe Setup File
We'll now test our executable file. I've converted the Python script to a .exe file using the following command:

	pyinstaller --onefile --windowed --name=SimpleCalculator --icon=calculator_icon.ico calculator.py
The `SimpleCalculator.exe` file can be found in the `dist` folder.

![pyinstl_exec1][6]
Upon running the file, it works as intended.

![pyinstl_exec2][7]

![pyinstl_exec3][8]

To ensure compatibility, the file can be run on other systems as well.

The following flowchart provides a comprehensive overview of the entire process from start to finish:

![pyinstl_flowchart][9]

# Distributing Your Tkinter Application
To include multiple files while creating an executable using PyInstaller, you can use the `--add-data` option.

	pyinstaller --onefile --add-data "file1.extension;." --add-data "file2.extension;." calculator.py
The `--add-data` option allows you to specify the path to the extra file or folder you wish to include. Use a semicolon `;` to distinguish the source path from the destination directory inside the executable. A dot `.` indicates that the file should be copied to the same directory as the executable.
It can be used to include .csv files or SQLite databases. For example:

	pyinstaller --onefile --add-data "todo_data.db;." todo_list.py

You have various options for distributing your .exe file to users:

- **Direct Downloads**: You can host the .exe file on your website or server and offer users a direct link to download it. This method gives you complete control over distribution.

- **GitHub Releases**: If your project is on GitHub, you can utilize the Releases feature to distribute your .exe file. Upload the file as an asset when creating a new release, and users can download it from the Releases page.

- **Third-Party Platforms**: Several third-party platforms allow file hosting and distribution, including:
   - **Google Drive**: Upload the .exe file to Google Drive and share the download link.
   - **Dropbox**: Similar to Google Drive, you can upload the .exe file to Dropbox and share the link.
   - **OneDrive**: Microsoft's OneDrive offers file hosting and sharing capabilities.

You can download the executable file we made in this article by clicking [here][10].

# Conclusion
In conclusion, creating a calculator application that can add, subtract, multiply and divide, using **Tkinter** and converting it into a **.exe file** using **PyInstaller** is a straightforward process that opens up numerous opportunities for **software distribution**. By following the steps outlined in this article, you've learned how to harness the power of Tkinter to build intuitive graphical user interfaces and leverage PyInstaller to package your Python scripts into **standalone executables**.

Now that you've successfully created your calculator application and transformed it into a .exe file, it's time to share your creation with the world. Distributing your .exe files allows others to easily access and use your software, whether it's for personal or professional use. Whether you choose to host your files on your own website, share them via GitHub releases, or utilize third-party platforms, the possibilities for distribution are endless.



[1]: https://www.python.org/downloads
[2]: https://docs.python.org/3/library/tkinter.html
[3]: https://coderlegion.com/190/introduction-to-tkinter-library-in-python
[4]: https://docs.python.org/3/library/tk.html
[5]: pyinstl_calculator
[6]: pyinstl_exec1
[7]: pyinstl_exec2
[8]: pyinstl_exec3
[9]: pyinstl_flowchart
[10]: SimpleCalculator.exe
