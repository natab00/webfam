from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Iwanttobuy1@localhost/Labuschewsky'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#from app import models

if __name__ == '__main__':
    app.run(debug = True)
    

@app.route('/')
def home():
    return render_template('index.html')
    return app

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)




class Contact(db.Model):
    __tablename__ = 'contact_form'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80))
    phone = db.Column(db.String(80))
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text())

    def __init__(self, fname, lname, phone, email, message):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        self.message = message

#@app.route('/submit_form', methods=['POST', 'GET'])
#def submit_form():
    #if  request.method == 'POST':
        #fname = request.form.get("fname")
        #data = request.form.to_dict()
        #print(data)
        #entry = Contact(request.form["fname"], request.form["lname"], request.form["phone"], request.form["email"], request.form["message"])
        #db.session.add(entry)
        #db.session.commit()

        #return render_template('/thanks.html', name=fname)
    #else:
        #return 'something went wrong'

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
       fname = request.form.get("fname")
       lname = request.form['lname']
       phone = request.form['phone']
       email = request.form['email']
       message = request.form['message']
       entry = Contact(fname, lname, phone, email, message) 
       db.session.add(entry)
       db.session.commit()
       return render_template('/thanks.html', name=fname)
    else:
        return 'something went wrong'