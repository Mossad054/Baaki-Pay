from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Path to the JSON file to store user data
JSON_FILE = 'users.json'

# Home route 
@app.route('/')
def index():
    return render_template('landing/homelanding/index.html')

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        
        # Create a dictionary with user data
        user_data = {'username': username, 'email': email}
        
        # Check if JSON file exists, if not create an empty list
        if not os.path.exists(JSON_FILE):
            with open(JSON_FILE, 'w') as f:
                json.dump([], f)
        
        # Read existing data from JSON file
        with open(JSON_FILE, 'r') as f:
            data = json.load(f)
        
        # Append new user data to the list
        data.append(user_data)
        
        # Write updated data back to the JSON file
        with open(JSON_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        
        # Return a message to the user upon successful signup
        return render_template('authentication/signup.html', message='Signup successful!')

    return render_template('authentication/signup.html')
    
if __name__ == '__main__':
    app.run(debug=True)
