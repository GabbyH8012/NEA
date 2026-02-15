from flask import Blueprint, render_template

# Blueprint for User account creation and login

userLogin_bp = Blueprint("userLogin", __name__, template_folder='../templates')

@userLogin_bp.route("/createAccount")
def createAccount():   
    return render_template("createAccount.html")

@userLogin_bp.route("/login")
def login():   
    return render_template("login.html")