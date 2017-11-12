from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template,redirect,url_for,request

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password@localhost/entry'
db  = SQLAlchemy(app)
  
class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    rent = db.Column(db.Integer)

    def __init__(self, name, rent):
        self.name = name
        self.rent = rent

    def __repr__(self):
        return '<id {}>'.format(self.id)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/seeds")
def market_rate():
    return render_template("seeds.html")

@app.route("/hardware")
def hardware():
    return render_template("hardware.html")


@app.route("/transport")
def transport():
	posts = Vehicle.query.all()
	return render_template("transport_all.html",posts=posts)



@app.route("/fertiliser")
def fertiliser():
    return render_template("fertiliser.html")

@app.route("/add_vehicle", methods=["GET", "POST"])
def vehicle():
	    if request.method == "GET":
	    	return render_template("new_vehicle.html")
	    else:
			name = request.form["name"]
			rent = request.form["rent"]

			note = Vehicle(name= name, rent= rent)
        
			db.session.add(note)
			db.session.commit()


			return redirect(url_for('transport'))

@app.route("/edit_vehicle", methods=["GET","POST"])
def edit_vehicle():




if __name__ == "__main__":
	app.run(debug=True)