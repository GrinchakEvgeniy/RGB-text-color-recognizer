from flask import Flask
from flask import render_template
from flask import request
from random import randint
import csv

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
	color = [randint(0, 255), randint(0, 255), randint(0, 255)]
	if request.method == 'POST':
		list_to_csv = [request.form['red'], request.form['green'], request.form['blue'], request.form['textcolor']]
		write(list_to_csv, request.form['red'])
	return render_template('hello.html', color=color)

def write(list_to_csv, do):
	with open('train_data.csv') as f:
		f.readline()
		line = f.readline()
		print(line)
		if line == '':
			f = open('train_data.csv', 'w',newline='')
			with f:
				writer = csv.writer(f,delimiter=',')
				writer.writerow(['red', 'green', 'blue', 'textColor'])
				writer.writerow(list_to_csv)
		else:
			f = open('train_data.csv', 'a',newline='')
			with f:
				writer = csv.writer(f,delimiter=',')
				writer.writerow(list_to_csv)
	# else:
	# 	f = open('train_data.csv', 'w')
	# 	with f:
	# 		writer = csv.writer(f)
	# 		writer.writerow(['red', 'green', 'blue', 'textColor'])
	# 		writer.writerow(list_to_csv)


if __name__ == '__main__':
	app.run(debug=True)