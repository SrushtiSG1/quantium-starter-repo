import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/your_dataset.csv")

# Create app
app = dash.Dash(__name__)

# Create a simple graph
fig = px.histogram(df, x=df.columns[0])

# Layout
app.layout = html.Div([
    html.H1("Data Dashboard"),
    dcc.Graph(figure=fig)
])

# Run app
if __name__ == "__main__":
    app.run(debug=True)