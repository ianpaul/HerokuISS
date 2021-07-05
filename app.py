import dash
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
    
app= dash.Dash(server=server, routes_pathname_prefix="/")
app.layout = dcc.Graph(figure=findISS(), style={"width": "100%", "height": "100vh"})

if __name__ == '__main__':
	app.run_server()
