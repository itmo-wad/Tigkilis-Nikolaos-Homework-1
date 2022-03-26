import os
from flask import Flask, flash, render_template , redirect


app = Flask(__name__)
app.secret_key = 'super67sEcret459!!key@s'
print('---LOG: best debug method: WEBSITE: OK')

@app.route('/')
def index():
    return redirect("/profile")

@app.route('/profile')
def profile():
    return render_template("index.html")

@app.route('/secret')
def secret():
    flash("Ha! You found me!")
    return render_template("index.html")

app.run(host='localhost', port=5000)