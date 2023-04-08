from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template("main/home.html", title='Home')

@main.route('/about')
def about():
    return render_template("main/about.html", title='About')

@main.route('/pulsetool')
def pulsetool():
    return render_template("main/pulsetool.html", title='Pulse Tool')

@main.route('/products')
def products():
    return render_template("main/products.html", title='Products')