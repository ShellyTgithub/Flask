from flask import Flask

app = Flask(__name__)
# Section 1 above is used for importing Libraries that we will need.
# We set up the 'app' as a Flask Application

# Section 2: APPLICATION ROUTES (WEB PAGE DEFINITIONS)

@app.route("/")
def home():
    """ Returns a very simple index page.
    """
    return "<h1>Hello, is it you I'm looking for?</h1>"

@app.route("/dynamic/<word>")
def dynamic_example1(word=None):
    """ Route to display a word from the url.
        Equivalent to /dynamic/<string:word>
    """
    app.logger.info(f"In dynamic function. About to display <word>: {word}")
    return word

@app.route("/square/<int:number>")
def square(number):
    """ Route to process a url int parameter inside html!
    """
    squared = number ** 2
    return f"URL Parameter: {str(number)} -> {str(squared)}"

@app.route("/html/<name>")
def say_hello_page(name):
    return f"""
    <html>
    <head>
        <title>Sample - Flask Routes</title>
    </head>
    <body>
    <h1>Name Page</h1>
    <p>Hello {name}</p>
    </body>
    </html>
    """


# Section 4: Run!
if __name__ == "__main__":
    app.run()
