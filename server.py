from flask import *
from simpletest import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello.html")

@app.route("/post", methods=['POST'])
def post():
	data = request.form['data']
	if data == "init":
		print("init")
		init()
	elif data == "up":
		print("up")
		forward()
		ini2()
	elif data == "down":
		print("down")
		up()
	elif data == "left":
		print("left")
		left()
		left()
		left()
		left()
		left()
		ini2()
	elif data == "right":
		print("right")
		right()
		right()
		right()
		right()
		right()
		ini2()
	else:
		print("data is error!")
	return 'You POSTED!'

if __name__ == "__main__":
	init()
	app.run(debug=True, host='0.0.0.0')
