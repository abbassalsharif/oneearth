import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html

file_encoding = 'utf8'        # set file_encoding to the file encoding (for country names)
input_file_and_path = 'OneEarth.csv'
input_fd = open(input_file_and_path, encoding=file_encoding, errors = 'backslashreplace')
data = pd.read_csv(input_fd)

data['Color'] = '#' + data['Color']

data['Text'] = data['Country'] + '<br>' + \
               (data['GSN target']*100).round(2).map(str) + '%'

fig = go.Figure(
    data=go.Choropleth(
        locations=data['Country'], 
        z = data['GSN target'].astype(float), # Data to be color-coded
        locationmode = 'country names', # set of locations match entries in `locations`
        colorscale = data['Color'],
        reversescale=True,
        colorbar_title = "GSN Target", 
        hovertext = data['Text'],
        hoverinfo = 'text', 
        colorbar = dict(
            tickvals=[0, 0.2, 0.4, 0.6, 0.8, 0.98], 
            ticktext=['0','20%', '40%', '60%', '80%', '99%',]
        )
    )
)

fig.update_layout(
    title_text = 'GSN Target by Country',
    width = 1200,
    height = 800
)

# fig.show()
app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id = 'map', figure = fig)
])

if __name__ == '__main__':
    app.run_server(debug=False)