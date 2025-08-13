from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Homepage route"""
    return render_template('index.html')

@app.route('/courses')
def courses():
    """Courses page route"""
    return render_template('courses.html')

if __name__ == '__main__':
    app.run(debug=True)
