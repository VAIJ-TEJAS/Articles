In this article, you'll learn about **scripting** in software development, using scripting languages to **automate** tasks, customize software, and speed up development. Scripting facilitates **rapid prototyping**, automates repetitive tasks, **integrates** software components, customizes and **extends functionality**, manages **deployment** and **configuration**, and automates **testing** and **quality assurance**. You'll be introduced to **Python**, known for its simplicity, readability, and popularity in automation, system administration, and rapid prototyping due to its ease of learning, extensive **standard library**, **platform independence**, and efficient task automation.

# Getting Started with Python Scripting
**Setting up the Python Environment**
- **Install Python**: Following are the steps to install Python in different OS.

	- **For Windows**: Download and install Python from the  [official website][1].
	    
	- **For Ubuntu**: You can download Python using the terminal:

	      sudo apt update
	      sudo apt install python3

	- **For MacOS**: You can download Python using Homebrew:
	    
	      brew install python3
	      
	Type `python --version`  in the command prompt or terminal to verify that Python is installed correctly.

- **Code Editor or IDE**: Choose a code editor or integrated development environment (IDE) for writing Python code like Visual Studio Code, PyCharm, IDLE, etc.
- **Install Packages**: You can install Python packages using the Python package manager, `pip`.

		pip install package_name

<div class="div-green"> <span class="alert-header">Tip:</span> <span class="alert-body"> Create a virtual environment for your Python project using `python -m venv env_name`, then activate it with `.\env_name\Scripts\activate`. To deactivate, run `deactivate`.</span> </div>

**Python Interpreter and .py files**
Python files with the `.py` extension store Python code and are generated using text editors or IDEs. The Python interpreter executes this code interactively for immediate input or in script mode for code from `.py` files. Running a Python script requires navigating to its folder in the command line and entering `python script.py`, simplifying Python program execution.

**Writing your first Python Script**
Let's start our scripting journey by writing the "Hello, World!" program in Python.
- Create a new file in the text editor named `hello.py`.
- Please write and save the code provided below:

		print("Hello World!")
- Open a command prompt or terminal and navigate to the directory containing the `hello.py` file.
- Execute your script using the command.:

		python hello.py


# Basics of Python Scripting
I highly recommend you to go through the [official documentation][2] to more about variable datatypes.

**Accepting Inputs**
The `input()` function in Python pauses the program, waiting for keyboard input. It returns the entered data as a string.

	name = input("Enter your name: ")
You can typecast it to int, float or bool as follows:
- int:

		age = int(input("Enter your age: "))
- float:

		temp = float(input("Enter temperature in F: "))
- bool:

		stud_bool = int(input("Are you a student? (True/False): "))

<div class="div-red"> <span class="alert-header">Caution:</span> <span class="alert-body"> If you enter a value that cannot be converted to the specified data type (Ex. typing "abc" when expecting an integer), it will result in a `ValueError`. </span> </div>

**Displaying Outputs**
The `print()` function is used to output text or values to the console.

	print("Hello! I'm George.")

Usage of the `print()` function can vary with different formatting techniques or additional parameters.
For each of the examples listed below, the following variables and their values are considered:

	item = "Lemons"
	quantity = 10
- Multiple items can be printed by separating them with commas.

		print("I need", quantity, item, "for this dish.")
	Output:
	
	![print1][3]

- Formatted strings (f-strings) embed variables or expressions directly within a string.

		print(f"Bring me {quantity} yellow {item} from the market.")
	Output:
	
	![print2][4]

- You can concatenate strings and variables using the `+` operator.

		print("We are " + str(quantity) + " " + item + " short!")
	Output:
	
	![print3][5]

- Specify the character or string to print at the output's end using the `end` parameter.

		items = ["Lemons", "Limes", "Oranges"]
		print(items[0], items[1], items[2], sep = ", ")
	Output:
	
	![print4][6]

- Specify the character or string to print at the output's end with the `end` parameter.

		print("I have only", quantity, end = " ")
		print(item, "left.")
	Output:
	
	![print5][7]

**Adding Comments**
Comments annotate code for explanations, documentation, or notes, enhancing readability and maintainability without affecting functionality.
- **Single-Line Comments**: Single-line comments in Python start with `#` and provide brief explanations on one line.

		x = 5				#The variable 'x' holds the value 5

- **Multi-Line Comments**: In Python, multi-line comments can be simulated using triple quotes (`'''` or `"""`). These strings, not assigned to any variable, act as comments and are ignored by the interpreter.

		""" 
		This sentence
		will be ignored by 
		the interpreter.
		"""

# Control Structures in Python
Control structures in Python manage code execution based on conditions or loops. They enable decision-making, action repetition, and selective code execution.

**Conditional Statements**: Conditional statements allow you to execute certain blocks of code based on specific conditions.
- **if statement**: Allows you to execute a block of code if a condition is true. If false, the code block is skipped.

		x = 6
		if (x%2 == 0):
			print("x is even.")
	Output:
	
	![if_stmt][8]
	
- **elif statement**: Stands for "else if." It follows an if statement and allows you to check additional conditions if the previous if or elif conditions are false.

		x = -7
		if (x%2 == 0):
		    print("x is even.")
		elif (x%2==1 and x<0):
		  	print("x is odd and negative.")
	Output:
	
	![elif_stmt][9]

- **else statement**: Optionally follows an if statement or a series of elif statements. It executes a block of code if none of the preceding conditions are true.

		x = 7
		if (x%2 == 0):
			print("x is even.")
		else:
			print("x is odd.")
	Output:
	
	![else_stmt][10]

**Loops**: Loops enable you to execute a block of code repeatedly.
- **For Loop**: Executes a block of code a fixed number of times, iterating over a sequence.

		for i in range(1, 6):       # i will start from 1 and end at 5
		    print(i)
	Output:
	
	![for_loop][11]

- **While Loop**: Runs code while a condition remains true.

		i = 5
		while i>0:
		    print(i)
		    i-=1
	Output:
	
	![while_loop][12]


# Functions and Modularization
**Functions**
Functions are code blocks performing specific tasks, taking input parameters, executing actions, and optionally returning results. They're defined with the `def` keyword, and parameters are specified inside parentheses after the function name.

	def add_nums(n1, n2):        # function to return sum of 2 numbers
	    return n1 + n2
Arguments are the actual values that are passed to the function when it is called. You can then call the function by its name and pass arguments.

	print(add_nums(2, 7))       # prints the value returned by the function
Output:

![function][13]

**Modular Programming**
Modularization divides a program into separate modules or components, with functions encapsulating related code for reusability. This enhances code organization, readability, and maintainability by enabling easy reuse of specific functionality.

Let's look at an example:
In Module `calculation.py`:

	def add_nums(n1, n2):
		return n1 + n2
In Module `stringops.py`:

	def concat_strs(s1, s2):
		return s1 + s2

The above modules can be imported and their functions can be used in your main program as follows:

	import calculation
	import stringops
	print(concat_strs("Jai", "Kumar"))
	print(add_nums(3, 7))


# File Handling in Python
Python file handling includes both reading from and writing to files. It allows you to interact with external files on your computer's file system.

**Reading from Files**
To open a file, use the `open()` function with the file path and desired mode. Once opened, you can read its contents using methods like `read()`, `readline()`, or `readlines()`.
- **`read()`**: The `read()` method reads the entire contents of the file and returns it as a string.

		with open("myfile.txt", "r") as file:
		    content = file.read()
		print(content)
	Output:
	
	![read][14]

- **`readline()`**: The `readline()` method reads a single line from the file and returns it as a string, advancing the file pointer to the next line with each call.

		with open("myfile.txt", "r") as file:
		    line1 = file.readline()
		    print(f"line1: {line1}")
		    line2 = file.readline()
		    print(f"line2: {line2}")
	Output:
	
	![readline][15]

- **`readlines()`**: The `readlines()` method reads all lines from the file and returns them as a list of strings. Each string in the list represents a file line.

		with open("myfile.txt", "r") as file:
		    lines = file.readlines()
		print(lines)
	Output:
	
	![readlines][16]

**Writing to Files**
To write data to a file, you open the file in write mode ("w") or append mode ("a") and use the `write()` method.

	with open("myfile.txt", "a") as file:
	    file.write("\nEnjoying so far?")
Before writing:

![write1][17]

After writing:

![write2][18]


<div class="div-red"> <span class="alert-header">Caution:</span> <span class="alert-body"> It's important to close it using the `close()` method to free up system resources.</span> </div>

**File Management**
The `os` module in Python offers functions for file management tasks like creating, deleting, and renaming files. To use it, import the module as follows:

	import os
1. Operations on **Directories**
	-  `os.mkdir(path)`: Creates a directory at the specified path.

			os.mkdir("newdir")
		Output:
		
		![mkdir][19]
	
	- `os.rmdir(path)`: Removes the directory at the specified path only if the directory is empty.

			os.rmdir("newdir")
	-  `os.rename(src, dst)`: Renames a directory or file  from `src` to `dst`.

			os.rename("newdir", "renamedir")
			os.rename("myfile.txt", "sampfile.txt)
	- `os.path.isdir(path)`: Checks if the path refers to a directory.

			os.path.isdir("renamedir")

2. Operations on **Files**
	- `os.path.exists(path)`: Verifies the existence of a file or directory at the given path.

			os.path.exists("myfile.txt")
	- `os.listdir(path)`: Return a list of files and directories in the specified directory.

			os.listdir("renamedir")
	- `os.path.getsize(path)`: Gets the size of a file in bytes.

			os.path.getsize("myfile.txt")


# Error Handling
Error handling in Python involves dealing with exceptions that may occur while executing your program. 
- **Try-Except Blocks**: The try block contains code that might trigger an exception, while the except block contains code to manage the exception. Let's use one to handle division by zero error.

		try:
		    num = 10
		    den = 0
		    result = num / den
		    print("Result:", result)
		except ZeroDivisionError:
		    print("Stop! Division by zero is not allowed.")

- **Finally Block**: You can use a finally block to ensure that certain code is executed regardless of whether an exception occurs. Let's use one to demonstrate file handling.

		try:
		    file = open("myfile.txt", "r")
		    content = file.read()
		    print(content)
		except FileNotFoundError:
		    print("Sorry, file not found.")
		finally:
		    if 'file' in locals():
		        file.close()
	The `finally` block always executes, irrespective of whether an exception occurs. It's typically used for cleanup tasks, such as closing files or releasing resources.

- **Else Block**: The `else` block in the try-except-finally structure executes when no exception occurs within the try block. It's useful for code that should run only when no exceptions are raised.

		try:
		    num = int(input("Enter a number: "))
		except ValueError:
		    print("Invalid input! Please enter a valid number.")
		else:
		    print("You entered:", num)
	If a non-integer value (like a string) is entered, a `ValueError` triggers the corresponding `except` block, printing an error message. Otherwise, the `else` block executes, printing the entered number.


# Advanced Scripting Techniques

**Regular Expressions**
Regular expressions (regex or regexp) define search patterns, widely used in text processing for pattern matching. Python's `re` module supports them.

- **Metacharacters** are special characters with a unique meaning in regular expressions.
	-   `.`: Matches any single character except newline.
	-   `^`: Matches the start of the string.
	-   `$`: Matches the end of the string.
	-   `*`: Matches zero or more of the preceding character.
	-   `+`: Matches one or more occurrences of the preceding character.
	-   `?`: Matches zero or one occurrence of the preceding character.
	-   `[]`: Matches any character found within the brackets.
	-   `|`: Matches either the expression before or after the pipe symbol.
	-   `{m}`: Exactly `m` occurrences.
	-   `{m, n}`: Between `m` and `n` occurrences.

- **Character classes** enable matching specific sets of characters.
	-   `\d`: Matches any digit (`[0-9]`).
	-   `\w`: Matches any alphanumeric character (`[a-zA-Z0-9_]`).
	-   `\s`: Matches any whitespace character (space, tab, newline).
	-   `\b`: Marks word boundary.

- **Anchors** indicate the position of a match within the text.
	-   `^`: Matches the start of the string.
	-   `$`: Matches the end of the string.

- **Escape sequences** are used to match special characters. For example `\.` matches a literal dot.

Let's look at an example:

	import re

	text = "The quick brown fox jumps over the lazy dog."
	pattern = r"\b\w{5}\b"
	matches = re.findall(pattern, text)
	print("Five-letter words:", matches)

It matches the expression with words comprising of exactly 5 letters and produces the following output:

![reg_exp][20]

**Command-Line Arguments**
Python's `argparse` module simplifies interacting with users via the command line by providing a robust method for parsing arguments and options.
- Import the `argparse` module.
- Create an ArgumentParser object.
- Add command-line arguments/options with `add_argument()`.
- Parse arguments using `parse_args()`.

<div class="div-blue"> <span class="alert-header">Note:</span> <span class="alert-body"> You can access the parsed arguments using dot notation on the `args` object.</span> </div>

Let's look at an example of a script to multiply two numbers:

	import argparse

	parser = argparse.ArgumentParser(description='Multiply two numbers')
	parser.add_argument('num1', type=float, help='First number')
	parser.add_argument('num2', type=float, help='Second number')
	args = parser.parse_args()
	result = args.num1 * args.num2
	print("Result:", result)
Save the above script in a file `CLI.py`. Run it in the command-line by typing:

	python CLI.py 5 7
It will multiply the numbers 5 and 7 and display the output:

![argparse][21]


# Scripting for Automation
Automation minimizes human intervention by using technology to perform tasks, enhancing efficiency and reducing manual effort. It streamlines operations across industries for tasks like data processing, report generation, software deployment, and testing.

Using Python scripts for web scraping and interacting with web APIs is common in data collection, analysis, and automation.
**Web scraping** extracts data from websites using libraries like **BeautifulSoup** and **Scrapy**.
**Web APIs** enable software to communicate over the web, with Python's **Requests** library facilitating HTTP requests and interactions.


# Testing and Debugging Scripts
Unit testing and test-driven development (TDD) are two software development practices aimed at enhancing code quality and reliability.

**Unit testing** involves testing isolated software components, like functions or methods, to ensure they perform as expected, aiding in bug detection and code maintainability.

**Test-driven development (TDD)** is a method of development where tests are written before code implementation. It encompasses writing failing tests, coding to pass them, and refactoring for improved design while ensuring test success.

Python's `unittest` module facilitates writing and running unit tests. It offers classes and methods for creating and executing test cases, automating verification of code components like functions and methods.

Let's proceed with an example. Here, I have created a `calc.py` file with a function to multiply two numbers:

	def multiply(n1, n2):
	    return n1 * n2

Then, I created a `test_calc.py` file consisting of test cases to validate the results of my function:

	import unittest
	from calc import multiply

	class TestMyMath(unittest.TestCase):
	    def test_multiply(self):
	        self.assertEqual(multiply(3, 6), 18)
	        self.assertEqual(multiply(5, 0), 0)
	        self.assertEqual(multiply(-5, 3), -15)
	        self.assertEqual(multiply(-12, -3), 36)

	if __name__ == '__main__':
	    unittest.main()
Import `unittest` and `multiply` from `calc`, create `TestMyMath` inheriting from `unittest.TestCase`, define `test_add` with `self.assertEqual()` to compare `multiply` results, and execute tests with `unittest.main()` from the command line:

	python test_calc.py
Output:

![unittest][22]

Debugging Python scripts is crucial for identifying and fixing errors. This can be achieved using breakpoints, print statements, and tools like `pdb`.
- **Print Statements**: Strategically insert print statements to output variable values, function calls, and control flow info, aiding in understanding the program's state.
- **Breakpoints**: Set breakpoints at suspected issue lines in the code. They halt program execution, enabling variable inspection and interactive code stepping.
- **Python Debugger (`pdb`)** : Utilize the built-in `pdb` module for interactive debugging. Insert the following lines at the desired location to initiate a debugging session.

		import pdb
		pdb.set_trace()


# Best Practices for Python Scripting
- Adhere to the [Python Enhancement Proposal (PEP) 8][23] style guide for writing clean and consistent Python code.
- Choose meaningful and descriptive names for variables, functions, classes, and modules to convey their purpose and intent.
- Break down your code into smaller, modular components with clear responsibilities.
- Use `try-except` blocks to catch and handle exceptions gracefully, preventing crashes and providing meaningful error messages.
- Provide inline comments to explain complex algorithms, non-obvious behavior, or edge cases.
- Write unit tests using frameworks like `unittest` to verify the correctness of your code.


# Conclusion
Python is a versatile language for software development, offering features like **syntax**, **conditional statements**, and **loops**. We explored **file** handling and **error** management, highlighting its robust capabilities. Python's scripting power is evident in automation and system administration tasks, aided by libraries like **`argparse`**. **Regular expressions** are potent tools for text processing and pattern matching. Testing with the **`unittest`** framework ensures code reliability and maintainability.

[1]: https://www.python.org/downloads
[2]: https://docs.python.org/3/library/datatypes.html
[3]: print1.png
[4]: print2.png
[5]: print3.png
[6]: print4.png
[7]: print5.png
[8]: if_stmt.png
[9]: elif_stmt.png
[10]: else_stmt.png
[11]: for_loop.png
[12]: while_loop.png
[13]: function.png
[14]: read.png
[15]: readline.png
[16]: readlines.png
[17]: write1.png
[18]: write2.png
[19]: mkdir.png
[20]: reg_exp.png
[21]: argparse.png
[22]: unittest.png
[23]: https://peps.python.org/pep-0008/
