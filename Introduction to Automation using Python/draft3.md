

In this guide, we'll explore automation with Python. Automation is key in today's fast-paced world, saving time and effort across various tasks. **Python**, which is a top choice for **Automation**. We'll cover its essential libraries along with examples  for practical uses. By the end, you'll be ready to automate tasks efficiently using Python.

# Understanding Automation
**What is automation**

**Automation** is the use of technology to perform different tasks with minimal human intervention. It involves the implementation of systems or processes that can **operate automatically**, **reducing the need for manual labor** and **increasing efficiency**. 

**Why Automation is Important and Required:**

-   **Efficiency:** Streamlines processes, saving time and effort.
-   **Accuracy:** Minimizes human error, ensuring precision.    
-   **Cost Reduction:** Lowers labor costs, increases productivity.    
-   **Scalability:** Adapts easily to changing demands.     
-   **Productivity:** Frees up time for strategic work.     
-   **Data Analysis:** Provides valuable insights for decision-making.    
 
# Introduction of Python in  Automation

Python is a powerful language for automation tasks due to its **simplicity**, **versatility**, and **extensive libraries**. You can also visit [Python official site](https://docs.python.org/3/) for more information. 

## Python Modules for Automation

Given below are the essential python Modules to automate various tasks along with their examples for better understanding.

**1. Selenium :** A powerful tool for automating web browsers, which allows you to interact with web elements programmatically. It's widely used for **web scraping**, **testing** and **fill forms**  in web applications.

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import time
    
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_input = driver.find_element(By.NAME, "q")  # Google's search input element name is "q"
    
    search_input.send_keys("Python automation")
    search_input.send_keys(Keys.RETURN)
    
    time.sleep(60)
    driver.quit()

 ![selenium](./img/selenium2(2).jpg)

**2. PyAutoGUI :** This helps us to automate GUI interactions. It is useful for automating tasks involving graphical user interfaces, such as opening applications

    import pyautogui
    import time
    try:
        pyautogui.press('win')
        pyautogui.write('notepad')
        pyautogui.press('enter')
        time.sleep(4)  # Wait for Notepad to open
    
        pyautogui.write('Hello')
        time.sleep(2)  # Let's type slowly for demonstration
        pyautogui.hotkey('ctrl', 's')
        time.sleep(4)  # Wait for Save As dialog to open
        pyautogui.write('Hello.txt')
        time.sleep(2)  
        pyautogui.press('enter')
        time.sleep(2)  
    
        print("Task completed successfully!")
    except Exception as e:
        print("An error occurred:", e)

![pyautogui1][3]

![pyautogui2](./img/pyautogui2.png)

**3. Requests :** This is a simple yet elegant **HTTP library** for Python, which allows you to send HTTP requests easily. It's commonly used for web scraping, **accessing APIs**.
  
    import requests
    try:
      response = requests.get("https://www.google.com")
      if response.status_code == 200:
          print("Request to Google successful!")
          print("HTML Content:")
          print(response.text)
      else:
          print("Failed to retrieve data from Google. Status code:", response.status_code)
    except Exception as e:
      print("An error occurred:", e)

![request][6]

**4. Beautiful Soup :** It provides us with different functions for **parsing HTML and XML documents**. It allows you to extract data from web pages effortlessly, facilitating     automation of data extraction processes.

    from bs4 import BeautifulSoup
    import requests
    
    response = requests.get("https://www.google.com")
    #Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    for link in soup.find_all("a"):
        print(link.get_text())

![beautiful](./img/beautiful1.png)  
    
**5. Pandas :** `pandas` is a powerful **data manipulation** library that help us to form data frames. It's commonly used for automating data processing tasks, such as cleaning, transforming, and analyzing datasets.
    
     import pandas as pd
     data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
      }
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)

![dataframe][8]

# Getting Started with Automation

## How to Automate a Task: A Step-by-Step Guide

**Step 1: Identify Task**
Before moving to any planning the first step is to identify the repetitive and time-consuming tasks.

**Step 2: Divide the Task into Smaller Steps**
Break down the task into smaller, manageable modules. Then start working on each modules independently.

**Step 3: Research Python Libraries**
Research for those Python libraries that can help us in automating each step of the task. 

**Step 4: Write the Code**
Write Python code to automate each step of the task. Given below is a short example to get you started with scripting:

    import os
    import shutil
    
    file_types = set()
    for filename in os.listdir('directory_path'):
        if os.path.isfile(filename):
            file_types.add(filename.split('.')[-1])
            
    for file_type in file_types:
        os.makedirs(file_type, exist_ok=True)
        
    for filename in os.listdir('directory_path'):
        if os.path.isfile(filename):
            file_type = filename.split('.')[-1]
            shutil.move(filename, os.path.join(file_type, filename))
        
**Step 5: Test the Code**
After you are done with coding it's time to test it with a sample data to ensure that it performs well.

![flow1][9]

![flow2][10] 

**Step 6: Update the Code**

Refine and update the code as needed based on test results and feedback. Ensure it handles edge cases and exceptions gracefully.

# Introduction to Automation Scripting Languages

Scripting and automation have become **indispensable** tools for individuals and organizations alike. 

**Understanding Automation Scripting Languages:**
Automation scripting languages are programming languages that are specifically designed to automate repetitive tasks. These languages are having the predefined syntax and functionalities that are useful for automating tasks.

**Characteristics of Automation Scripting Languages:**
- **Readable Syntax**: Clear and concise code for easier comprehension.
- **Abundance of Libraries**: Extensive pre-built functions streamline development.
- **Interpretation or Compilation**: Code execution either directly (interpreted) or translated into machine language (compiled).
- **Cross-Platform Compatibility**: Capable of running on various operating systems. 

**Popular Automation Scripting Languages:**
1.  **Python**: Versatile, with rich libraries; used for automation, web dev, and data analysis.
2.  **Bash (Shell)**: Default on Unix; excels in system tasks and command-line ops.
3.  **PowerShell**: Microsoft's automation tool for Windows; robust system management.
# Essential Python Libraries for Automation
**OS Module** : The `os` module in Python provides a **platform-independent** way of interacting with the **operating system**.

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

![os_module][12]
<div class="div-blue"> <span class="alert-header">Note:</span> <span class="alert-body">While renaming the files make sure to create the file whose name you want to change.</span> </div>

**Shutil Module** : The `shutil` module offers a high-level interface for **file operations**, including file **copying**, **moving**, and **deletion**. You can gain more knowledge from [shutil module](https://docs.python.org/3/library/shutil.html#module-shutil)

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

![shutil_module](./img/shutil_module.png)
<div class="div-blue"> <span class="alert-header">Note:</span> <span class="alert-body">Make sure to pass the correct path of the source and destination file in the same way as mentioned above.</span> </div>

**Subprocess Module** : The `subprocess` module provides a powerful way to **spawn** new processes. It allows you to execute **system commands**, **run external programs**.For more details visit [subpress module](https://docs.python.org/3/library/subprocess.html)

**Example :**

    import subprocess
    try:
        result = subprocess.run(['-l'], capture_output=True, text=True)
        print("Command output:", result.stdout)
    except FileNotFoundError:
        print("Command not found.")
    except Exception as e:
        print("An error occurred:", e)

![subprocess_module][14]

**Time  and  Datetime Modules** : The `time` and `datetime` modules in Python provide functionalities for handling time-related tasks and scheduling automation jobs.
For further information check [Time module in python](https://docs.python.org/3/library/time.html#module-time)
**Example :**

    import time
    delay = 5
    start_time = time.time()
    while time.time() < start_time + delay:
        pass
    print("Automation job executed after {} seconds.".format(delay))

![time_date][15]
<div class="div-blue"> <span class="alert-header">Note:</span> <span class="alert-body">When this code is executed than after the delay of 5 seconds the message is displayed</span> </div>

# Web Scraping and Automation
**Web scraping** and **Automation**, empower users to automate repetitive tasks and extract valuable data from websites automatically. The users are able to interact with the web pages and extract data automatically.

**Automating Web Tasks**
Automation scripts can interact with web pages, submit forms, extract data, and perform other tasks, enabling the automation of web-based workflows.

 **Example**

    import requests
    from bs4 import BeautifulSoup
    url = "https://www.google.com"
    try:
      response = requests.get(url)
      if response.status_code == 200:
          print("Webpage accessed successfully!")
          soup = BeautifulSoup(response.text, 'html.parser')
          links = soup.find_all('a')
          for link in links:
              print(link.text)
          payload = {'username': 'your_username', 'password': 'your_password'}
          login_response = requests.post('https://www.example.com/login', data=payload)
          if login_response.status_code == 200:
              print("Login successful!")
          else:
              print("Login failed.")
      else:
          print("Failed to access the webpage.")
    except Exception as e:
      print("An error occurred:", e)

![web_scrap][16]

# Automating System Tasks
This  involves streamlining repetitive processes on both **Windows** and **Linux** operating systems, enhancing **productivity** and **efficiency**.

**Task Automation on Windows**

On **Windows**, PowerShell is a powerful automation tool that provides a wide range of `cmdlets` and scripts for managing system tasks. With **PowerShell**, you can automate tasks such as **file manipulation**, **registry editing**, **user management**, and **system configuration**.

**Example :**

    $sourceDir = "C:\Users\dell\Desktop\File1.txt"
    $destDir = "C:\Users\dell\Desktop\File2.txt"
    
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $backupFile = "backup_$timestamp.tar.gz"

    Compress-Archive -Path $sourceDir -DestinationPath "$destDir\$backupFile"
    Write-Host "Backup created: $destDir\$backupFile"

![powershell](./img/powershell.png)

# Data Processing and Automation

**Introduction to Data Processing**

**Data processing** is the method of transforming raw data into valuable information or insights. It involves several stages such as **data collection**, **cleaning**, **transformation**, **analysis**, and **visualization**.

**Using Pandas for Data Automation**

When the Python library `Pandas` is used for data automation then it allows efficient **processing**, **manipulation**, and **analysis** of data. `Pandas` is a powerful library that provides data structures such as `DataFrame` .

**Example :**

    import pandas as pd
    data = pd.read_csv('data.csv')
    data.head(7)
    df = pd.DataFrame(data)
    df.head()
    missing_values = df.isna().sum()
    print(missing_values)
    df_filled = df.fillna(0)
    df_filled.head(7)

![panda1][17] ![panda2][18]

# Testing and Automation

**Testing** and **automation** are crucial aspects of software development, ensuring **software reliability** and **quality**. It involves systematically evaluating software to find defects, while automation utilizes tools and scripts for efficient.

**Overview of Testing Automation**

Testing automation involves the use of software tools and frameworks to automate the process of testing software applications. One popular testing automation framework is `pytest`.

## Using pytest for Testing Automation

**Pytest** is a popular testing framework in Python known for its **simplicity** and **scalability**. It offers powerful features for writing and executing test cases efficiently. With `pytest`, developers can easily create **test functions**, **organize test suites**, and **assert expected outcomes**, making it suitable for both **small** and **large-scale projects**.

**Example :**

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

![py_test][19]

**NOTE:** Always save your `pytest` file with the following naming convention that is `test_filename`

# Real-World Automation Examples

- **Backup Automation**: Schedule regular backups of critical data to prevent loss in case of hardware failure or data corruption.
- **Server Maintenance**: Automate routine server maintenance tasks such as software updates, disk cleanup, and system reboots.
- **Report Generation**: Automatically generate and distribute reports on a scheduled basis, reducing manual effort and ensuring timely delivery.
- **Email Automation**: Implement automated email responses, email filtering, and email forwarding to streamline communication processes.
- **Data Migration**: Automate the migration of data between databases or cloud storage solutions to ensure accuracy and efficiency.
- **Customer Support**: Implement chatbots or automated ticketing systems to handle common customer inquiries and support requests.

# Conclusion

In conclusion, **Automation** with **Python** empowers individuals and organizations to **streamline workflows**, increase **productivity**, and **drive innovation**. By leveraging Python's simplicity, versatility, and rich ecosystem of libraries, automation enthusiasts can automate tasks across diverse domains, from **file operations** and **web scraping** to **system administration** and **data processing**. Remember to explore further, experiment with different libraries and tools, and apply best practices to create **efficient**, **reliable** automation solutions.


  [1]: https://logiclair.org/?qa=blob&qa_blobid=15838233321585473441
  [2]: https://logiclair.org/?qa=blob&qa_blobid=9123795144558585525
  [3]: https://logiclair.org/?qa=blob&qa_blobid=14912766778711305660
  [4]: https://logiclair.org/?qa=blob&qa_blobid=2396116423201933139
  [5]: https://logiclair.org/?qa=blob&qa_blobid=6172482470636820611
  [6]: https://logiclair.org/?qa=blob&qa_blobid=13033853441911983193
  [7]: https://logiclair.org/?qa=blob&qa_blobid=2098310934623573145
  [8]: https://logiclair.org/?qa=blob&qa_blobid=11465619741529268881
  [9]: https://logiclair.org/?qa=blob&qa_blobid=12988320224929339783
  [10]: https://logiclair.org/?qa=blob&qa_blobid=12229359629986255120
  [11]: https://logiclair.org/?qa=blob&qa_blobid=14061471290674041970
  [12]: https://logiclair.org/?qa=blob&qa_blobid=14821207025398722810
  [13]: https://logiclair.org/?qa=blob&qa_blobid=5755817284276135819
  [14]: https://logiclair.org/?qa=blob&qa_blobid=13235046775727453611
  [15]: https://logiclair.org/?qa=blob&qa_blobid=7133510508519989931
  [16]: https://logiclair.org/?qa=blob&qa_blobid=13203608641888015506
  [17]: https://logiclair.org/?qa=blob&qa_blobid=15419402808891249462
  [18]: https://logiclair.org/?qa=blob&qa_blobid=17675462299952413712
  [19]: https://logiclair.org/?qa=blob&qa_blobid=7916416413820548395
