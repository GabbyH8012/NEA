#### imports ####
from flask import Blueprint, request, render_template
from database.database import add_new_swimmer, check_existing_swimmer


# Create Blueprint for User account creation and login
userManagement_bp = Blueprint("userManagement", __name__, template_folder='../templates')


# user login handler
# -----------------
@userManagement_bp.route("/login", methods=['GET', 'POST'])
def login():   

    if request.method == 'POST':
        
        # Read data from the form if method is POST - data is submitted
        se_id = request.form.get('SE_ID')
        email = request.form.get('email')
        password = request.form.get('password')

        # Reject blank input
        if se_id.strip() == '' or email.strip() == '' or password.strip() == '':   
            return "Complete all required fields"
        
        else:
            # Valid input - check login credentials
            return f"Checking credentials for Swim England ID {se_id}"

    # or assuming first-time form visit - load login form
    else:
        return render_template('login.html')
    

# createAccount handler
# ---------------------
@userManagement_bp.route("/createAccount", methods=['GET', 'POST'])
def createAccount():   
    
    if request.method == 'POST':

        # Read data from the form if method is POST - data is submitted
        se_id = int(request.form.get('SE_ID'))
        name = str(request.form.get('name'))
        email = str(request.form.get('email'))
        password = str(request.form.get('password'))
        repassword = str(request.form.get('repassword'))

        # Reject blank input
        if name.strip() == '' or email.strip() == '' or password.strip() == '' or repassword.strip() == '':   # Invalid input
            return "Invalid Swim England ID, name, email address, password or re-entered password"
        
        else:
            # Valid input - check if passwords match
            if password != repassword:
                return "Passwords do not match"
            else:
                # Valid input - check for existing record befor adding new swimmer to database
                if check_existing_swimmer(int(se_id)):
                    return "<h1>Swimmer with this Swim England ID already exists!</h1>"
                else:
                    successful_add = add_new_swimmer(se_id, name, email, password)

                    if not successful_add:
                        return "<h1>Failed to create account due to database error!</h1>"
                    else:
                        return f"<h1>Account created for {name} with Swim England ID {se_id}!</h1>"
                        
    # or if method is not POST, assuming first-time form visit - load login form
    else:
        return render_template("createAccount.html")



    