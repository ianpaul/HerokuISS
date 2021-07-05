import flask
import space2

app = flask.Flask(__name__)

@app.route('/')

def space():
	info = findISS()
	render_template('display.html', info=info['data'])
	return res

if __name__ == "__main__":
	app.debug = False
	port = int(os.environ.get('PORT', 33507))
	waitress.serve(app, port=port)

