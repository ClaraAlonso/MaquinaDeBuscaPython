from flask import Flask, render_template, request, url_for, redirect

from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

class Link(db.Model):
    
    __tablename__ = 'link'
    
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String)
    #ultimaColeta = db.Column(db.String)
    
    def __init__(self, url, ultimaColeta):
        self.url = url
        #self.ultimaColeta = ultimaColeta
        
db.create_all()

@app.route("/link")
def link():
    return render_template("link.html")

@app.route("/inserirLink", methods=['GET', 'POST'])
def inserirLink():
    if request.method == "POST":
        url = request.form.get("url")
        #ultimaColeta = request.form.get("ultimaColeta")
    
        if url:
            link = Link(url)
            db.session.add(link)
            db.session.commit()

    return redirect(url_for("index"))

@app.route("/listaLink")
def lista():
    link = Link.query.all()
    return render_template("listaLink.html", link=link)

if __name__ == '__main__':
     app.run(debug=True)