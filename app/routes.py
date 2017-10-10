from flask import render_template
from app import app

@app.route('/')
def index():
    import pdb; pdb.set_trace(); #gitignore
    return render_template('index.html')
