from flask import Flask

# set FLASK_APP=hello.py
# flask --app hello run



app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()