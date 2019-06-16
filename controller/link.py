
from flask import Flask, render_template, request, url_for, redirect

from flaskext.cache.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///db.sqllite'

db = SQLAlchemy(app)

class Link(db.Model):
    
    __tablename__ = 'link'
    
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String)
    ultimaColeta = db.Column(db.String)
    
    def __init__(self, url, ultimaColeta):
        self.y=url = nome
        self.ultimaColeta = ultimaColeta
        
db.create_all()

@app.route("/link")
def link():
    return render_template("link.html")

@app.route("/inserirLink", methods=['GET', 'POST'])
def inserirLink():
    if request.method == "POST":
    url = request,form.get("url")
    ultimaColeta = request,form.get("ultimaColeta")


if __name__ == '__main__':
     app.run(debug=True)