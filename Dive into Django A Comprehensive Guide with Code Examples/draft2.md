
**Django** is a high-level **Python web framework** that is used for building web applications efficiently and with ease. It is known for its **scalability**, **security**, and **versatility**, and has a built-in **admin interface**, and **authentication system**. In this article, we will explore Django **models**, **views** and **templates**, along with an introduction to **Django Rest Framework**.

# Getting Started with Django

1. Open your terminal or command prompt and type the following command to install Django:

		pip install django

	<div class="div-blue"> <span class="alert-header">Note:</span> <span class="alert-body"> You can verify that Django is installed by running: `django-admin --version`.</span> </div>

2. To start a new Django project, navigate to the directory where you wish to build your project and run:

		django-admin startproject myproject

	<div class="div-red"> <span class="alert-header">Caution:</span> Replace `myproject` with the name of your project. </div>

	This creates a new directory named `myproject` containing the basic files and folders for your Django project.

3. Open the `views.py` file inside the `myproject` directory and add the following code:

		from django.http import HttpResponse

		def hello_world(request):
		    return HttpResponse("Hello, World!")

4. To map this view to a URL, open the `urls.py` file in the `myproject` directory and add the following code:

		from django.urls import path
		from . import views

		urlpatterns = [path('hello/', views.hello_world, name='hello_world'),]

5. To run the development server, navigate to your project directory and type the following command in the terminal:

		python manage.py runserver

	This command will start the development server on your local machine. You can access your Django project by opening `http://127.0.0.1:8000/hello/` in your web browser, which displays "Hello, World!" on the page.

Output:

![Command Prompt][1]

![hello_world][2]


# Django Models

**Django models** are Python classes used to represent database tables. The **Django Object-Relational Mapping (ORM)** translates these classes into database schema and provides an API for interacting with the database.

1. To define a model, Django provides many field types such as CharField, IntegerField, DateTimeField, and ForeignKey, each denoting a field in the database table. In `models.py` file, create a Python class that inherits from `django.db.models.Model`, and define the structure of the database.

		from django.db import models

		class Bill(models.Model):
		    UHID = models.IntegerField()
		    date = models.DateField()
		    PatientName = models.CharField(max_length=100)
		    doctorName = models.CharField(max_length=100)
		    remark = models.CharField(max_length=100)

	This code creates 5 fields:
	- `UHID` field stores integer values.
	- `date` field store dates.
	- `PatientName`, `doctorName` and `remark` fields store a maximum of 100 characters.

2. Django models support the Create, Read, Update, and Delete (CRUD) operations. `save()` method is used to Create and Update, `delete()` method to Delete, and querying methods for Read operations.

		bill = Bill.objects.create(UHID=1, date=date(2024, 3, 2), PatientName='xyz', doctorName='ABC', remark='Lorem Epsom')      # Create
		bills = Bill.objects.all()     # Read
		bill.PatientName = 'XYZ'
		bill.save()       # Update
		bill.delete()      # Delete

3. **Querysets** allow efficient database retrieval operations by supporting various methods for filtering, ordering, aggregating, and annotating data.

		bills = Bill.objects.filter(UHID=1)     # Filtering
		bills = Bill.objects.order_by('-UHID')     # Ordering
		latest_bill_date = Bill.objects.aggregate(latest_date=Max('date'))['latest_date']     # Aggregating

Output:

![Django Models][3]


I encourage you to refer the [Django ORM Cookbook][4] for more information on querying.


# Django Views and URLs

**Views** are Python classes that receive web requests and return web responses. They handle user interactions and generate dynamic content to be displayed to the user.

**URLs** define the mapping between a URL pattern and the corresponding view that handles a request. By defining URLs, you establish the structure and navigation of your web application.

**Mapping URLs to Views**
You can map URLs to views using the `urls.py` module in your Django app. This file contains a list of URL patterns defined using the `urlpatterns` variable. Each URL pattern is mapped to a specific view defined in `views.py`.

**Class-based Views vs Function-based Views**
Django supports **class-based views** and **function-based views**. Following is a comparison between class-based and function-based views:

- **Class-based Views**: 
  - Encapsulate view logic within classes.
  - Support inheritance and mixins for code reuse.
  - Provide built-in methods for handling HTTP requests (e.g., `get`, `post`).

- **Function-based Views**:
  - Define view logic as standalone functions.
  - Directly map HTTP methods to view functions.

Let's take a look at a few examples to understand Views and URLs better:

- Function-based View:

	`views.py`:
	
		from django.http import HttpResponse

		def my_view(request):
		    return HttpResponse("Hello, world!")

	`urls.py`:

		from django.urls import path
		from .views import my_view
		
		urlpatterns = [path('hello/', my_view, name='my_view'),]

	This code maps the function `my_view` to the URL `hello/` directly,

Output:

![myview][2]


- Class-based View:

	`views.py`:
	
		from django.views import View
		from django.http import HttpResponse
		from django.shortcuts import render

		class MyView(View):
		    def get(self, request):
		        return HttpResponse("Hello, world!")
		     
		class PassDataView(View):
		    def get(self, request):
		        data = {'name': 'John', 'age': 30}
		        response = f"""
		        Welcome to My Template<br>
		        Name: {data['name']}<br>
		        Age: {data['age']}
		        """
		        return HttpResponse(response)

	`urls.py`:

		from django.urls import path
		from .views import MyView, PassDataView

		urlpatterns = [ 
			path('hello/', MyView.as_view(), name='my_view'), 
		  path('pass_data/', PassDataView.as_view(), name='pass_data'),
		]

	Here, the two classes, `MyView` and `PassDataView`, each are mapped to the URLs `hello/` and `pass_data/` respectively.

Output:

![MyView][2]

![pass_data][5]


# Django Templates

Django's template system is a tool used to build dynamic web pages by combining HTML with Django template language (DTL) syntax. It allows you to create reusable components and generate HTML dynamically based on data from the server easily.

**Creating and Rendering Templates**
Create a file with a `.html` extension within the `templates` directory of your Django app. In the example, I named the app `dispapp`, and the HTML templates are stored in `dispapp/templates`. Template tags and filters can be used to insert dynamic data, loop through data, and perform logic within this template.
To render a template, use the `render` shortcut function and pass the template name and context data as arguments in the `views.py` file.

**Template Inheritance and Extending Base Templates**
In Django, you can create a base template with common elements such as headers, footers, etc., and then inherit it in other templates to override specific blocks.

Let's take a look at an example:

`templates/base.html`:

	<!DOCTYPE html>
	<html>
	<head>
	    <title>{% block title %}Sample Site{% endblock %}</title>
	</head>
	<body>
	    <div>
	        <h1>Template Inheritance Demo</h1>
	        {% block content %}
	        <!-- Content from your child template will be inserted here -->
	        {% endblock %}
	    </div>
	</body>
	</html>

`templates/child.html`:

	{% extends "base.html" %}

	{% block title %}Child Page{% endblock %}

	{% block content %}
	    <p>This is the child template.</p>
	    <p>Name: {{ name }}</p>
	    <p>Age: {{ age }}</p>
	{% endblock %}

Context data from views can be passed to templates using dictionaries. This enables you to dynamically enter data from the server into templates.

For `views.py`, use the class-based view from the last topic, but replace the `PassDataView` class as follows:

	class PassDataView(View):
	    def get(self, request):
	        context = {'name': 'Bethany', 'age': 37}
	        return render(request, 'child.html', context)

Make sure `views.py` is located in the same directory as `templates` directory.

`dispapp/urls.py`:

Same as `views.py` from the class-based view's example.

`myproject/views.py`:

	from django.contrib import admin
	from django.urls import path, include

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('', include('dispapp.urls')),
	]

This code is needed to register and reroute the app into the `dispapp.urls` module.

<div class="div-red"> <span class="alert-header">Caution:</span> Make sure your app's name (`dispapp`) is included in the `INSTALLED_APPS` section in `settings.py`.</div>

Output:

![templates][6]

Visit the [Django documentation on templates][7] for more information.


# Django Forms

Django simplifies the process of creating HTML forms using its form handling mechanism. Using Django's built-in form classes and template tags, you can efficiently generate forms with minimal boilerplate code.

Django also allows built-in **form validation** and **error handling** using a range of validators that can be applied to form fields, ensuring data integrity and security.

Let's take an example as follows:

`create_product.html`:

	<!DOCTYPE html>
	<html>
	<head>
	    <title>Create Product</title>
	</head>
	<body>
	    <h2>Create a new product</h2>
	    <form method="post">
	        {% csrf_token %}
	        {{ form.as_p }}
	        <button type="submit">Save</button>
	    </form>
	</body>
	</html>

`product_list.html`:

	<!DOCTYPE html>
	<html>
	<head>
	    <title>Product List</title>
	</head>
	<body>
	    <h2>Product List</h2>
	    <ul>
	        {% for product in products %}
	            <li>{{ product.name }} - {{ product.price }}</li>
	        {% endfor %}
	    </ul>
	</body>
	</html>

`views.py`:

	from django.shortcuts import render, redirect
	from .models import Product
	from .forms import ProductForm

	def create_product(request):
	    if request.method == 'POST':
	        form = ProductForm(request.POST)
	        if form.is_valid():
	            form.save()
	            return redirect('product_list')
	    else:
	        form = ProductForm()
	    return render(request, 'create_product.html', {'form': form})

	def product_list(request):
	    products = Product.objects.all()
	    return render(request, 'product_list.html', {'products': products})

It provides 2 views: `create_product` which allows you to enter the details of a product; `product_list` which displays the list of the entered product.

`urls.py`:

	from django.urls import path
	from . import views

	urlpatterns = [
	    path('create/', views.create_product, name='create_product'),
	    path('list/', views.product_list, name='product_list'),
	]

**Using Django Forms with Models**
Django's form system also integrates with models, allowing you to create forms directly from model definitions, enabling you to perform CRUD operations on your database easily.

`models.py`:

	from django.db import models

	class Product(models.Model):
	    name = models.CharField(max_length=100)
	    description = models.TextField()
	    price = models.DecimalField(max_digits=10, decimal_places=2)
	    created_at = models.DateTimeField(auto_now_add=True)

	    def __str__(self):
	        return self.name

This creates a database with 4 columns as given.

`forms.py`:

	from django import forms
	from .models import Product

	class ProductForm(forms.ModelForm):
	    class Meta:
	        model = Product
	        fields = ['name', 'description', 'price']

It displays a form containing columns `name`, `description` and `price` of the new product and then redirects to the page displaying entered products later.

Outputs:

![create_prod][8]

![disp_list][9]


# Django Admin

The **Django admin interface** provides a user-friendly interface to perform CRUD operations on your data. The interface is built using Django's ORM, which provides an effective way to perform administrative tasks.

1. You need to **register** your models with the admin site to access them in the interface. For this, you have to create a `admin.py` file in your app directory and import your models into it. Then, use the `admin.site.register()`or the`@admin.register()` method to register your models.
2. The Django admin interface allows you to tweak the interface to your project's needs. You can customize the admin interface's appearance, behavior, functionality, etc. Some common customizations include:

	- **Adding custom actions**: You can perform bulk operations on selected objects in the admin interface using custom actions. This can involve exporting data or sending emails.
	- **Customizing list views**: You can customize the list views to display additional fields, filters, etc.
	- **Inlines**: You can edit related objects directly within the parent model's admin page using inline models.
	- **ModelAdmin options**: ModelAdmin options such as `list_display`, `list_filter`, and `search_fields` can help you customize the behavior of your models in the interface.
3. Create a superuser to gain access to the interface. Run this command in the terminal and enter a username, email and password when prompted:

		python manage.py createsuperuser

To understand this concept, let's add the `admin.py` file to the example we looked at while learning Forms.

`dispapp/admin.py`:

	from django.contrib import admin
	from .models import Product

	@admin.register(Product)
	class ProductAdmin(admin.ModelAdmin):
	    list_display = ('name', 'price', 'created_at')
	    list_filter = ('created_at',)
	    search_fields = ('name', 'description')

This code allows you to access the admin interface when you go to `http://127.0.0.1:8000/admin/` and enter the username and password. You can then enter more or view existing products in the `Products` table and also view users and groups that have access to the interface.

Output:

![dashboard][10]

![options][11]

![Products][12]

![Users][13]


# Django Authentication and Authorization

Django's `auth` module provides readily available components for handling user authentication tasks like user registration, login, logout, and password management.

**User Registration and Login Views**
To allow users to register and log in to your application, you'll need to create views for user registration and login. These views handle user input, validate credentials, and manage user sessions.
The User Registration View allows users to create a new account, validates the users' inputs, and redirects the users to the login page after successful registration.
The User Login View authenticates the users' credentials, creates a user session after login, and then redirects the users to the required page.

**Restricting Access to Views Based on User Authentication**
You can also restrict access to certain views or functionalities based on whether a user is authenticated or not. Decorators such as `login_required` can be used to enforce authentication requirements on views.

As an example, we shall be adding the following codes to the example we used while learning Admin:

`templates/register.html`:

	<!DOCTYPE html>
	<html>
	<head>
	    <title>User Registration</title>
	</head>
	<body>
	    <h2>Register</h2>
	    <form method="post">
	        {% csrf_token %}
	        {{ form.as_p }}
	        <button type="submit">Register</button>
	    </form>
	</body>
	</html>

This displays the registration form.

`templates/login.html`:

	<!DOCTYPE html>
	<html>
	<head>
	    <title>User Login</title>
	</head>
	<body>
	    <h2>Login</h2>
	    <form method="post">
	        {% csrf_token %}
	        {{ form.as_p }}
	        <button type="submit">Login</button>
	    </form>
	</body>
	</html>

This displays the login form.

`forms.py` (add):

	from django.contrib.auth.forms import UserCreationForm
	from django.contrib.auth.models import User
	class UserRegistrationForm(UserCreationForm):
	    email = forms.EmailField()
	    class Meta:
	        model = User
	        fields = ['username', 'email', 'password1', 'password2']

It uses the `auth` module to handle registration.

`views.py` (add):

	from django.contrib.auth.forms import UserCreationForm
	from .forms import UserRegistrationForm
	def register(request):
	    if request.method == 'POST':
	        form = UserRegistrationForm(request.POST)
	        if form.is_valid():
	            form.save()
	            return redirect('login')
	    else:
	        form = UserRegistrationForm()
	    return render(request, 'register.html', {'form': form})

It uses the `auth` module to handle registration and login. After registration, you will be redirected to the login page.

`dispapp/urls.py` (modify urlpatterns):

	urlpatterns = [
	    path('create/', views.create_product, name='create_product'),
	    path('list/', views.product_list, name='product_list'),
	    path('register/', views.register, name='register'),
	    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	]

`settings.py` (add):

	LOGIN_REDIRECT_URL = '/list/'

After you log in, you will be redirected to the page containing the list of entered products.

Output:

![register][14]

![login][15]



# Django Rest Framework (DRF)

The Django Rest Framework (DRF) is an intuitive toolkit that allows you to create **RESTful APIs** using Django. Using tools like serializers, views, etc., scalable and flexible APIs can be built.

**Serializers and Views in DRF**
Serializers convert complex data types, such as queryset and model instances, into native Python datatypes. These can then be easily rendered into JSON, XML, or other formats.
Views in DRF are similar to Django views but additionally provide built-in support to handle HTTP methods such as GET, POST, PUT, DELETE, etc., and allow easy creation of API endpoints.

![Get Request][16]

**Authentication and Permissions in DRF**
Authentication and permissions mechanisms provided by DRF can be used to secure your API endpoints. Tokens, session authentication, OAuth, or custom authentication schemes can be employed for authentication.  Access to resources can be controlled using permissions based on user roles and permissions defined in your application.

Let's take a look at an example to understand the concepts better:

`serializers.py`:

	from rest_framework import serializers
	from .models import MyModel

	class MyModelSerializer(serializers.ModelSerializer):
	    class Meta:
	        model = MyModel
	        fields = '__all__'

`views.py`:

	from rest_framework import generics
	from .models import MyModel
	from .serializers import MyModelSerializer

	class MyModelListView(generics.ListCreateAPIView):
	    queryset = MyModel.objects.all()
	    serializer_class = MyModelSerializer

`urls.py`:

	from django.urls import path
	from .views import MyModelListView

	urlpatterns = [
	    path('mymodel/', MyModelListView.as_view(), name='mymodel-list'),
	]

![API Calls][17]


# Conclusion
**Django** is a powerful, yet flexible, Python framework used for building web applications. It provides **models** to interact with databases, **views** for handling requests, **URLs** for routing and **forms** to handle user input. Django also provides simple and efficient authorization and authentication mechanisms using the `auth` module. **DRF** is a versatile toolkit that allows you to build robust RESTful APIs for your web applications. I highly encourage you to take a look at the [official Django documentation][14] to explore more about this topic in detail.



[1]: command_prompt.png
[2]: hello_wrld.png
[3]: django_model.png
[4]: https://books.agiliq.com/projects/django-orm-cookbook/en/latest/
[5]: pass_data.png
[6]: templates.png
[7]: https://docs.djangoproject.com/en/3.2/topics/templates/
[8]: create_prod.png
[9]: disp_list.png
[10]: dashboard.png
[11]: options.png
[12]: products.png
[13]: users.png
[14]: register.png
[15]: login.png
[16]: get_request.png
[17]: API_call.png
[18]: https://docs.djangoproject.com/en/5.0/
