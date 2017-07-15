from flask import Flask # imports the Flask class: our WSGI (web server gateway interface)
from flask import render_template
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

@app.route("/saymynamepost/<name>", methods=['POST'])
def saymynamepost(name):
    return "POSTed %s" % name

@app.route('/double/<post_id>')
def double(post_id):
    # show the post with the given id, the id is an integer
    post_id = int(post_id) * 2
    return '%d' % post_id

@app.route('/hellotemplate/<name>')
def hellotemplate(name=None):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run()