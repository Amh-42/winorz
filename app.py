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

@app.route('/checkout')
def checkout():
    """Checkout page route for WINORZ+ Elite access"""
    return render_template('checkout.html')

@app.route('/success')
def success():
    """Success page after completing Elite purchase"""
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
