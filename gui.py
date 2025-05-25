import dash
from dash import dcc, html, Input, Output, State
import joblib
import pandas as pd

model = joblib.load('./model/water_potability_predictor.pkl')

app = dash.Dash(__name__)
app.title = "Water Potability Predictor"

app.layout = html.Div(
    style={"maxWidth": "600px", "margin": "auto", "padding": "20px", "fontFamily": "Arial, sans-serif"},
    children=[
        html.H1("Water Potability Predictor", style={"textAlign": "center"}),
        html.P(
            "Enter water quality measurements below to predict if the water is safe to drink:",
            style={"textAlign": "center"}
        ),
        html.Div([
            html.Label("pH (6.5–8.5):"),
            dcc.Input(id="input-ph", type="number", step=0.01, placeholder="e.g. 7.2", style={"width": "100%"}),
            html.Br(), html.Br(),

            html.Label("Hardness (mg/L):"),
            dcc.Input(id="input-hardness", type="number", step=0.1, placeholder="e.g. 150", style={"width": "100%"}),
            html.Br(), html.Br(),

            html.Label("TDS (Total Dissolved Solids in mg/L):"),
            dcc.Input(id="input-tds", type="number", step=0.1, placeholder="e.g. 500", style={"width": "100%"}),
            html.Br(), html.Br(),

            html.Label("Chloramines (mg/L):"),
            dcc.Input(id="input-chloramines", type="number", step=0.01, placeholder="e.g. 2.0", style={"width": "100%"}),
            html.Br(), html.Br(),

            html.Label("Sulfate (mg/L):"),
            dcc.Input(id="input-sulfate", type="number", step=0.1, placeholder="e.g. 250", style={"width": "100%"}),
            html.Br(), html.Br(),

            html.Label("Conductivity (µS/cm):"),
            dcc.Input(id="input-conductivity", type="number", step=0.1, placeholder="e.g. 400", style={"width": "100%"}),
            html.Br(), html.Br(),

            html.Label("Turbidity (NTU):"),
            dcc.Input(id="input-turbidity", type="number", step=0.1, placeholder="e.g. 1.5", style={"width": "100%"}),
            html.Br(), html.Br(),

            html.Button("Predict Potability", id="btn-predict", n_clicks=0, style={"width": "100%", "padding": "10px"}),
            html.Br(), html.Br(),

            html.Div(id="prediction-output", style={"textAlign": "center", "fontSize": "20px", "fontWeight": "bold"})
        ])
    ]
)

@app.callback(
    Output("prediction-output", "children"),
    Input("btn-predict", "n_clicks"),
    State("input-ph", "value"),
    State("input-hardness", "value"),
    State("input-tds", "value"),
    State("input-chloramines", "value"),
    State("input-sulfate", "value"),
    State("input-conductivity", "value"),
    State("input-turbidity", "value"),
)
def predict_potability(n_clicks, ph, hardness, tds, chloramines, sulfate, conductivity, turbidity):
    if n_clicks is None or n_clicks == 0:
        return ""
    inputs = [ph, hardness, tds, chloramines, sulfate, conductivity, turbidity]
    if any(v is None for v in inputs):
        return "Please fill in all fields before predicting."

    data = pd.DataFrame([{
        'ph': ph,
        'Hardness': hardness,
        'Solids': tds,
        'Chloramines': chloramines,
        'Sulfate': sulfate,
        'Conductivity': conductivity,
        'Turbidity': turbidity
    }])

    pred = model.predict(data)[0]
    prob = model.predict_proba(data)[0][pred]

    if pred == 1:
        return f"Safe to drink! (Confidence: {prob*100:.1f}%)"
    else:
        return f"Not safe to drink. (Confidence: {prob*100:.1f}%)"

if __name__ == '__main__':
    app.run(debug=True)
