
In this comprehensive guide, we embark on a journey into the realm of task automation using Python. We'll explore how Python can **streamline workflows** by automating repetitive tasks. From setup to practical examples, you'll learn **essential libraries**, **scheduling**, **testing**, and **deployment**.
# Task automation
Task automation helps in enhancing the  productivity by automating repeating tasks, reducing manual effort, and minimizing errors. This allows the organizations to streamline operations and redirect resources. Automation tools like Python comes in very handy for these tasks.

**Why Python for Task Automation?**
- **Simplicity**: Python's clear and easy-to-read syntax makes it ideal for automating tasks with minimal code complexity.  
- **Extensive Libraries**: A wealth of libraries, like `os`, `shutil`, `requests`, and `pandas`, provide tools for various automation tasks, from file management to data processing.  
- **Cross-Platform**: Python runs on multiple operating systems, allowing scripts to be used in diverse environments.  
- **Strong Community**: Python's large community offers extensive resources, tutorials, and support for automation-related queries. 
- **Rapid Prototyping**: Python's simplicity enables quick development and testing of automation scripts, allowing for rapid iteration and refinement.

# Getting Started with Python for Task Automation
**Setting Up the Python Environment**
The steps are given below: -
1.  **Install Python**: Download and install the latest version of Python from the official website ([https://www.python.org/downloads/](https://www.python.org/downloads/)). 
2.  **Choose an IDE**: Select an Integrated Development Environment (IDE) for Python development. 
3.  **Install Required Packages**: Use `pip`, the Python package manager, to install any additional packages or libraries. 	You need to install packages like `requests`, `beautifulsoup4`, or `pandas` for this guide using `pip install`. 
4. **Check Installation** : Make sure that python is installed correctly by using `python --version`, 
You have installed python successfully now write your first code and explore different concepts.

**Writing Your First Automation Script**
Let's create a simple Python script to automate a basic task, such as file management.

	import os
	
	def organize_files(directory):
	    for filename in os.listdir(directory):
	        if filename.endswith('.txt'):
	            # Move text files to a 'TextFiles' directory
	            os.rename(os.path.join(directory, filename), os.path.join(directory, 'TextFiles', filename))
	directory_path = 'C:\\Users\\dell\\Desktop\\temp'
	organize_files(directory_path)
![first](./img/first1.png)

# Essential Python Libraries for Automation

**OS Module**

The `os` module in Python provides a **platform-independent** way of interacting with the **operating system**, offering functions for various operating system-related tasks such as **file and directory operations**, **process management**.

**Example :**

    import os
    cwd = os.getcwd()
    print("Current directory:", cwd)
    
    new_dir = os.path.join(cwd, 'new_directory')
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        print("New directory created:", new_dir)
    else:
        print("Directory already exists:", new_dir)
    
    files = os.listdir(cwd)
    print("Files in current directory:", files)
    
    old_file = os.path.join(cwd, 'old_file.txt')
    new_file = os.path.join(cwd, 'new_file.txt')
    os.rename(old_file, new_file)
    print("File renamed from 'old_file.txt' to 'new_file.txt'")

![os_module](./img/os_module1.png)
<div class="div-blue"> <span class="alert-header">Note:</span> <span class="alert-body">While renaming the files make sure to create the file whose name you want to change.</span> </div>

**Shutil Module**

The `shutil` module offers a high-level interface for **file operations**, including file **copying**, **moving**, and **deletion**.

**Example :**

    import shutil
    source_file = 'C:\\Users\\dell\\Desktop\\temp\\source.txt'
    destination_file = 'C:\\Users\\dell\\Desktop\\temp\\destination.txt'
    
    try:
        shutil.copy(source_file, destination_file)
        print("File copied successfully!")
    except FileNotFoundError:
        print("Source file not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print("An error occurred:", e)

![shutil_module](./img/shutil_module1.png)
<div class="div-blue"> <span class="alert-header">Note:</span> <span class="alert-body">Make sure to pass the correct path of the source and destination file in the same way as mentioned above.</span> </div>

**Subprocess Module**

The `subprocess` module in Python provides a powerful way to **spawn** new processes. It allows you to execute **system commands**, **run external programs**, and interact with them programmatically from within your Python script.

**Example :**

    import subprocess
    try:
        #Run the command and capture output
        result = subprocess.run(['-l'], capture_output=True, text=True)
        # Print the command output
        print("Command output:", result.stdout)
    except FileNotFoundError:
        print("Command not found.")
    except Exception as e:
        print("An error occurred:", e)

![subprocess_module](./img/subprocess_module1.png)

**Scheduled Module**
The `schedule` module in Python provides us withe the most simple and intuitive way to schedule repeating tasks and automate job execution. With `schedule`, you can automate tasks like **data backups**, **report generation**, and **system maintenance**.

**Example :**

	import schedule
	import time

	def print_message():
	    print("This message is printed every second.")
	schedule.every(1).seconds.do(print_message)
	while True:
	    schedule.run_pending()
	    time.sleep(1)  # Wait for 1 second
![task_schedule](./img/task_schedule.png)
# Automating File and Data Management
**File Organization and Cleanup**
Automating file organization, renaming, and cleanup tasks can significantly improve efficiency and maintain a tidy file system. Python provides powerful tools for automating these processes such as `os` and `shutil`.

	import os
	import shutil

	def organize_files(directory):
	    if not os.path.exists(os.path.join(directory, 'Images')):
	        os.makedirs(os.path.join(directory, 'Images'))
	    if not os.path.exists(os.path.join(directory, 'Documents')):
	        os.makedirs(os.path.join(directory, 'Documents'))

    for filename in os.listdir(directory):
        if filename.endswith(('.jpg', '.png', '.gif')):
            shutil.move(os.path.join(directory, filename), os.path.join(directory, 'Images', filename))
        elif filename.endswith(('.pdf', '.docx', '.txt')):
            shutil.move(os.path.join(directory, filename), os.path.join(directory, 'Documents', filename))
    directory_path =  'C:\\Users\\dell\\Desktop\\temp'
    organize_files(directory_path)

![before_file](./img/before_file1.png) 
![after_file](./img/after_file1.png)

**Data Processing and Analysis**
Automate data processing tasks using libraries like `pandas` for **parsing**, **cleaning**, and **transforming** datasets.

	  import pandas as pd
	     data = {
	        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
	        'Age': [25, 30, 35, 40],
	        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
	      }
	    df = pd.DataFrame(data)
	    print("DataFrame:")
	    print(df)

![dataframe](./img/dataframe1.png)
# Web Scraping and Data Retrieval Automation
**Introduction to Web Scraping**

**Web scraping** is the process of extracting data from websites. It involves retrieving HTML content from web pages and then parsing and extracting the desired information. 
It is commonly used foe the following :-
-   **Data Collection**: Gathering information for analysis or research.
-   **Lead Generation**: Extracting contact information for sales.
-   **Content Aggregation**: Collecting and curating content from multiple sources.
-   **Search Engine Indexing**: Indexing web pages for search engines.

**Using BeautifulSoup and Requests**

`Beautiful Soup` and `requests` form a powerful combination for web scraping tasks. **Requests** is used to fetch the HTML content of web pages, while **Beautiful Soup** is employed to parse and extract data from the HTML, enabling to extract valuable information from websites through automation.

	import requests
	from bs4 import BeautifulSoup
	url = 'https://www.google.com'
	response = requests.get(url)

	if response.status_code == 200:
	    soup = BeautifulSoup(response.text, 'html.parser')
	    links = soup.find_all('a')
	    for link in links:
	        print(link.text)
	        print("Retrival of data successfull")
	else:
	    print("Failed to retrieve data from the website.")
     
![web_scrap](./img/web_scrap1.png)

**Automating Web Tasks**
Automate tasks such as **data scraping**, **form submission**, and **content extraction** from websites helps people to extract and discover more about the websites as well as reduce the time for filling of the form manually.

	import smtplib
	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart

	smtp_host = 'smtp.hostinger.com'
	smtp_port = 465
	sender_email = 'sender@gmail.com'
	receiver_email = 'receiver@gmail.com'
	password = 'password'

	message = MIMEMultipart()
	message['From'] = sender_email
	message['To'] = receiver_email
	message['Subject'] = 'Demo mail'

	message.attach(MIMEText('Welcome!! This is Test Mail.', 'plain'))

	try:
	    server = smtplib.SMTP_SSL(smtp_host, smtp_port)
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message.as_string())
	    print("Email sent successfully!")

	except Exception as e:
	    print(f"Failed to send email. Error: {e}")

	finally:
	    server.quit()
![email_send](./img/email_send.png)
# System Administration and Maintenance Automation
## Server Monitoring and Reporting
Automating server monitoring and generating status reports is crucial for maintaining the **health** and **performance** of systems. By scripting these tasks, administrators can proactively detect issues and  analyze system behavior to give more informations.

	import psutil
	import datetime

	def monitor_server():
	    cpu_usage = psutil.cpu_percent(interval=1)
	    memory_usage = psutil.virtual_memory().percent
	    disk_usage = psutil.disk_usage('/').percent
	    network_io = psutil.net_io_counters()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	    print("Timestamp:", timestamp)
	    print("CPU Usage:", cpu_usage, "%")
	    print("Memory Usage:", memory_usage, "%")
	    print("Disk Usage:", disk_usage, "%")
	    print("Network I/O (Bytes Sent/Received):", network_io.bytes_sent, "/", network_io.bytes_recv)
	monitor_server()
![sys_admin](./img/sys_admin1.png)

**Backup and Recovery Automation**
Automating **data backup** helps in disaster recovery and system restoration tasks. It is essential to ensure that the data integrity and continuity is maintained.

	import shutil
	import os
	import datetime

	def backup_data(source_dir, dest_dir):
	    #Generate timestamp for backup folder
	    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
	    
	    #Create a backup folder with timestamp
	    backup_folder = os.path.join(dest_dir, f"backup_{timestamp}")
	    os.makedirs(backup_folder)
	    
	    for root, dirs, files in os.walk(source_dir):
	        for file in files:
	            source_path = os.path.join(root, file)
	            dest_path = os.path.join(backup_folder, os.path.relpath(source_path, source_dir))
	            shutil.copy2(source_path, dest_path)
	    
	    print("Backup completed successfully.")

	source_directory = 'C:\\Users\\dell\\Desktop\\src'
	destination_directory = 'C:\\Users\\dell\\Desktop'
	backup_data(source_directory, destination_directory)
![backup](./img/backup1.png)

## Task Scheduling and Job Automation
**Introduction to Task Scheduling**
**Task scheduling** involves automating the execution of tasks or jobs at predefined times or intervals.

	import schedule
	import time
	def print_message():
	    print("Scheduled task: Hello, world!")

	schedule.every(5).seconds.do(print_message)

	while True:
	    schedule.run_pending()
	    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage
![task_schedule2](./img/task_schedule2.png)

**Using Cron Jobs (Unix) and Task Scheduler (Windows)**

	import os
	def create_task():
	    command = 'notepad.exe'
	    os.system(f'schtasks /create /sc once /tn "open_notepad" /tr "{command}" /st 00:00')
	
	if __name__ == "__main__":
	    create_task()
![task_auto](./img/task_auto1.png)
# Testing and Deployment Automation
## Introduction to Testing Automation
Automated testing involves the use of software tools and scripts to execute **test cases**, **validate functionality**, and identify defects in a software application.

**Using pytest and unittest**

`pytest` is a mature and feature-rich testing framework known for its simplicity and extensibility, which provides powerful features such as **fixtures**, **parameterized testing**, and **plugins**.

	class Calculator:
	    def add(self, a, b):
	        return a + b
	   def subtract(self, a, b):
	         return a - b
	calculator = Calculator()
	def test_addition():
	    assert calculator.add(2, 3)==5
	    assert calculator.add(5, -1)==4
	def test_subtraction():
	    assert calculator.subtract(5, 3)==2
	    assert calculator.subtract(10, 7)==3
![pytest](./img/pytest.png)

`unittest` is a built-in Python framework for automated testing that allows you to create, organize, and run test cases to test the validation of the data. It supports **test case classes**, **assertions**, **setup** and **teardown methods**. For more details prefer to [unnitest Documentation](https://docs.python.org/3/library/unittest.html) 

	import unittest

	def add(x, y):
	    return x + y

	class TestMathOperations(unittest.TestCase):

	    def test_addition(self):
	        self.assertEqual(add(2, 3), 5)
	        self.assertEqual(add(-1, 1), 0)
	        self.assertEqual(add(0, 0), 0)

	if __name__ == '__main__':
	    unittest.main()
![test_uni](./img/test_uni1.png)
# Best Practices for Task Automation with Python

When creating task automation scripts in Python, you need to follow the  best practices to ensure that your code is reliable, maintainable, and easy to understand. Here are some of the best practices that are listed below :-

- **Automated Testing**: Utilize `unittest` or `pytest` to create automated tests, ensuring your automation scripts works well.
- **Use Functions and Classes**: Organizing your code with functions and classes helps to build a better structure.
- **Robust Error Handling**: Using the `try/except` blocks helps you to manage the possible errors and helps in avoiding them.
- **Follow PEP 8**: Adhere to the Python style guide for consistent code formatting, using tools like `black` or `autopep8`.
 - **Modular Design**: Break your code into small, independent functions or modules to increase reusability and ease testing.
- **Clear Comments and Docstrings**: Add concise comments to explain complex code, and use docstrings for function and class descriptions.


# Conclusion
To sum it up, Python task automation can significantly boost efficiency and productivity by **streamlining** repetitive tasks and allowing you to focus on more critical work. Through Python's **user-friendly syntax**, **extensive libraries**, and strong community support, you can automate a variety of tasks, from **file management** and **data processing** to **system administration** and **web scraping**. As you dive into automation, follow best practices for maintainable and reliable scripts. Remember, to explore more about the Python Modules by visiting their [official website](https://www.python.org/).
