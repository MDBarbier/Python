from flask import Flask # imports the Flask class: our WSGI (web server gateway interface)
app = Flask(__name__)  # instance of the class - use __name__ if only one module

@app.route("/") # "/" default route
def root():
    return "I am root"

@app.route("/goodbye")
def goodbye():
    return "Goodbye, World!"

@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/saymyname/<name>")
def saymyname(name):
    return "Hello %s" % name

@app.route('/double/<post_id>')
def double(post_id):
    # show the post with the given id, the id is an integer
    post_id = int(post_id) * 2
    return '%d' % post_id

if __name__ == "__main__":
    app.run()