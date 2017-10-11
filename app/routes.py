from flask import render_template
from app import app

from app.ramen.controllers import ramen_api

app.register_blueprint(ramen_api, url_prefix='/ramen')

@app.route('/')
def index():
    return render_template('index.html')
