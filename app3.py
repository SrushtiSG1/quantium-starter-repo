import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(by="Date")

# Create app
app = Dash(__name__)

# Layout
app.layout = html.Div(style={
    "backgroundColor": "#f4f6f9",
    "padding": "20px",
    "fontFamily": "Arial"
}, children=[

    html.H1(
        "📊 Soul Foods Sales Dashboard",
        style={
            "textAlign": "center",
            "color": "#2c3e50"
        }
    ),

    html.Div([
        html.Label("Select Region:", style={"fontWeight": "bold"}),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"marginBottom": "20px"}
        )
    ], style={"textAlign": "center"}),

    dcc.Graph(id="sales-chart")
])

# Callback (this is the brain)
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region",
        title="Sales Trend of Pink Morsels"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f4f6f9",
        xaxis_title="Date",
        yaxis_title="Sales",
        title_x=0.5
    )

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)