import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load data
df = pd.read_csv("formatted_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort data
df = df.sort_values(by="Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    color="Region",
    title="Pink Morsel Sales Over Time"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div(children=[

    # Header
    html.H1("Soul Foods Sales Analysis - Pink Morsels"),

    # Line chart
    dcc.Graph(
        id="sales-chart",
        figure=fig
    )
])

# Run app
if __name__ == "__main__":
    app.run(debug=True)