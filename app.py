import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Load data
import pandas as pd

file0 = "data/daily_sales_data_0.csv"
file1 = "data/daily_sales_data_1.csv"
file2 = "data/daily_sales_data_2.csv"

df1 = pd.read_csv(file0)
df2 = pd.read_csv(file1)
df3 = pd.read_csv(file2)

df = pd.concat([df1, df2, df3], ignore_index=True)

print(df.head())

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