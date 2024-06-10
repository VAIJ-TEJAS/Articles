Data gathering is made possible via **web scraping**, which automates the process of extracting information from websites. Powerful libraries like **Scrapy**, **BeautifulSoup**, and **Selenium**, together with its straightforward syntax, make **Python** the best choice. For **analysis** purposes, such as pricing tracking, review gathering, or news tracking, proficiency with web scraping is essential. In this article, we'll cover web scraping basics, usage of tools like BeautifulSoup, Selenium, and Scrapy and **Requests** for **API scraping**.

# Understanding Web Scraping
Web scraping makes use of a variety of tools and techniques to extract information.

**Techniques**
- **HTML Parsing**: It involves fetching HTML content of a webpage, like tags, attributes, or text content, and then parsing it to extract the desired data.
- **DOM (Document Object Model) Parsing**: It uses the browser's representation of the webpage and interacts with JavaScript-rendered content to scrape data from dynamic websites.
- **Regular Expressions (regex)**: It is used to match patterns in the HTML source code and use them as filters.

**Tools**
- **BeautifulSoup**: This Python module parses HTML and XML documents and can easily extract information by building a parse tree from the source code of webpages. Learn more [here][1].
- **Scrapy**: It is an effective Python library that uses self-contained crawlers called spiders, that extract data from websites. Learn more [here][2].
- **Selenium**: It's a browser automation tool that runs a web browser in a regular manner by scraping dynamic material generated using JavaScript. Learn more [here][3].
- **Requests**: It is an HTTP library for Python that allows you to send and handle HTTP requests and responses. Learn more [here][4].

**Legal Considerations**
- Many websites' Terms of Service (TOS) specifically ban scraping.
- Scraping data may breach copyright laws by extracting and using material without authorization.
- Always examine and respect a website's `robots.txt` file, which specifies which portions of the site can and cannot be scraped.

**Overview of HTML and CSS**

**HTML** is the standard markup language for creating and structuring web pages. It makes use of elements such as `<div>`, `<p>`, `<img>`, etc., and attributes that provide additional information about elements. It follows a tree-like hierarchy, called the DOM tree.
**CSS** controls the appearance, formatting, and layout of HTML components. It improves the visual attractiveness of websites while also ensuring uniform design across several pages.

# Installing and Configuring Web Scraping Libraries

<div class="div-blue"> <span class="alert-header">Note:</span> <span class="alert-body"> The following codes are run on the terminal or in a code editor or IDE like Visual Studio Code.</span> </div>

The libraries can be installed as follows:

- **BeautifulSoup**:

		pip install beautifulsoup4
- **Scrapy**:

		pip install scrapy
- **Selenium**:

		pip install selenium
- **Requests**:

		pip install requests

<div class="div-red"> <span class="alert-header">Caution:</span> <span class="alert-body"> Make sure `pip` is installed on your system.</span> </div>

Working in a virtual environment is recommended since it reduces conflicts with other projects and helps manage dependencies.

- Creating a virtual environment:

		python -m venv sampenv

- Activation:
	- On Windows:

			sampenv\Scripts\activate
	- On Linux and macOS:

			source sampenv/bin/activate

<div class="div-green"> <span class="alert-header">Tip:</span> <span class="alert-body"> Working in a virtual environment is recommended since it reduces conflicts with other projects and helps manage dependencies.</span> </div>

**Browser developer tools for inspecting web pages**

- **Inspect Element**: It allows you to view the HTML structure of the webpage. Select the element, right-click and select `Inspect`  to do so.
- **Console Tab**: You can run JavaScript code with it. It may be used to interact with the page's DOM to test JavaScript snippets.
- **Copy XPath or CSS Selector**: To locate elements in your web scraping script, right-click on an element in the `Elements` tab and pick `Copy`, `Copy XPath` or `Copy selector` to obtain the XPath or CSS selector.


# Basic Web Scraping with BeautifulSoup

BeautifulSoup is a Python library that works on HTML and XML files to extract data by creating a parse tree from a page source to traverse and find elements, attributes or text using methods like `find()` and `find_all()`.
- **Extracting Tags**
	- You can extract HTML tags like `<p>`, `<div>`, `<a>`, etc. using `find()` and `find_all()` methods.
	- Syntax:
		- `find()`: soup.find(tag_name, attrs={})
		- `find_all()`: soup.find_all(tag_name, attrs={})

- **Extracting Attributes**
	- HTML tag attributes can be extracted using the `get()` method or a dictionary-style access from the `find()` method.
	- Syntax:
		- tag = soup.find('tag_name')
		- `get()`: tag.get('attr_name')
		- Dictionary-style access: tag['attr_name']

- **Extracting Text**
	- Text contents of HTML elements can be accessed using the `get_text()` method or the  `.text` attribute.
	- Syntax:
		- tag = soup.find('tag_name')
		- `get_text()`: tag.get_text()
		- `.text`: tag.text

Let's take a look at an example to understand the methods better:

	from bs4 import BeautifulSoup

	html_content = """
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <title>Grocery List</title>
	</head>
	<body>
	    <div id="content">
	        <h1>Welcome to my List</h1>
	        <p>This is a list of my <strong>grocery items</strong>.</p>
	        <ul>
	            <li>Milk</li>
	            <li>Bread</li>
	            <li>Carrots</li>
	            <li>Butter</li>
	        </ul>
	        <a href="https://samp.com">Sample</a>
	    </div>
	</body>
	</html>
	"""

	soup = BeautifulSoup(html_content, 'html.parser')
	title_tag = soup.find('title')     # extracts Title tag
	h1_tag = soup.find('h1')     # extracts H1 tag
	p_tag = soup.find('p')
	ul_tag = soup.find('ul')
	a_tag = soup.find('a')

	print("Title:", title_tag.text)    # extracts text from Title tag
	print("H1:", h1_tag.get_text())    # extracts text from H1 tag
	print("Paragraph:", p_tag.text)
	print("List Items:")
	for li in ul_tag.find_all('li'):    # extracts list items
	    print("-", li.text)
	print("Link Href:", a_tag['href'])    # displays 'href' attribute's value

The code contains a sample HTML script, from which tags, attributes and texts are extracted.

Output:

![beautifulsoup][5]

# Scraping Dynamic Websites with Selenium
Selenium is a great tool for scraping dynamic webpages using JavaScript. It enables button clicks, form submissions, and page navigation by allowing programmatic control of a web browser.
In order to use Selenium, you need to set up Selenium WebDriver for your browser.
- **Google Chrome**
	- Download ChromeDriver from chromedriver.chromium.org
	- Set up ChromeDriver:

			from selenium import webdriver
			from selenium.webdriver.chrome.service import Service
			from webdriver_manager.chrome import ChromeDriverManager
			service = Service(ChromeDriverManager().install())
			driver = webdriver.Chrome(service=service)
			
- **Mozilla Firefox**
	- Download GeckoDriver from github.com/mozilla/geckodriver/releases.
	- Set up GeckoDriver:

			from selenium import webdriver
			from selenium.webdriver.firefox.service import Service
			from webdriver_manager.firefox import GeckoDriverManager
			service = Service(GeckoDriverManager().install())
			driver = webdriver.Firefox(service=service)

- **Microsoft Edge**
	- Download EdgeDriver from developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/.
	- Set up EdgeDriver:

			from selenium import webdriver
			from selenium.webdriver.edge.service import Service
			from webdriver_manager.microsoft import EdgeChromiumDriverManager
			service = Service(EdgeChromiumDriverManager().install())
			driver = webdriver.Edge(service=service)

**Extracting Elements**

- **find_element() Method**
	- To discover a single web element that meets the given criteria, use the `find_element()` function.
	- Syntax:
		- element = driver.find_element(By.ID, 'ID_value')

- **find_elements() Method**
	- Use the `find_elements()` function to find numerous web items that fit certain criteria. It will return a list of WebElement objects that represent all matched things.
	- Syntax:
		- elements = driver.find_elements(By.CLASS_NAME, 'Class_name_val')

- **get_attribute() Method**
	- It retrieves the value of an attribute like `href`, `src`, etc. from a web element.
	- Syntax:
		- link = driver.find_element(By.TAG_NAME, 'Tag_value')
		- href_value = link.get_attribute('attr_value')

- **text Property**
	- It extracts text content from elements like paragraphs, headings, or list items.
	- Syntax:
		- element = driver.find_element(By.CLASS_NAME, 'Class_val')
		- txt = element.text

- **send_keys() Method**
	- This method is helpful for input fields since it mimics typing into text fields or search boxes.
	- Syntax:
		- inp_box = driver.find_element(By.NAME, 'Name_value')
		- inp_box.send_keys('Hello!')

- **click() Method**
	- This method is used to click buttons, links, checkboxes, or any clickable element.
	- Syntax:
		- button = driver.find_element(By.ID, 'ID_value')
		- button.click()

- **execute_script() Method**
	- JavaScript code for advanced interactions, such as scrolling and event triggering, is executed via this method.
	- Syntax:
		- driver.execute_script("your_JS_code")
	- Example for scrolling: 
		- driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

Let's take a look at an example to understand it better:

samplepage.html:

	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <title>Sample Page for Selenium</title>
	    <script>
	        document.addEventListener('DOMContentLoaded', function() {
	            document.getElementById('dynamicButton').addEventListener('click', function() {
	                document.getElementById('dynamicContent').innerHTML = '<p class="dynamicText">I hope you are doing well.</p>';
	                document.getElementById('dynamicContent').innerHTML += '<a href="https://samp.com" class="dynamicLink">Example Link</a>';
	            });
	        });
	    </script>
	</head>
	<body>
	    <h1 id="pageTitle">Welcome!</h1>
	    <input type="text" id="inputField" name="inputName" placeholder="Enter something...">
	    <button id="dynamicButton">Load Content</button>
	    <div id="dynamicContent"></div>
	</body>
	</html>

Python script for data extraction:

	from selenium import webdriver
	from selenium.webdriver.chrome.service import Service
	from selenium.webdriver.common.by import By
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
	from webdriver_manager.chrome import ChromeDriverManager

	service = Service(ChromeDriverManager().install())
	driver = webdriver.Chrome(service=service)
	driver.get("samplepage.html")    # opens the webpage

	wait = WebDriverWait(driver, 20)
	page_title = wait.until(EC.presence_of_element_located((By.ID, 'pageTitle')))     # waits for 20 sec for page to load
	page_title = driver.find_element(By.ID, 'pageTitle')
	print("Page Title:", page_title.text)
	input_field = driver.find_element(By.NAME, 'inputName')
	input_field.send_keys('Hello, Alayne!')    # enters given data
	print("Input Field Value:", input_field.get_attribute('value'))
	dynamic_button = driver.find_element(By.ID, 'dynamicButton')
	dynamic_button.click()    # clicks the button
	wait = WebDriverWait(driver, 10)
	dynamic_text = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dynamicText')))
	print("Dynamic Text:", dynamic_text.text)
	dynamic_link = driver.find_element(By.CLASS_NAME, 'dynamicLink')
	print("Dynamic Link Href:", dynamic_link.get_attribute('href'))
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # scrolls
	driver.quit()    # close the browser

The code extracts data from the given JavaScript file and also enters data into the text field, clicks a button and scrolls through the webpage.

Output:

![selenium][6]


# Scraping with Scrapy

A Python-based framework for online crawling and scraping, Scrapy provides a number of tools for effectively extracting data from webpages. It effortlessly pulls data, follows links, and manages requests.  
An item is a container that item pipelines use to process and store scraped data. An item pipeline component is any Python class that implements a method on items.

Let's understand how to set up and define pipelines in for a Scrapy project using an example. We will be scraping [this][7] webpage


**Setting up Scrapy Projects and Defining Item Pipelines**

1. Open your terminal and go to the directory where you want to create a Python project.
2. Run the following command to create a Scrapy project consisting of files necessary for configuring the project.

		scrapy startproject scrapy_test
This creates a Scrapy project named `scrapy_test`.

3. Go to `items.py` in the `scrapy_test` folder. Here, you'll define a Scrapy item class, acting as a blueprint for your extracted data. Use `scrapy.Field()` to create field instances capable of storing any data type.

		import scrapy
		class  ScrapyTestItem(scrapy.Item):
			text = scrapy.Field()
			author = scrapy.Field()
			tags = scrapy.Field()
This code creates `text`, `author` and `tags` fields to store data from the webpage.

4. To set up the project settings, navigate to `settings.py`. This is where you design and configure the order of execution for the scraped item processing pipelines. Lower values indicate higher priority.

		ITEM_PIPELINES = {
		'scrapy_test.pipelines.JsonWriterPipeline': 300,
		'scrapy_test.pipelines.HtmlWriterPipeline': 800,
		}
This ensures that `JsonWriterPipeline` executes before `HtmlWriterPipeline`. These pipelines are defined in the next step.

5. Navigate to `pipelines.py`. This file handles data processing, including cleansing, verifying, storing, and exporting. Multiple pipelines can be defined here.

		import json
		class JsonWriterPipeline:
		    def open_spider(self, spider):
		        self.file = open('quotes.json', 'w')

		    def close_spider(self, spider):
		        self.file.close()

		    def process_item(self, item, spider):
		        line = json.dumps(dict(item), ensure_ascii=False) + "\n"     # extracted data is converted to JSON formatted string, and non-ASCII characters are handled properly.
		        self.file.write(line)
		        return item

		class HtmlWriterPipeline:
		    def open_spider(self, spider):
		        self.file = open('quotes.html', 'w')
		        self.file.write('<html><body><ul>')

		    def close_spider(self, spider):
		        self.file.write('</ul></body></html>')
		        self.file.close()

		    def process_item(self, item, spider):
		        self.file.write(f"<li><p>{item['text']}</p><p>{item['author']}</p><p>{', '.join(item['tags'])}</p></li>")     # extracted data is stored in a list format
		        return item

This code formats the fields and stores the extracted data into two files, `quotes.json` and `quotes.html`.

6. Open `scrapy_test/spiders`, then create `scrapy_code.py`. This file will include spider classes to define URLs to crawl, process answers, and retrieve data using XPath or CSS selectors. The item classes in `items.py` are used by the spider.

		import scrapy
		from scrapy_test.items import ScrapyTestItem

		class QuotesSpider(scrapy.Spider):
		    name = 'quotes'
		    start_urls = [http://quotes.toscrape.com]

		    def parse(self, response):
		        for quote in response.css('div.quote'):
		            item = ScrapyTestItem()
		            item['text'] = quote.css('span.text::text').get()
		            item['author'] = quote.css('span small::text').get()
		            item['tags'] = quote.css('div.tags a.tag::text').getall()
		            yield item

This code defines a spider named `quotes`. Using a CSS selector, it selects all elements with the class `quote` and creates a `ScrapyTestItem` instance for each. The `get()` method retrieves the text content and stores it in the respective fields.

7. In your terminal, navigate to the root directory of the project (`scrapy_test`) and run the command:

		scrapy crawl quotes

Where `quotes` is the spider we created.

The extracted data is stored in `quotes.json` and `quotes.html` in the project's root directory.

Output:

![jsonfile][8]

![htmlfile][9]


# Scraping APIs and JSON Data

Scraping APIs provide an organized way to obtain structured data. These APIs make endpoints available for accessing structured data in formats like XML and JSON. Using Requests, you may retrieve the required data by submitting queries to these endpoints and interpreting the returned responses.
Accessing APIs might involve the usage of API keys or tokens. Keys or tokens are specified in the `request header`.

**Making HTTP Requests and Accessing APIs**
1. Acquire the API key or token by generating the key/token in the platform of your choice.
2. Define the URL of the webpage you want to scrape and include the key/token in the request header. Also mention the content type.

		url = https://website_name.com/data
		api_key = 'abcxyz'
		header = { 'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json' }
3. Send an HTTP GET request to the specified URL with the provided headers using the `get()` method. It returns a `Response` object containing the server's response to the HTTP request, which can be used to extract the status code, content, etc.

		response = requests.get(url, headers=header)
4. If the `status code` of the response is 200, the request was successful and the contents can be extracted in text or JSON format.

		if response.status_code == 200:
			print(response.headers)
			print(response.text)    # or response.json()
		else:
			print(f"Error: {response.status_code}")

Let's take a simple example using the URL 'https://jsonplaceholder.typicode.com/todos/12'

	import requests
	url = 'https://jsonplaceholder.typicode.com/todos/12'
	header = {'Content-type': 'application/json'}
	response = requests.get(url, headers=header)
	if response.status_code == 200:
	    print(response.headers)
	    print(response.json())
	else:
	    print(f"Error: {response.status_code}")

This code does not involve the use of keys/tokens.

Output:

![apioutput][10]

You can also use `Requests` to download ZIP file. For example, to download a Kaggle dataset:

	import os
	import requests

	key = '82jfvyg3j4jngjr'    # Kaggle API key
	dataset_url = 'https://www.kaggle.com/datasets/vivek468/superstore-dataset-final'
	save_path = 'C:\\Downloads'    # replace with the path you want to store the file in

	response = requests.get(dataset_url, headers={'Authorization': f'Bearer {key}'}, stream=True)
	if response.status_code == 200:
	    with open(os.path.join(save_path, 'dataset.zip'), 'wb') as f:    # download the file
	        for chunk in response.iter_content(chunk_size=1024):
	            f.write(chunk)
	    print('Download successful.')
	else:
	    print('Failed to download dataset. Status code:', response.status_code)


Output:

![apikeyzip1][11]

![apikeyzip2][12]


# Conclusion
Thus, a potent method for obtaining data from websites is **Web Scraping**, which makes it possible to **gather** and **analyze** data effectively. The **requests** library, **BeautifulSoup**, **Selenium**, and **Scrapy** provide special benefits for various scraping requirements and enable developers to explore the web and retrieve important data easily. I encourage you to explore these tools further to unlock the full potential of web scraping to interact with and analyze web data.


[1]: https://beautiful-soup-4.readthedocs.io/en/latest/
[2]: https://docs.scrapy.org/en/latest/
[3]: https://www.selenium.dev/documentation/
[4]: https://requests.readthedocs.io/en/latest/
[5]: beautifulsoup.png
[6]: selenium.png
[7]: http://quotes.toscrape.com
[8]: jsonfile.png
[9]: htmlfile.png
[10]: apioutput.png
[11]: apikeyzip1.png
[12]: apikeyzip2.png
