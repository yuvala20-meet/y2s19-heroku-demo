from flask import Flask, render_temlete
app = Flask(__name__)

@app.route('/accessories')
	def accessories():
		return render_temlete("accessories.html")