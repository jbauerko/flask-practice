from flask import Flask, render_template, url_for

# Creating an instance of the flask class, which represents the webapp
app = Flask(__name__) 
# Name is a special built in variable that indicates the name of the module in which it is used

@app.route('/') # Route decorator - maps a url to a python function
def index(): # Root url handler
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True) 