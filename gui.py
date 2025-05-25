import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State
import joblib
import pandas as pd

model = joblib.load('./model/water_potability_predictor.pkl')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "Water Potability Predictor"

dbc_css = {
    "maxWidth": "600px",
    "margin": "auto",
    "padding": "20px"
}

app.layout = dbc.Container(
    fluid=True,
    className="p-4",
    children=[
        dbc.Row(
            dbc.Col(
                html.H1(
                    "💧 Water Potability Predictor",
                    className="text-center text-primary mb-4"
                ),
                width=12
            )
        ),
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H5("Enter Water Quality Parameters", className="card-title mb-3"),
                        dbc.Row([
                            dbc.Col(html.Div([
                                dbc.Label("pH (6.5–8.5)"),
                                dbc.Input(id="input-ph", type="number", step=0.01, placeholder="7.2"),
                            ], className="mb-3"), md=6),
                            dbc.Col(html.Div([
                                dbc.Label("Hardness (mg/L)"),
                                dbc.Input(id="input-hardness", type="number", step=0.1, placeholder="150"),
                            ], className="mb-3"), md=6),
                        ]),
                        dbc.Row([
                            dbc.Col(html.Div([
                                dbc.Label("TDS (mg/L)"),
                                dbc.Input(id="input-tds", type="number", step=0.1, placeholder="500"),
                            ], className="mb-3"), md=6),
                            dbc.Col(html.Div([
                                dbc.Label("Chloramines (mg/L)"),
                                dbc.Input(id="input-chloramines", type="number", step=0.01, placeholder="2.0"),
                            ], className="mb-3"), md=6),
                        ]),
                        dbc.Row([
                            dbc.Col(html.Div([
                                dbc.Label("Sulfate (mg/L)"),
                                dbc.Input(id="input-sulfate", type="number", step=0.1, placeholder="250"),
                            ], className="mb-3"), md=6),
                            dbc.Col(html.Div([
                                dbc.Label("Conductivity (µS/cm)"),
                                dbc.Input(id="input-conductivity", type="number", step=0.1, placeholder="400"),
                            ], className="mb-3"), md=6),
                        ]),
                        dbc.Row([
                            dbc.Col(html.Div([
                                dbc.Label("Turbidity (NTU)"),
                                dbc.Input(id="input-turbidity", type="number", step=0.1, placeholder="1.5"),
                            ], className="mb-3"), md=6),
                        ]),
                        dbc.Button(
                            "Predict Potability",
                            id="btn-predict",
                            color="primary",
                            className="mt-3 w-100"
                        ),
                        dcc.Loading(
                            id="loading-output",
                            type="default",
                            children=html.Div(id="prediction-output", className="mt-3 text-center fw-bold")
                        )
                    ])
                ),
                width=8,
                className="d-flex justify-content-center"
            )
        ], justify="center", align="start")
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
    if not n_clicks:
        return ""
    inputs = [ph, hardness, tds, chloramines, sulfate, conductivity, turbidity]
    if any(v is None for v in inputs):
        return "Please fill in all fields before predicting."

    df_input = pd.DataFrame([{
        'ph': ph,
        'Hardness': hardness,
        'Solids': tds,
        'Chloramines': chloramines,
        'Sulfate': sulfate,
        'Conductivity': conductivity,
        'Turbidity': turbidity
    }])
    pred = model.predict(df_input)[0]
    prob = model.predict_proba(df_input)[0][pred]

    if pred:
        return f"✅ Safe to drink! Confidence: {prob*100:.1f}%"
    return f"❌ Not safe to drink. Confidence: {prob*100:.1f}%"

if __name__ == '__main__':
    app.run(debug=True)
