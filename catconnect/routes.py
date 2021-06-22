from catconnect import app
from flask import render_template
from catconnect.models import Item
from catconnect.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/adoptionpage')
def adoption_page():
    cats = Item.query.all()
    return render_template('adoptionpage.html', cats=cats)

@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html',form=form)