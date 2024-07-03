**RESTful APIs** are an integral part of modern **web development** due to their **scalability** and ability to **communicate** across various platforms over the internet. They are built using the Python frameworks **Flask**, which is known for its flexibility, and **Django**, which comes with a multitude of features including database management, authentication, etc. RESTful APIs adhere to the principles of Representational State Transfer (REST), which is used to create networked applications, identified by **URIs (Uniform Resource Identifiers)** and handled using HTTP methods.  In this article, we'll explore how to use Flask and Django to build RESTful APIs along with code examples.

# Introduction to RESTful APIs
REST is a design framework that comprises of statelessness, a uniform interface, and a client-server architecture, for developing scalable web services. HTTP methods determine the actions that can be performed on a resource in RESTful API designs. Let's take a look at the most commonly used HTTP methods and their CRUD operations:

- **GET**: Retrieves data from the server.
- **POST**: Adds a new resource to the server.
- **PUT**: Updates an existing resource on the server.
- **DELETE**: Removes a resource from the server.

<div class="div-blue"> <span class="alert-header">Note:</span> By mapping CRUD operations to HTTP methods, RESTful APIs provide a standardized way to interact with resources.</div>

# Setting Up Flask/Django Projects for API Development
**Creating a new Flask/Django project**

- Flask:

    - To install Flask, run this command in the terminal:

            pip install Flask

    - Then, create a new project directory and navigate into it:

            mkdir flask_project
            cd flask_project

- Django:

    - Install Django by running this command in the terminal:

            pip install django

    - Then, create a new Django project and navigate into it:

            django-admin startproject django_project
            cd django_project

**Installing necessary dependencies for API development**

- Flask:

    - You will need to install Flask-RESTful for building RESTful APIs:

            pip install Flask Flask-RESTful
<div class="div-red"> <span class="alert-header">Caution:</span> You might need additional packages depending on your requirements. </div>
 
- Django:

    - Django comes with built-in packages for creating APIs, but you might need additional packages like Django REST framework for more advanced features:

            pip install django djangorestframework

**Running the development server**

- Flask:

    - To run the development server for Flask, execute your `app.py` file:

            python app.py

        This will start a development server on `http://127.0.0.1:5000/` by default.

- Django:

    - For Django, you use `manage.py` to run the development server:

            python manage.py runserver

        The development server will be accessible at `http://127.0.0.1:8000/` by default.

For more detailed guides, refer to the official documentation for [Flask][1] and [Django][2].

# Handling Requests and Responses
**Serializing and Deserializing Data (JSON, XML) in Flask/Django** In web applications, it's common to send and receive data in JSON or XML formats. Flask and Django allow serializing and deserializing data to and from these formats.

In Flask, you can use the `jsonify` function to serialize Python objects to JSON:

    from flask import jsonify
    data = {'name': 'John', 'age': 30}
    return jsonify(data)

In Django, you can use serializers to serialize querysets or model instances to JSON:

    from django.core.serializers import serialize
    data = serialize('json', SomeModel.objects.all())

**Constructing HTTP Responses with Appropriate Status Codes** Flask and Django allow you to construct HTTP responses to indicate the success or failure of a request.

Let's look at examples demonstrating request handling and response construction:

- Flask:

        from flask import Flask, jsonify, request, make_response
        app = Flask(__name__)
  
        @app.route('/', methods=['GET'])
        def hello():
            name = request.args.get('name', 'Guest')
            return f'Hello, {name}!'

        @app.route('/not_found')
        def not_found():
            response = make_response('Resource not found', 404)
            return response

        @app.route('/json_ex')
        def json_example():
            data = {'message': 'Hello, JSON!'}
            return jsonify(data)

        app.run(debug=True)

    Upon running the code, the page displays a welcome message. The `/not_found` endpoint will display the error message, and the `json_ex` endpoint displays the searialised data in JSON format.

- Django:`views.py`:

        from django.http import HttpResponse, JsonResponse, HttpResponseNotFound

        def hello(request):
            name = request.GET.get('name', 'Guest')
            return HttpResponse(f'Hello, {name}!')

        def not_found(request):
            return HttpResponseNotFound('Resource not found')

        def json_example(request):
            data = {'message': 'Hello, JSON!'}
            return JsonResponse(data)

    `urls.py`:

        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.hello, name='hello'),
            path('not_found/', views.not_found, name='not_found'),
            path('json_ex/', views.json_example, name='json_example'),
        ]

    This code has the same functionality as the Flask's code.

The outputs of both the codes will be the same:

![hello][3]

![error][4]

![json][5]

# URL Routing and Resource Endpoints
URL routes are the entry points to access different resources or functionalities of a web application. In Flask or Django, URL routes are defined in the application's main **URL configuration file**, where each route is associated with a specific HTTP method and corresponds to a particular view.

Once the URL routes have been created, they must be mapped to the relevant views or viewsets containing the actual business logic. In Flask, views are Python functions marked with `@app.route` decorator, but in Django, views are generally specified as methods within a class-based viewset in the `urls.py` file.

A URL route for retrieving a specific resource will resemble this format:

    /api/resource/<resource_id>/

And in the view or viewset, you can access `resource_id` to retrieve the specific resource with that identifier.

Let's take a look at examples to understand this better:

- Flask:

        from flask import Flask, jsonify
        app = Flask(__name__)

        @app.route('/user/<username>', methods=['GET'])
        def get_user(username):
            users = {
                'alice': {'name': 'Alice', 'age': 30},
                'bob': {'name': 'Bob', 'age': 25}
            }
            user = users.get(username, 'User not found')
            return jsonify(user)

        app.run(debug=True)

    This code displays the details of the users in JSON format in the URLs `/user/alice/` and `/user/bob/`.

- Django:`views.py`:

        from django.http import JsonResponse

        def get_user(request, username):
            users = {
                'alice': {'name': 'Alice', 'age': 30},
                'bob': {'name': 'Bob', 'age': 25}
            }
            user = users.get(username, 'User not found')
            return JsonResponse(user, safe=False)

    `urls.py`:

        from django.urls import path
        from . import views

        urlpatterns = [path('user/<str:username>/', views.get_user, name='get_user'),]

    This code gives the same output as the Flask's.

Outputs:

![alice][6]

![bob][7]

# Authentication and Authorization in Web APIs
Authentication and authorization are essential to secure applications, especially when it comes to building APIs that expose sensitive data or perform critical actions.

**Implementing Authentication for API Endpoints** Authentication verifies the identity of a user or entity accessing an application or service. There are several methods for implementing authentication for API endpoints:

- **Token-based Authentication**: In this method, clients are issued unique tokens upon successful login. Subsequent requests made later, use these tokens to authenticate the user.
- **JSON Web Tokens (JWT)**: JWT is URL-safe method of encoding information that will be exchanged between two parties, such as client and server.

Let's take a look at an example of implementing token-based authentication using Flask:

    from flask import Flask, request, jsonify
    from flask_jwt_extended import JWTManager, create_access_token, 
    get_jwt_identity, jwt_required

    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] ='supersecret'
    jwt = JWTManager(app)

    users = {'user': 'pswrd'}

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if username in users and users[username] == password:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
       else:
            return jsonify({'error': 'Invalid username or password'}), 401

    @app.route('/protected', methods=['GET'])
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200

    app.run(debug=True)

Here, the `/login` endpoint verifies the user's credentials and generates a JWT access token upon successful authentication. The `/protected` endpoint requires a valid JWT token for access, enforced by the `@jwt_required()` decorator.

Output:

![login][8]

![protected][9]

# Serializers and Deserializers
Serialization is the conversion of a complex data structure, like Python object, into a format that can be transmitted or stored in a file easily, like JSON (JavaScript Object Notation), XML (eXtensible Markup Language) or YAML.

Deserialization is the reconversion of the serialized data to its original data structure. This is important to process incoming client requests.

DRF serializers in Django have built-in validation capabilities and Marshmallow in Flask provides support for validation through its `Schema` class.

Let's look at the codes:

In Django, the serialization will be done in `serializers.py` file in your app's folder:

    from rest_framework import serializers
    from .models import Product

    class ProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ['id', 'name', 'description']

Define your model in `models.py`:

    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()

        def __str__(self):
            return self.name

`views.py`:

    from django.shortcuts import render
    from rest_framework.response import Response
    from rest_framework.decorators import api_view
    from .models import Product
    from .serializers import ProductSerializer

    @api_view(['GET'])
    def product_list(request):
        if request.method == 'GET':
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

This code serializes and deserializes the data.

Output:

![ser_des_django][10]

<div class="div-red"> <span class="alert-header">Caution:</span> Make sure to install the `djangorestframework` module and include `rest_framework` in the `INSTALLED_APPS` section in `settings.py`. </div>

The same can be done in Flask using Flask-RESTful and Marshmallow:

    from flask import Flask, jsonify, request
    from marshmallow import Schema, fields, ValidationError

    app = Flask(__name__)
    products = [
        {
            "name": "Laptop",
            "description": "High-performance laptop with SSD storage",
            "price": 1200.00
        },
        {
            "name": "Smartphone",
            "description": "Latest model with dual-camera setup",
            "price": 800.00
        }
    ]    # sample data

    class ProductSchema(Schema):
        name = fields.Str(required=True)
        description = fields.Str(required=True)
        price = fields.Float(required=True)

    @app.route('/api', methods=['GET'])
    def get_products():
        return jsonify(products), 200

        app.run(debug=True)

This code performs serialization and deserialization and displays the data in `/api`.

Output:

![ser_des_flask][11]

# CRUD Operations with Flask/Django ORM
CRUD operations allow you to manipulate data stored in your database. Here's what each operation does:

- **Create**: Adds new records to the database.
- **Read**: Retrieves records from the database.
- **Update**: Modifies records in the database.
- **Delete**: Removes records from the database.

**Flask ORM** The SQLAlchemy ORM in Flask allows you to interact with data in databases.

- **Create** To enter a new record in your database, you can define a model class and use the `session.add()` method and then `session.commit()`.

- **Read** To retrieve records from your database, you can use `query.all()` to retrieve all or `query.filter()` to retrieve based on a condition.

- **Update** To update records, you need to fetch, modify and commit changes in a record.

- **Delete** To delete records, you can use the `session.delete()` method and then `session.commit()`.

This example code demonstrates CRUD operations in Flask. Note that a simple HTML script named `product.html` has been used:

    from flask import Flask, request, render_template, redirect, url_for
    from flask_sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'    # database
    db = SQLAlchemy(app)

    class Product(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        description = db.Column(db.Text, nullable=True)
        price = db.Column(db.Float, nullable=False)

    @app.route('/', methods=['GET', 'POST'])
    def product_list():
        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            price = float(request.form['price'])
            new_product = Product(name=name, description=description, price=price)
            db.session.add(new_product)    # create
            db.session.commit()
            return redirect(url_for('product_list')) 
        products = Product.query.all()    # retrieve
        return render_template('product.html', products=products)

    @app.route('/update/<int:id>', methods=['GET', 'POST'])
    def update_product(id):    # update
        product = Product.query.get_or_404(id)
        if request.method == 'POST':
            product.name = request.form['name']
            product.description = request.form['description']
            product.price = float(request.form['price'])
            db.session.commit()
            return redirect(url_for('product_list'))
        return render_template('product.html', product=product)

    @app.route('/delete/<int:id>', methods=['POST'])
    def delete_product(id):    # delete
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return redirect(url_for('product_list'))

    with app.app_context():
        db.create_all()
    app.run(debug=True)

Upon execution, a page containing existing records and a form to create a new entry will appear. Options to update and delete will be provided along each entry.

Output:

![crud1_flask][12]

![crud2_flask][13]

**Django ORM** Django consists of built-in ORM, which allows interaction with databases.

- **Create** To enter a new record, create a new instance of the model and call the `save()` method.

- **Read** You can use queryset methods such as `all()`, `get()`, or `filter()` to retrieve records.

- **Update Operation** To update records, you need to fetch, modify and save changes to the record using the `save()` method.

- **Delete Operation** To delete, you have to fetch the record and call the `delete()` method.

Let's observe CRUD operations using the following example:

`views.py`:

    from django.shortcuts import render, redirect, get_object_or_404
    from .models import Product
    from .forms import ProductForm

    def product_list(request):    # create and retrieve
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('product_list')
    else:
        form = ProductForm()
        products = Product.objects.all()
        return render(request, 'product.html', {'products': products, 'form': form})

    def update_product(request, id):    # update
        product = get_object_or_404(Product, id=id)
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('product_list')
        else:
           form = ProductForm(instance=product)
        return render(request, 'product.html', {'form': form})

    def delete_product(request, id):    # delete
        product = get_object_or_404(Product, id=id)
        if request.method == 'POST':
            product.delete()
            return redirect('product_list')
        return render(request, 'product.html', {'product': product})

`models.py`:

from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField(blank=True)
        price = models.DecimalField(max_digits=10, decimal_places=2)

        def __str__(self):
            return self.name

`urls.py`:

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.product_list, name='product_list'),
        path('update/<int:id>/', views.update_product, name='update_product'),
        path('delete/<int:id>/', views.delete_product, name='delete_product'),
    ]

This code performs the exact same operations as the Flask code.

Output:

![crud1_dj][14]

![crud2_dj][15]

# Conclusion
In this article, we have explored various functionalities that **Flask** and **Django** frameworks offer to create useful RESTful APIs. Features such as **authentication**, **authorization**, **serialization** and **CRUD** operations using ORMs allow us to use the two frameworks to create extremely efficient APIs that are platform independent. We highly encourage you to explore the documentations provided throughout the article to deepen your knowledge about the features and leverage them to the fullest.

  [1]: https://flask.palletsprojects.com/
  [2]: https://docs.djangoproject.com/en/stable/
  [3]: https://logiclair.org/?qa=blob&qa_blobid=16266377445707127220
  [4]: https://logiclair.org/?qa=blob&qa_blobid=9346400292446090253
  [5]: https://logiclair.org/?qa=blob&qa_blobid=3216341660688294463
  [6]: https://logiclair.org/?qa=blob&qa_blobid=7374402418012406775
  [7]: https://logiclair.org/?qa=blob&qa_blobid=17879022255200297375
  [8]: https://logiclair.org/?qa=blob&qa_blobid=4305567721446402514
  [9]: https://logiclair.org/?qa=blob&qa_blobid=8795568490372538295
  [10]: https://logiclair.org/?qa=blob&qa_blobid=17810318594583621902
  [11]: https://logiclair.org/?qa=blob&qa_blobid=16260165105177898932
  [12]: https://logiclair.org/?qa=blob&qa_blobid=4942925935466504
  [13]: https://logiclair.org/?qa=blob&qa_blobid=16467716695236336539
  [14]: https://logiclair.org/?qa=blob&qa_blobid=10122563557020819117
  [15]: https://logiclair.org/?qa=blob&qa_blobid=3859524776406481273
