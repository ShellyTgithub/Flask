from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_from_flask():
    return "<h1>Hello from Eoghan using Flask!<h1>"

if __name__ == "__main__":
    app.run(debug=True)
