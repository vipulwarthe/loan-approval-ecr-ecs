from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define another route for the home page
@app.route('/home')
def home():
    return render_template('home.html')

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
