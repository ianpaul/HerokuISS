import dash
from flask import Flask
import dash_core_components as dcc
import pandas as pd
import plotly.express as px
import plotly
import json

app = dash.Dash(__name__)

url = 'http://api.open-notify.org/iss-now.json'

df = pd.read_json(url)

df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True)

df = df.drop(['index', 'message'], axis=1)

fig = px.scatter_geo(df, lat='latitude', lon='longitude')

server = Flask(__name__)
app = dash.Dash(server=server)
app.layout = dcc.Graph(figure=fig)

if __name__ == '__main__':
	app.run_server(debug=True, use_reloader=False)
