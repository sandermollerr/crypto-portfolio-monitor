from dashboard.app import dash_app
from dashboard.layouts import parent_structure

dash_app.layout = parent_structure.layout

parent_structure.render_callbacks(app=dash_app)

if __name__ == '__main__':
    dash_app.run_server(debug=True, port=8000, host='0.0.0.0')
