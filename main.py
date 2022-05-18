import random
from flask import Flask
app = Flask(__name__)

def red_decorator(function):
    def wrapper():
        return '<h1><em style="color:blue;"><b>'+function()+'</h1></b></em>'

    return wrapper

value=random.randint(0,10)

@app.route('/')
@red_decorator
def start():
    return '<h1>guess the number</h1>'\
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<n>')
def check(n):
    if int(n)>10:
        return '<h1>invlaid input</h1>' \
               '<img src="https://media.giphy.com/media/3ogwFHwmO7M90MvPos/giphy.gif">'
    if int(n)>value:
        return '<h1>too high</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif int(n)<value:
        return  '<h1>too low</h1>' \
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif int(n)==value:
        return '<h1>you got me</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'




if __name__=="__main__":
    app.run(debug=True)