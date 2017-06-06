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
		ini2()
		time.sleep(1)
		forward()
		ini2()
	elif data == "down":
		print("down")
		up()
	elif data == "left":
		print("left")
		ini2()
		time.sleep(1)
		left()
		left()
		left()
		left()
		left()
		ini2()
	elif data == "right":
		print("right")
		ini2()
		time.sleep(1)
		right()
		right()
		right()
		right()
		right()
		ini2()
	elif data == "init2":
		print("fight")
		ini2()
	elif data == "res":
		print("rescue")
		time.sleep(3)
		ini3()
		time.sleep(2)
	else:
		print("data is error!")
	return 'You POSTED!'

if __name__ == "__main__":
	init()
	app.run(debug=True, host='127.0.0.1')
