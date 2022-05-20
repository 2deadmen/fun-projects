from ctypes.wintypes import POINT
import imp
from flask import Flask, render_template
from post import Post

app = Flask(__name__)
ost=Post()
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/post')
def post():
    return render_template("post.html",title=ost.title,body=ost.body)


if __name__ == "__main__":
    app.run(debug=True)
