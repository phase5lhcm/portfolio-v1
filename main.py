from portfolio_app_v1 import app
from flask import  render_template

@app.route('/')
def test():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)