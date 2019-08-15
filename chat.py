import mysql.connector

from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__, static_url_path="/static", static_folder="/templates")

@app.route('/')
def index():
	return render_template('chat.html')

@app.route('/read')
def store():
	text = (request.args.get('line')).split(':')
	print(text[0] + text[1])
	conn = mysql.connector.connect(host="localhost", user="student", passwd="fredfredburger", database="student")
	cursor = conn.cursor()
	cursor.execute("INSERT INTO kylechat (name, msg) VALUES (text[0], text[1])")

if __name__ == '__main__':
	app.run('198.110.204.9', 5001, debug = True)
