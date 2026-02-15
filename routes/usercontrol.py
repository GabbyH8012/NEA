from flask import Blueprint, request, render_template

# Blueprint for User account creation and login

userLogin_bp = Blueprint("userLogin", __name__, template_folder='../templates')


# createAccount handler
# =====================

@userLogin_bp.route("/createAccount", methods=['GET', 'POST'])
def createAccount():   
    
    # POST method for submitting account creation credentials
    if request.method == 'POST':
        
        # Read form data
        se_id = request.form.get('SE_ID')
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        repassword = request.form.get('repassword')

        # Reject blank input
        if se_id.strip() == '' or name.strip() == '' or email.strip() == '' or password.strip() == '' or repassword.strip() == '':   # Invalid input
            return "<h1>Invalid Swim England ID, name, email address, password or re-entered password!</h1>"
        
        else:
            # Valid input - check if passwords match
            if password != repassword:
                return "<h1>Passwords do not match!</h1>"
            else:
                # Valid input - check login credentials ...
                # dummy code here for now
                return f"<h1>Account created for {name} with Swim England ID {se_id}!</h1>"
    
    # Other methods assume first-time form visit - render static account creation form
    else:
        return render_template("createAccount.html")


# userLogin handler
# =================

@userLogin_bp.route("/login", methods=['GET', 'POST'])
def login():   
    
    # POST method for submitting login credentials
    if request.method == 'POST':
        
        # Read email address and password from the form
        se_id = request.form.get('SE_ID')
        email = request.form.get('email')
        password = request.form.get('password')

        # Reject blank input
        if se_id.strip() == '' or email.strip() == '' or password.strip() == '':   # Invalid input
            return "<h1>Invalid Swim England ID, email address or password!</h1>"
        
        else:

            # Valid input - check login credentials ...
            # dummy code here for now
            return f"<h1>Checking credentials for Swim England ID {se_id}!</h1>"

    # Other methods assume first-time form visit - render static login form
    else:
        return render_template('login.html')
    