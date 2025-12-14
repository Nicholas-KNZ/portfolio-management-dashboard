# Import packages
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np 

# Import Dummy Data 
df = pd.read_csv('app/data/portfolio1.csv')

# Create Asset Allocation Chart 
# Calcualte Allocation 

df_pie = pd.concat([df["Symbol"], df["Wert"] / np.sum(df["Wert"])], axis=1)

# Group by company
df_pie = df_pie.groupby(["Symbol"], as_index=False).sum()

# Create pie chart
fig = px.pie(df_pie, values='Wert', names='Symbol', title='Portfolio Pie Chart')




# Initialize the app
app = Dash()

# App layout

app.layout = html.Div(children=[
    html.H1('Portfolio Manager'),
    dcc.Graph(
        id='portfolio-pie',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
