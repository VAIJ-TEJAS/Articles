
**Flask** is a Python web framework, known for its **flexibility** and **versatility**. It seamlessly integrates multiple functionalities, including **authentication systems** and **database connectivity**. It emphasizes modular design, code readability and minimalism. In this article, we will explore **routing**, **templating** with **Jinja2**, **request handling** and designing **RESTful APIs** with Flask with code examples to aid understanding.

# Getting Started with Flask
Let's take a look and installing and setting up a Flask application.

<div class="div-blue"> <span class="alert-header">Note:</span> <span class="alert-body"> You may run the following on the terminal or in a code editor or IDE like Visual Studio Code.</span> </div>

1. Install Flask using the terminal:

		pip install flask

<div class="div-green"> <span class="alert-header">Tip:</span> <span class="alert-body"> Working in a virtual environment is recommended as it reduces conflicts with other projects and helps manage dependencies.</span> </div>

2. Create a virtual environment.

		python -m venv flaskenv
	Activation:
	- On Windows:

			flaskenv\Scripts\activate
	- On Linux or macOS:

			source flaskenv/bin/activate

3. Create your Flask application and navigate into it:

		mkdir first_app
		cd first_app

4. In this directory, we will create a Python file (app.py) to write our code in:

		from flask import Flask
		
		app = Flask(__name__)
		@app.route('/')
		def say_hello():
		    return 'Hello, World!'

		app.run(debug=True)

	`Flask(__name__)` creates an instance of the Flask class and `@app.route('/')` binds `say_hello` function to root URL of the web application. 

5. To run the application, we will set the `FLASK_APP` environment variable and then run it:
	
	- Setting on Windows:

			set FLASK_APP=app.py
	- Setting on Linux or macOS:

			export FLASK_APP=app.py
	- Run:

			flask run

This creates your first Flask application which outputs a "Hello, World" statement in the localhost.

Output:

![hello_term][1]

![hello_world][2]


# Routing
In Flask, you use routes to map URLs to functions in your web applications using the `@app.route` decorator. A route determines the logic that should be executed when a user visits a specific URL on your application. 

Different HTTP methods, including `GET`, `POST`, `PUT`, `DELETE`, etc., can be handled by Flask routes. A route only reacts to `GET` requests by default. You can determine the type of request and respond using `request.method`.

Let's understand it better using an example:

`app.py`:

	from flask import Flask, request
	
	app = Flask(__name__)

	@app.route('/')
	def home():
	    return '''
	        <h1>Welcome to the Home Page! Select any of the following links:</h1>
	        <p><a href="/about">About</a></p>
	        <p><a href="/contact">Contact</a></p>
	        <p><a href="/form">Form</a></p>
	    '''

	@app.route('/about')
	def about():
	    return 'This is a sample About Page. It is to demonstrate the use of routing in Flask.'

	@app.route('/contact', methods=['GET', 'POST'])
	def contact():
	    if request.method == 'POST':
	        return 'Contact me at sample@some.com. Handling POST Request'
	    else:
	        return 'Contact me at sample@some.com. Handling GET Request'

	@app.route('/form', methods=['GET', 'POST'])
	def form():
	    if request.method == 'POST':
	        name = request.form['name']
	        return f'Thank you, {name}!'
	    return '''
	        <form method="post">
	            Name: <input type="text" name="name">
	            <input type="submit">
	        </form>
	    '''

	app.run(debug=True)

This code first takes you to the Home page with 3 links:
- The `about` page has no requests specified. Hence, it reacts when a `GET` request is made.
- The `contact` page can handle `GET` and `POST` requests. It displays slightly different sentences depending on the request made.
- The `form` page displays a small form when a `GET` request is made. It processes the form data and displays a sentence with the name entered upon receiving a `POST` request.


Output:

![home][3]

![about][4]

![contact][5]

![form_get][6]

![form_post][7]


# Templates and Jinja2
You can incorporate dynamic HTML pages using Python embeddings in Flask by using Jinja2 templates. Jinja2 uses a number of features like filters, template inheritance, etc. to provide complex templates. It is essential to separate the application logic from the presentation logic in order to modularize your code.

**Creating and Rendering Templates in Flask**
<div class="div-green"> <span class="alert-header">Tip:</span> <span class="alert-body"> It is recommended to store your templates in a separate directory named `templates` within your project directory.</span> </div>

We will be using the example mentioned in the previous to build upon. Our code will consist of 4 HTML templates, each containing the structure of the Home, `about`, `contact` and `form` pages.

In the `templates` folder, create the following templates:

`index.html`:

	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <title>Home</title>
	</head>
	<body>
	    <h1>Welcome to the Home Page!</h1>
	    <p><a href="/about">About</a></p>
	    <p><a href="/contact">Contact</a></p>
	    <p><a href="/form">Form</a></p>
	</body>
	</html>

`about.html`:

	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <title>About</title>
	</head>
	<body>
	    <p>This is a sample About Page. It is to demonstrate the use of routing in Flask.</p>
	    <p><a href="/">Home</a></p>
	</body>
	</html>

`contact.html`:

	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <title>Contact</title>
	</head>
	<body>
	    <p>Contact Us</p>
	    <p>Contact me at sample@some.com. Handling {{ method }} Request</p>
	    <form method="post">
	        <input type="submit" value="Send POST Request">
	    </form>
	    <p><a href="/">Home</a></p>
	</body>
	</html>

`form.html`:

	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <title>Form</title>
	</head>
	<body>
	    <h1>Enter your name</h1>
	    {% if name %}
	        <p>Thank you, {{ name }}!</p>
	    {% else %}
	        <form method="post">
	            Name: <input type="text" name="name">
	            <input type="submit">
	        </form>
	    {% endif %}
	    <p><a href="/">Home</a></p>
	</body>
	</html>

Finally, these templates can be used in `app.py` using the `render_template()` function:

	from flask import Flask, render_template, request
	app = Flask(__name__)

	@app.route('/')
	def home():
	    return render_template('index.html')

	@app.route('/about')
	def about():
	    return render_template('about.html')

	@app.route('/contact', methods=['GET', 'POST'])
	def contact():
	    if request.method == 'POST':
	        return render_template('contact.html', method='POST')
	    return render_template('contact.html', method='GET')

	@app.route('/form', methods=['GET', 'POST'])
	def form():
	    if request.method == 'POST':
	        name = request.form['name']
	        return render_template('form.html', name=name)
	    return render_template('form.html', name=None)

	app.run(debug=True)

Notice that you can also pass dynamic data to your templates and have them stored in variables. In this example, `form.html` stores the name you enter and then displays it.
`contact.html` can also send a `POST` request, and the type of request is stored in the `method` variable and the page is updated accordingly.

Output:

![home_temp][8]

![about_temp][9]

![get_temp][10]

![post_temp][11]

![formget_temp][12]

![formpost_temp][13]


# Request Handling

The `request` object in Flask allows you to handle requests using the `GET` and `POST` parameters. `request.args` can be used to access `GET` parameters, whereas `request.form` can be used to access `POST` parameters.

`GET` parameters are used to retrieve data from the server. `POST` parameters are used to submit data to the server, which can then be processed.

The example provided previously displays how `POST` parameters can be used to alter the behaviour of the web app when a `POST` request is made.

We can build upon that code to display how `GET` parameters can be used. Let's use a template `greet.html` that uses a `GET` request to retrieve your name after entered, to display a greeting. You need to add the following lines to `app.py`:

	@app.route('/greet')
	def greet():
	    name = request.args.get('name')
	    return render_template('greet.html', name=name)

`greet.html`:

	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <title>Greet</title>
	</head>
	<body>
	    <h1>Greetings!</h1>
	    <form method="get" action="/greet">
	        <input type="text" name="name" placeholder="Enter your name">
	        <input type="submit" value="Greet">
	    </form>
	    {% if name %}
	        <p>Hello, {{ name }}!</p>
	    {% endif %}
	    <p><a href="/">Home</a></p>
	</body>
	</html>

Output:

![greet_get1][14]

![greet_get2][15]


**File Uploads with Flask**
You can easily provide an option to access an uploaded file in your web application using Flask. This is possible using `request.files` that accesses uploaded files.

Let's build upon the previous code to understand this better. Add these lines to `app.py`:

	@app.route('/upload', methods=['GET', 'POST'])
	def upload_file():
	    if request.method == 'POST':
	        file = request.files['file']
	        if file:
	            file.save(f"Downloads//{file.filename}")     # Change the path!
	            return f'File {file.filename} uploaded successfully!'
	    return render_template('upload.html')

`upload.html`:

	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <title>Upload File</title>
	</head>
	<body>
	    <h1>Upload a File</h1>
	    <form method="post" enctype="multipart/form-data">
	        <input type="file" name="file">
	        <input type="submit" value="Upload">
	    </form>
	    <p><a href="/">Home</a></p>
	</body>
	</html>

This code saves the file you upload, to the mentioned path.

Output:

![file1][16]

![file2][17]


**Handling JSON requests**
JSON format is mostly used to handle client-server exchange. It is a lightweight format and can also be interpreted easily by humans. Hence, handling JSON requests is essential in Flask and it is made easy with the help of `request.get_json()`.

Building upon the previous example, add the following lines to `app.py`:

	from flask import jsonify
	@app.route('/json', methods=['POST'])
	def json_example():
	    data = request.get_json()
	    name = data.get('name')
	    age = data.get('age')
	    response = {'message': f'Name: {name}, Age: {age}'}
	    return jsonify(response)

Now, we can send a `POST` request with `name` and `age` values in the terminal after running the program. The final output would look as follows:

![json][18]



[1]: hello_term.png
[2]: hello_world.png
[3]: routing1.png
[4]: routing2.png
[5]: routing3.png
[6]: routing4.png
[7]: routing5.png
[8]: home_temp.png
[9]: about_temp.png
[10]: get_temp.png
[11]: post_temp.png
[12]: formget_temp.png
[13]: formpost_temp.png
[14]: greet_get1.png
[15]: greet_get2.png
[16]: file1.png
[17]: file2.png
[18]: json.png
