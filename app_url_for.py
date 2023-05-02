from flask import Flask, url_for

app = Flask(__name__)
# Section 1 above is used for importing Libraries that we will need.
# We set up the 'app' as a Flask Application

# Section 2: APPLICATION ROUTES (WEB PAGE DEFINITIONS)

@app.route("/")
def home_page():
    url1 = url_for('a_different_page')
    return f"""
    <html>
    <head>
        <title>Sample - Flask Routes Home</title>
    </head>
    <body>
    <h1>Another Page</h1>
    <p>Hello again!</p>
    <hr>
    <a href="{url1}">Different Page Link</a>
    </body>
    </html>
    """

@app.route("/index/<name>/<int:age>")
def index(name, age):
    """ Returns a more complex index page.
    """
    url = url_for('a_different_page')
    return f"""
    <html>
    <head>
        <title>Sample - Adv Flask Routes</title>
    </head>
    <body>
    <h1>Name Page</h1>
    <p>Hello {name}</p>
    <p>You are {age} years old!</p>
    <hr>
    <a href="{url}">Page 2</a>
    </body>
    </html>
    """

@app.route("/different")
def a_different_page():
    url1 = url_for('home_page')
    return f"""
    <html>
    <head>
        <title>Sample - Flask Routes</title>
    </head>
    <body>
    <h1>Another Page</h1>
    <p>Hello again/p>
    <p><a href="{url1}">Homepage</a>
    </body>
    </html>
    """

# Section 4: Run!
if __name__ == "__main__":
    app.run(debug=True)