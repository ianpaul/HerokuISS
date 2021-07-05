import flask
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = flask.Flask(__name__)

@app.route('/')

def findISS():

    url = 'http://api.open-notify.org/iss-now.json'

    df = pd.read_json(url)

    df['latitude'] = df.loc['latitude', 'iss_position']
    df['longitude'] = df.loc['longitude', 'iss_position']
    df.reset_index(inplace=True)

    df = df.drop(['index', 'message'], axis=1)

    fig = px.scatter_geo(df, lat='latitude', lon='longitude')
    pio.write_html(fig, file="/index.html", auto_open=False)

if __name__ == "__main__":
	app.debug = False
	port = int(os.environ.get('PORT', 33507))
	waitress.serve(app, port=port)

