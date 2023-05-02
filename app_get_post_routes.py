from flask import Flask, request, Response

app = Flask(__name__)
# Section 1 above is used for importing Libraries that we will need.
# We set up the 'app' as a Flask Application

# Section 2 - we tell our webserver that when the url / is accessed in the browser,
# it should return the contents of the hello_from_flask() function
@app.route("/")
def hello_from_flask():
    return "Hello from Eoghan using Flask!"

# Extra 'routes' here -
@app.route("/get/text")  #   <<====== WEb address in the browser bar
def get_text():              #   <<== function to execute
    return Response("Hello from Flask using an explicit response object.", mimetype='text/plain')

@app.route("/post/text", methods=['POST'])
def post_text():
    #data_sent = request.data.decode('utf-8')
    #app.logger.info(data_sent)
    value = str(request.args.get('eoghan'))
    app.logger.info(value)
    return Response("You posted this data to the Flask app:" + value, mimetype='text/plain')

# Section 3- Now let's run it!
if __name__ == "__main__":
    app.run(debug=True)