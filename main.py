# Main Python module & application entry point

# Import flask package
from flask import Flask

# Import blueprints
from routes.usercontrol import userLogin_bp                     # Import user control blueprint

# Create flask application
app = Flask(__name__)

# Register blueprints
app.register_blueprint(userLogin_bp)        # Register user control blueprint


# Launch the application
if __name__ == '__main__':
    app.run(debug=True)