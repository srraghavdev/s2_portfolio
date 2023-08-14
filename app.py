from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/projects')  # New route for the Projects page
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run(debug=True)
