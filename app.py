"""
MVP hello world plotly dash (or just dash) app.
run with: $ python3 app.py

Requires only one package to run: dash

Recommended Process:
     $ python3 -m venv env; source env/bin/activate
(ENV)$ python3 -m pip install --upgrade pip
(ENV)$ python3 -m pip install git+https://github.com/psf/black
(ENV)$ python3 -m pip install pylint pydocstyle flake8
(ENV)$ python3 -m pip install -r requirements.txt

# optional auto-formatter
$ black app.py 

$ flake8 app.py; pylint app.py;

run with: $ python3 app.py

Open in browser:
http://127.0.0.1:8050

Press CTRL+C to quit (terminal server)

# Subsiquent cold-start run:
    $ source env/bin/activate; python3 app.py


"""

import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[html.H1("Hello World!")])

if __name__ == "__main__":
    app.run_server()
