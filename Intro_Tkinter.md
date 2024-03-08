# Introduction to Tkinter

Embarking on the journey of **Graphical User Interface (GUI)** development in **Python** opens up a realm of possibilities, with **Tkinter** emerging as a stalwart companion. Whether you're a novice programmer venturing into the world of GUIs or a seasoned developer seeking simplicity and efficiency, Tkinter stands as a reliable toolkit. In this comprehensive article, we'll unravel the intricacies of Tkinter, explore its fundamental **widgets**, discuss its advantages and disadvantages, and equip you with the knowledge to excel in Python GUI development.

### Understanding Tkinter

Tkinter, short for **Tk interface**, is a built-in Python library designed for creating interactive GUI applications. Based on the Tk GUI toolkit, Tkinter simplifies the creation of windows, buttons, menus, and various graphical elements. As an integral part of the Python standard library, Tkinter seamlessly integrates with Python projects without the need of installing anything extra, offering a seamless and robust GUI development experience.

### Exploring Basic Widgets

Let's start by looking at some basic things you can create with Tkinter.

- **Label**: Displays text or an image. It is a static element and doesn't allow user interaction.
- **Button**: A clickable element that performs an action when pressed, such as submitting a form or triggering a function.
- **Entry**: A text field where users can input text or numbers. It is often used for data entry or search functionality.
- **Checkbutton**: A checkbox that allows users to select or deselect an option.
- **Radiobutton**: A set of mutually exclusive buttons, allowing users to choose only one option from multiple choices.
- **Listbox**: A widget that displays a list of items from which users can select one or more options. It's often used for selecting items from a list or displaying results.
- **Scrollbar**: Allows users to scroll through content that exceeds the visible area of a widget, such as a text box or list.
- **Frame**: A container used to group and organize other widgets. It is often used for layout purposes to create sections or divisions within a window.
- **Canvas**: Provides a drawing area for creating graphics, shapes, and custom elements. It is used for creating diagrams, charts, and interactive visualizations.
- **Menu**: Creates a menu bar or dropdown menu with options and commands. It is often used for adding navigation, settings, and other functionality to the application's interface.

These widgets form the core building blocks of Tkinter GUI applications and are commonly used in various projects to create user-friendly interfaces.

### Basic Functionalities

Let's dive into some code examples to see these concepts in action.

```sh
import tkinter as tk
window = tk.Tk()
window.title("Welcome to Tkinter")
window.geometry("900x700")
label = tk.Label(window, text="Hello World!")
label.pack()
window.mainloop()
```

![sample_window_output](https://github.com/Parinitha-Samaga/Article_img/blob/main/Tkinter_1.png)

Markdown is a lightweight markup language based on the formatting conventions
that people naturally use in email.
As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Tech

Dillinger uses a number of open source projects to work properly:

- [AngularJS] - HTML enhanced for web apps!
- [Ace Editor] - awesome web-based text editor
- [markdown-it] - Markdown parser done right. Fast and easy to extend.
- [Twitter Bootstrap] - great UI boilerplate for modern web apps
- [node.js] - evented I/O for the backend
- [Express] - fast node.js network app framework [@tjholowaychuk]
- [Gulp] - the streaming build system
- [Breakdance](https://breakdance.github.io/breakdance/) - HTML
to Markdown converter
- [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## Installation

Dillinger requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```

## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

## Docker

Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd dillinger
docker build -t <youruser>/dillinger:${package.json.version} .
```

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
