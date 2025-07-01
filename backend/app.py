from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# @app.route('/')
# def index():
#     msg = "Hey user!" # assume this msg data is from database
#     return render_template('index.html', message=msg)

@app.route('/api')
def api():
    msg = "Hey Nandan!" # assume this msg data is from database
    return {'msg': msg}

if __name__ == "__main__":
    app.run(debug=True)