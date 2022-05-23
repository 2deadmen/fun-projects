from flask import Flask, render_template
import requests


app=Flask(__name__)


response = requests.get(url="https://api.npoint.io/65a73dd190e802438010")
Text = response.json()[0]
Text1 = response.json()[1]
Text2 = response.json()[2]
@app.route('/')
def home():
       
    return render_template("index.html",text=Text,text1=Text1,text2=Text2)
list=[]

list.append(Text)
list.append(Text1)
list.append(Text2)
@app.route('/post/<index>')
def post(index):
    for i in list:
        if i['id'] == int(index):
            Text =i          
    return render_template("post.html",text=Text)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)
