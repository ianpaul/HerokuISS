import dash
from flask import Flask
import dash_core_components as dcc
import pandas as pd
import plotly.express as px
import plotly
import json

app = dash.Dash(__name__)

def findISS():

    url = 'http://api.open-notify.org/iss-now.json'

    df = pd.read_json(url)

    df['latitude'] = df.loc['latitude', 'iss_position']
    df['longitude'] = df.loc['longitude', 'iss_position']
    df.reset_index(inplace=True)

    df = df.drop(['index', 'message'], axis=1)

    fig = px.scatter_geo(df, lat='latitude', lon='longitude')
    return dcc.Graph(figure=fig, style={"width": "1920px", "height": "1080px", "display": "inline-block"})

server = Flask(__name__)
app = dash.Dash(server=server)

app.layout = findISS

if __name__ == '__main__':
	app.run_server(debug=True)
