import flask
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
    

def to_dict(allcafe):
  cafes=[]
  for random_cafe in allcafe:
    cafe={
        "id":random_cafe.id,
        "name":random_cafe.name,
        "map_url":random_cafe.map_url,
        "img_url":random_cafe.img_url,
        "location":random_cafe.location,
        "has_sockets":random_cafe.has_sockets,
        "has_toilet":random_cafe.has_toilet,
        "has_wifi":random_cafe.has_wifi,
        "seats":random_cafe.seats,
        "coffee_price":random_cafe.coffee_price
    }
    cafes.append(cafe)
  return cafes

@app.route('/all')
def all():

    allcafe = db.session.query(Cafe).all()

    cafes=to_dict(allcafe)
    return flask.jsonify(cafes)
@app.route('/search')
def search():
    loc=request.args.get('loc')
    allcafe=Cafe.query.filter_by(location=loc)
    cafes = to_dict(allcafe)
    if cafes!=[]:


        return flask.jsonify(cafes)
    elif cafes==[]:
        return flask.jsonify(error={'not found':'sorry'})
@app.route('/add',methods=['POST'])
def add():
    if request.method=='POST':
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
@app.route('/update/<id>')
def update(id):
    cafe=Cafe.query.get(id)
    if cafe:

        cafe.coffee_price=request.form.get("new_price")
        db.session.commit()
        return flask.jsonify(response={"success": "Successfully added the new cafe."})
    else:
      return flask.jsonify(error={"not found": "no cafe was found"}),404

@app.route('/delete/<id>',methods=['DELETE'])
def delete(id):
    cafe=Cafe.query.get(id)
    if request.args.get('api_key')=="Topsecret":
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return flask.jsonify(response={"success": "Successfully deleted the cafe."})
        else:
            return flask.jsonify(error={"not found": "no cafe was found"}), 404
    else:
        return flask.jsonify(error={"sorry":"wrong api key"}),403
## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
