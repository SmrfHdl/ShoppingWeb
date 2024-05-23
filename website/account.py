from flask import Blueprint, render_template, request, flash

account_bp = Blueprint('account', __name__)

@account_bp.route('/account', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'login':
            # Handle login
            print("Login data: ", request.form)
        elif action == 'register':
            # Handle register
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

            if len(username) < 2:
                flash('Username is too short.', category='error')
                pass
            elif len(email) < 4:
                flash('Email is invalid.', category='error')
                pass
            elif len(password) < 6:
                flash('Password must be at least 6 characters.', category='error')
                pass
            else: 
                flash('Account created!', category='success')

            print("Register data: ", request.form)
    return render_template("account.html")
