from flask import render_template
from . import main


@main.route('/')
@main.route('/Home')
def index():
    title = "Home - Welcome to Let's Blog"
    return render_template('index.html', title=title)
