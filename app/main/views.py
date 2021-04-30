from flask import render_template
from . import main
from flask_login import login_required


@main.route('/')
@main.route('/Home')
def index():
    title = "Home - Welcome to Let's Blog"
    return render_template('index.html', title=title)


@main.route('/blogs')
def blogs():
    return render_template('blogs.html')

@main.route('/add_blog', methods=["GET","POST"])
@login_required
def add_blog():
    return render_template(add_blog.html)
    
