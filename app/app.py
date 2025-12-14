# Import packages
from dash import Dash, html, dcc
import dash 
import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np 

# Unterschied dash - Dash - pcc usw. 

# Initialize the app
app = Dash(use_pages=True)

# App layout

app.layout = html.Div(children=[
    html.H1('Portfolio Manager'),
    html.Div(
        [dcc.Link(children=page["name"], href=page["path"]) for page in dash.page_registry.values()]
        ),
    dash.page_container

])

# Run the app
if __name__ == '__main__':
    app.run(debug=False)
