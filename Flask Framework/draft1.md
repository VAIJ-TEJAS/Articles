
**Flask** is a Python web framework, known for its **flexibility** and **versatility**. It seamlessly integrates multiple functionalities, including **authentication systems** and **database connectivity**. It emphasizes modular design, code readability and minimalism. In this article, we will explore **routing**, **templating** with **Jinja2**, **request handling** and **Flask extensions** with code examples to aid understanding.

# Getting Started with Flask
Let's install and set up a Flask application.

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
4. In this directory, we will create a Python file `app.py` to write our code in:

		from flask import Flask
		
		app = Flask(__name__)
		@app.route('/')
		def say_hello():
		    return 'Hello, World!'

		app.run(debug=True)

	`Flask(__name__)` creates an instance of the Flask class and `@app.route('/')` binds `say_hello` function to the root URL of the web application. 

5. To run the application, we set the `FLASK_APP` environment variable and run it:
	
	- Setting on Windows:

			set FLASK_APP=app.py
	- Setting on Linux or macOS:

			export FLASK_APP=app.py
	- Run:

			flask run
This creates a Flask application that outputs "Hello, World" in the localhost.

Output:

![hello_term][1]

![hello_world][2]


# Routing
In Flask, routes map URLs to functions in your web applications using the `@app.route` decorator. A route determines the logic to be executed when a user visits a specific URL on your application.

Different HTTP methods like `GET`, `POST`, `PUT`, `DELETE`, etc., are handled by Flask routes. A route reacts to `GET` requests by default. You can determine the type of request and respond using `request.method`.

Let's look at an example:

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
You can incorporate dynamic HTML pages using Python embeddings in Flask by using Jinja2 templates. Jinja2 uses many features like filters, template inheritance, etc. to provide complex templates. It is essential to separate the application logic from the presentation logic to modularize your code.

**Creating and Rendering Templates in Flask**
<div class="div-green"> <span class="alert-header">Tip:</span> <span class="alert-body"> It is recommended to store your templates in a separate directory named `templates` within your project directory.</span> </div>

We will use the example mentioned in the previous to build upon. Our code will consist of 4 HTML templates, each containing the structure of the Home, `about`, `contact` and `form` pages.

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

Notice that you can also pass dynamic data to your templates and store them in variables. Here, `form.html` stores the entered name and displays it. `contact.html` stores the type of request in the `method` variable and the page is updated accordingly.

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
`greet.html` (body):

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

The `upload.html` script provides an option to upload files. This code saves the file you upload, to the mentioned path.

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
Now, send a `POST` request with `name` and `age` values in the terminal after running the program. The final output would look as follows:

![json][18]


# Flask Extensions
Flask offers several features, which can be accessed using libraries. Let's explore some of them.

**Flask-SQLAlchemy**
It allows you to access databases and perform CRUD operations, simplifying the use of SQL databases in Flask. Install it using the following command:

	pip install Flask-SQLAlchemy
**Flask-WTF**
It is a library that handles forms, validates entered data and renders HTML forms. It uses the WTForms library to do so. Install it by running:

	pip install Flask-WTF
**Flask-RESTful**
This library is useful to develop RESTful APIs and maintain API endpoints while following REST principles. Install it using the command:

	pip install Flask-RESTful
You can learn more by going through the [official documentation][27].
Here is an example of the Flask-SQLAlchemy extension:

	from flask import Flask, render_template
	from flask_sqlalchemy import SQLAlchemy

	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
	db = SQLAlchemy(app)

	class User(db.Model):
	    id = db.Column(db.Integer, primary_key=True)
	    username = db.Column(db.String(80), unique=True, nullable=False)
	    email = db.Column(db.String(120), unique=True, nullable=False)

	    def __repr__(self):
	        return f'<User {self.username}>'

	@app.route('/')
	def home():
	    users = User.query.all()
	    return render_template('entries.html', users=users)

	@app.route('/add')
	def add_users():
	    user1 = User(username='Amelia', email='amelia@some.com')
	    user2 = User(username='Harry', email='har2y@some.com')
	    db.session.add(user1)
	    db.session.add(user2)
	    db.session.commit()
	    return 'Users added! Go to the home page to see them.'

	with app.app_context():
	    db.create_all()
	app.run(debug=True)
This code creates a database named `users.db` upon execution. Going to the `/add` endpoint adds the sample users' data using the `db.session.add()` function and the changes are committed using the `db.session.commit()` function. The saved data is retrieved using `User.query.all()` function and displayed on the Home page.
A simple HTML template named `entries.html` is also used to display the database entries.

Output:

![sql_add][19]

![sql_home][20]


# Working with Databases
Here, we will learn to use Flask-SQLAlchemy in a bit more detail. As mentioned earlier, this library provides an easy way to interact with SQLite databases and perform CRUD operations on them.

When paired up with **Flask-Migrate**, you can handle database migration and update the structure of your database when needed. You can install it using the command:

	pip install Flask-Migrate
- Initialize a migrations directory by running:

		flask db init
	This is done only once.
- In the previous example, if the model `User` is altered to add a new column `age`, the changes are induced to the database by running:

		flask db migrate -m "New column added"
	This detects changes and generates a migration script.
- To save changes, run:

		flask db upgrade

**CRUD Operations**
The new model would look as follows:

	from flask_migrate import Migrate
	migrate = Migrate(app, db)

	class User(db.Model):
	    id = db.Column(db.Integer, primary_key=True)
	    username = db.Column(db.String(100), unique=True, nullable=False)
	    email = db.Column(db.String(120), unique=True, nullable=False)
	    age = db.Column(db.Integer)

- Create and Retrieve: The `User.query.all()` retrieves all existing records to display, and `db.session.add()` adds a new record, while `db.session.commit()` commits the changes.

		@app.route('/', methods=['GET', 'POST'])
		def user_list():
		    if request.method == 'POST':
		        username = request.form['username']
		        email = request.form['email']
		        age = int(request.form['age']) if request.form['age'] else None
		        new_user = User(username=username, email=email, age=age)
		        db.session.add(new_user)
		        db.session.commit()
		        return redirect(url_for('user_list'))

		    users = User.query.all()
		    return render_template('entries.html', users=users)
- Update: The unique `id` of an entry to be updated is retrieved using `User.query.get_or_404(id)` and the changes are committed using `db.session.commit()`.

		@app.route('/update/<int:id>', methods=['GET', 'POST'])
		def update_user(id):
		    user = User.query.get_or_404(id)
		    if request.method == 'POST':
		        user.username = request.form['username']
		        user.email = request.form['email']
		        user.age = int(request.form['age']) if request.form['age'] else None
		        db.session.commit()
		        return redirect(url_for('user_list'))
		    return render_template('entries.html', user=user)
- Delete: The `id` of a record is retrieved and deleted using `db.session.delete()`.

		@app.route('/delete/<int:id>', methods=['POST'])
		def delete_user(id):
		    user = User.query.get_or_404(id)
		    db.session.delete(user)
		    db.session.commit()
		    return redirect(url_for('user_list'))

Output:

![crud1][21]

![crud2][22]


# Authentication and Authorization
Session management tasks like logging in and logging out, can be handled easily using the **Flask-Login** library. It can be installed using the following command:

	pip install Flask-Login
The **Flask-Principal** library is used for stronger security, which offers role-based access control (RBAC). It restricts access to certain actions, depending on the user's role. To install Flask-Principal, run:

	pip install Flask-Principal
- Import the necessary libraries to start the project:

		from flask import Flask, request, render_template, redirect, url_for
		from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
		from flask_principal import Principal, RoleNeed, identity_loaded, UserNeed, Identity, AnonymousIdentity, identity_changed

		app = Flask(__name__)
		app.secret_key = 'sample'  # Replace with a stronger key

		users = {1: {'id': 1, 'username': 'Har2y', 'password': 'harrypass', 'roles': ['admin']},
		    2: {'id': 2, 'username': 'Amelia', 'password': 'bedeliamy', 'roles': []},}
	The secret key is needed to enable session cookies and for security. We have created two sample users, `Har2y` (admin), and `Amelia`.
- Create and initialize instances to enable authentication and RBAC:

		login_manager = LoginManager()
		login_manager.init_app(app)
		login_manager.login_view = 'login'
		principals = Principal(app)
- Create a class that inherits `UserMixin` to provide default implementation to methods like `is_authenticated` (checks if the user is authenticated), `is_active` (checks if an account is active), etc. and define attributes:

		class User(UserMixin):
		    def __init__(self, user_data):
		        self.id = user_data['id']
		        self.username = user_data['username']
		        self.password = user_data['password']
		        self.roles = user_data.get('roles', [])
- Create functions to load a user object based on their `id` and assign roles upon authentication.

		@login_manager.user_loader
		def load_user(user_id):
		    user_data = users.get(int(user_id))
		    if user_data:
		        return User(user_data)
		    return None

		@identity_loaded.connect_via(app)
		def on_identity_loaded(sender, identity):
		    identity.user = current_user
		    if hasattr(current_user, 'id'):
		        identity.provides.add(UserNeed(current_user.id))
		        if current_user.roles:
		            for role in current_user.roles:
		                identity.provides.add(RoleNeed(role))
- A function for logging in accepts the username and password and checks if the details entered are correct.

		@app.route('/', methods=['GET', 'POST'])
		def login():
		    if request.method == 'POST':
		        username = request.form['username']
		        password = request.form['password']
		        user = next((u for u in users.values() if u['username'] == username and u['password'] == password), None)
		        if user:
		            user_obj = User(user)
		            login_user(user_obj)
		            identity_changed.send(app, identity=Identity(user['id']))
		            return redirect(url_for('dashboard'))
		    return render_template('login.html')
- The user is taken to the dashboard if the credentials are correct.

		@app.route('/dashboard')
		@login_required
		def dashboard():
		    return f'Hello, {current_user.username}! <a href="{url_for("logout")}">Logout</a>'
- The `/admin` endpoint can be accessed only by admins who have logged in.

		@app.route('/admin')
		@login_required
		def admin():
		    if 'admin' in current_user.roles:
		        return 'You are an admin!'
		    return 'Access Denied!'
- When the user logs out, a function changes the identity to anonymous and redirects to the Login Page.

		@app.route('/logout')
		@login_required
		def logout():
		    logout_user()
		    identity_changed.send(app, identity=AnonymousIdentity())
		    return redirect(url_for('login'))

		app.run(debug=True)

Output:

![login][23]

![dashboard][24]

![har2y_admin][25]

![amelia_admin][26]


# Conclusion
Flask offers robust tools for modern web development, including extensions like **Flask-Login** and **Flask-Principal** to streamline user management and provide security, enhancing application security. By integrating **SQLAlchemy** for CRUD operations, Flask ensures scalable and efficient data handling, making it a versatile option for building dynamic web apps in Python.

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
[19]: sql_add.png
[20]: sql_home.png
[21]: crud1.png
[22]: crud2.png
[23]: login.png
[24]: dashboard.png
[25]: har2y_admin.png
[26]: amelia_admin.png
[27]: https://flask-restful.readthedocs.io/en/latest/
