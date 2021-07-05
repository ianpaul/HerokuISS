from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio
import json

app = Flask(__name__)

@app.route('/')

def findISS():

    url = 'http://api.open-notify.org/iss-now.json'

    df = pd.read_json(url)

    df['latitude'] = df.loc['latitude', 'iss_position']
    df['longitude'] = df.loc['longitude', 'iss_position']
    df.reset_index(inplace=True)

    df = df.drop(['index', 'message'], axis=1)

    fig = px.scatter_geo(df, lat='latitude', lon='longitude')
    graphJSON = json.dumps(fig, cls=plotly.utlils.PlotlyJSONEncoder)

    return render_template('display.html', graphJSON=graphJSON)

