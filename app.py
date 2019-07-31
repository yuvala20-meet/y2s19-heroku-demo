from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def fashion():
	return render_template('fasion.html')

@app.route('/accessories')
def accessories():
	return render_template("accessories.html")

if __name__ == '__main__':
    app.run(debug=True)