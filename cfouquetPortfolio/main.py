
from flask import Flask, render_template

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def default_route(name=None):
    return render_template('main.html', name=name)

