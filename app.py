import dash
import dash_bootstrap_components as dbc

# bootstrap theme
external_stylesheets = [dbc.themes.COSMO, dbc.icons.BOOTSTRAP]
neecco_palette = ["#669900", "#1E88E5", "#FFC107", "#5B3000"]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)

app.title = "NEECCo Dashboard"
server = app.server
app.config.suppress_callback_exceptions = True
