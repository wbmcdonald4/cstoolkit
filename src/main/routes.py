from flask import Blueprint, render_template, request, redirect, url_for
from src.main.util import append_email_to_google_sheet

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    logos = [
        'fantazscores', 
        'fittes', 
        'propcheck', 
        # 'partnerstack'
        ]
    return render_template("main/home.html", title='Home', logos=logos)

# obsolete
@main.route('/contact')
def contact():
    return render_template("main/contact.html", title='contact')

@main.route('/pulse')
def pulse():
    return render_template("main/pulse.html", title='Pulse')

@main.route('/onboard')
def onboard():
    return render_template("main/onboard.html", title='Onboard')

@main.route('/capture_onboarding_email', methods=['POST'])
def capture_onboarding_email():
    email = request.form['email']
    append_email_to_google_sheet(email)
    return redirect(url_for('main.home'))

@main.route('/about')
def about():
    return render_template("main/about.html", title='About')