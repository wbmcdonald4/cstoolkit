from flask import Blueprint, render_template, request, redirect, url_for
from src.main.util import append_email_to_google_sheet

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template("main/home.html", title='Home')

@main.route('/about')
def about():
    return render_template("main/about.html", title='About')

@main.route('/pulse')
def pulse():
    return render_template("main/pulse.html", title='Pulse Tool')

@main.route('/onboardingtool')
def onboardingtool():
    return render_template("main/onboardingtool.html", title='Onboarding Tool')

@main.route('/capture_email', methods=['POST'])
def capture_email():
    email = request.form['email']
    append_email_to_google_sheet(email)
    return redirect(url_for('main.install_app'))

@main.route('/capture_onboarding_email', methods=['POST'])
def capture_onboarding_email():
    email = request.form['email']
    append_email_to_google_sheet(email)
    return redirect(url_for('main.home'))

@main.route('/install_app')
def install_app():
    # Render the app install page
    return render_template('main/install_app.html')
