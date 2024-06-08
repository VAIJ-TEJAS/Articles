**Web scraping** is the automated process of extracting information from websites, allowing you to collect huge amounts of statistics quickly and efficaciously. **Python** is an effective tool for this task due to its simple syntax and robust libraries like **BeautifulSoup**, **Scrapy**, and **Selenium**. Understanding web scraping is crucial for leveraging online data for **analysis**, whether you're monitoring prices, collecting reviews, or monitoring news. In this article, we'll explore the basics of web scraping, how Python can help you get started, and best practices for ethical scraping.

# Understanding Web Scraping
Web scraping makes use of a variety of tools and techniques to extract information.

**Techniques**
- **HTML Parsing**: It involves fetching HTML content of a webpage, like tags, attributes, or text content, and then parsing it to extract the desired data.
- **DOM (Document Object Model) Parsing**: It uses the browser's representation of the webpage and interacts with JavaScript-rendered content to scrape data from dynamic websites.
- **Regular Expressions (regex)**: It is used to match patterns in the HTML source code and use them as filters.

**Tools**
- **BeautifulSoup**: It is a Python library for parsing HTML and XML documents. It creates a parse tree from web page source code that can be used to extract information easily. Learn more [here][1].
- **Scrapy**: It is an effective Python library that uses self-contained crawlers called spiders, that extract data from websites. Learn more [2][here].
- **Selenium**: It is a browser automation tool that scrapes dynamic content rendered by JavaScript. It controls a web browser and allows you to interact with web pages normally. Learn more [3][here].
- **Requests**: It is an HTTP library for Python that allows you to send and handle HTTP requests and responses. Learn more [4][here].

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

**Dynamic Websites and their Challenges for Web Scraping**

Websites that are dynamic produce material based on server-side processing or user interactions. This poses challenges for web scraping due to the dynamic nature of the content delivery.
- Dynamic websites load the contents of the page asynchronously using JavaScript. Conventional web scraping tools like BeautifulSoup or Scrapy may lead to incomplete data extraction.
- Since restricted material frequently requires user logins, session, cookie, and authentication token, management can be difficult, particularly for lengthy scraping jobs.  
- In order to collect all the data from websites with endless scrolling, users must simulate their behavior and watch network requests as additional material loads down the page.  
- Websites that use parameterized dynamic URLs make scraping more difficult since it can be challenging and error-prone to create and maintain these URLs dynamically.

**Selenium for Automated Web Browser Interaction**

When it comes to web scraping dynamic websites with JavaScript-loaded content, Selenium is an extremely useful tool. It makes it possible to programmatically operate a web browser, providing features like button clicks, form submission, and page navigation.
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
	- Synatx:
		- element = driver.find_element(By.ID, 'ID_value')

- **find_elements() Method**
	- To identify several web items that meet the given criteria, use the `find_elements()` function. All matched items are represented by a list of WebElement objects.
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
	driver.get("samplepage.html")    # open the webpage

	wait = WebDriverWait(driver, 20)
	page_title = wait.until(EC.presence_of_element_located((By.ID, 'pageTitle')))     # to wait for 20 sec for page to load
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

Scrapy is a high-level Python-based web crawling and scraping framework. It offers an extensive collection of tools and technologies to support developers in efficiently and methodically extracting data from websites. Scrapy can manage requests, follow links, and extract data from web pages with ease.
An item is a container that stores scraped data. The objects that your spiders scrape are processed by item pipelines in Scrapy. Every Python class that implements a basic method that takes an item and acts upon it, makes up an item pipeline component.

Let's understand how to set up and define pipelines in for a Scrapy project using an example. We will be using the following HTML script, stored as `samplepage.html`.

	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Sample Quotes Page</title>
	</head>
	<body>
	    <div class="quote">
	        <span class="text">"The only limit to our realization of tomorrow is our doubts of today."</span>
	        <span> - <small>Franklin D. Roosevelt</small></span>
	        <div class="tags">
	            <a class="tag" href="/tag/inspiration">inspiration</a>
	            <a class="tag" href="/tag/tomorrow">tomorrow</a>
	        </div>
	    </div>
	    <div class="quote">
	        <span class="text">"In the end, we will remember not the words of our enemies, but the silence of our friends."</span>
	        <span> - <small>Martin Luther King Jr.</small></span>
	        <div class="tags">
	            <a class="tag" href="/tag/friendship">friendship</a>
	            <a class="tag" href="/tag/memory">memory</a>
	        </div>
	    </div>
	</body>
	</html>

**Setting up Scrapy Projects and Defining Item Pipelines**

1. Open your terminal and go to the directory where you want to create a Python project.
2. Run the following command to create a Scrapy project consisting of files necessary for configuring the project.

		scrapy startproject scrapy_test
This creates a Scrapy project named `scrapy_test`.

3. Navigate to the `items.py` file in the `scrapy_test` folder.  Here, you will be defining a Scrapy item class, which acts as a blueprint for the data you will be extracting. For doing so, `scrapy.Field()` is used, which creates field instances to store any type of data in.

		import scrapy
		class  ScrapyTestItem(scrapy.Item):
			text = scrapy.Field()
			author = scrapy.Field()
			tags = scrapy.Field()
This code creates `text`, `author` and `tags` fields to store data from the webpage.

4. Navigate to `settings.py` file. Here, you can configure various settings for your project. We will be defining the pipelines that will be applied to process the scraped items, as well as their order of execution and priority. Lower the priority value, higher is the priority.

		ITEM_PIPELINES = {
		'scrapy_test.pipelines.JsonWriterPipeline': 300,
		'scrapy_test.pipelines.HtmlWriterPipeline': 800,
		}
This ensures that `JsonWriterPipeline` executes before `HtmlWriterPipeline`. These pipelines are defined in the next step.

5. Navigate to `pipelines.py` file. Processing of the scraped data, including cleansing, verifying, storing, and exporting, is handled via pipelines. Multiple pipelines can be defined in this file.

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

This code stores the extracted data in two files: `quotes.json` and `quotes.html`. The data extracted in the fields defined previously is stored in the two files in a formatted manner.

6. Navigate to scrapy_test/spiders and create a new Python Source file named `scrapy_code.py`. Here, we will be creating spider classes to perform the scraping. Spider classes describe which URLs to crawl, parse the responses, and then use XPath or CSS selectors to retrieve data from webpages. The item classes defined in the `items.py` file are used by the spider.

		import scrapy
		from scrapy_test.items import ScrapyTestItem
		import urllib.parse
		import urllib.request

		class QuotesSpider(scrapy.Spider):
		    name = 'quotes'
		    file_url = urllib.parse.urljoin('file:', urllib.request.pathname2url("samplepage.html"))     # make sure to swap out the given path with your own
		    start_urls = [file_url]

		    def parse(self, response):
		        for quote in response.css('div.quote'):
		            item = ScrapyTestItem()
		            item['text'] = quote.css('span.text::text').get()
		            item['author'] = quote.css('span small::text').get()
		            item['tags'] = quote.css('div.tags a.tag::text').getall()
		            yield item

This code creates a spider class and names the spider as `quotes`. Using a CSS selector, it selects all HTML elements with the class `quote` within the response HTML and creates a new instance of `ScrapyTestItem` class for each element. The `get()` method retrieves textual contents of each element and stores them in their respective field instances.

7. In your terminal, navigate to the root directory of the project (`scrapy_test`) and run the command:

		scrapy crawl quotes

Where `quotes` is the spider we created.

The extracted data is stored in `quotes.json` and `quotes.html` in the project's root directory.

Output:

![jsonfile][7]

![htmlfile][8]









[1]: https://beautiful-soup-4.readthedocs.io/en/latest/
[2]: https://docs.scrapy.org/en/latest/
[3]: https://www.selenium.dev/documentation/
[4]: https://requests.readthedocs.io/en/latest/
[5]: beautifulsoup.png
[6]: selenium.png
[7]: jsonfile.png
[8]: htmlfile.png
