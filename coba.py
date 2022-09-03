# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app (inilah API)
app = Flask(__name__)

# on the terminal type: curl "http://127.0.0.1:5000/" dengan url default localhost
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST']) # alamat endpoint
def home(): # fungsi yang berjalan di suatu endpoint
	if(request.method == 'GET'):

		data = "hello world"
		return jsonify({'data': data})


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/home/alone', methods = ['GET'])
def disp():

	return jsonify({'data': 4**2})


# driver function
if __name__ == '__main__':

	app.run(debug = True)
