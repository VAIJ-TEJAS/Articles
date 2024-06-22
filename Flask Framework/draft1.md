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



[1]: hello_term.png
[2]: hello_world.png
[3]: routing1.png
[4]: routing2.png
[5]: routing3.png
[6]: routing4.png
[7]: routing5.png
