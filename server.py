from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello.html")

@app.route("/post", methods=['POST'])
def post():
    data = request.form['data']
    print(data)
    return 'You POSTED!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')