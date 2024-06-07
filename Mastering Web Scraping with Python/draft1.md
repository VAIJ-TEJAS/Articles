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

![5][beautifulsoup]

# Scraping Dynamic Websites with Selenium




[1]: https://beautiful-soup-4.readthedocs.io/en/latest/
[2]: https://docs.scrapy.org/en/latest/
[3]: https://www.selenium.dev/documentation/
[4]: https://requests.readthedocs.io/en/latest/
[5]: beautifulsoup.png
