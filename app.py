from flask import Flask, render_template
import os

app = Flask(__name__)

# Dynamically create a route for each HTML file in the templates folder
template_folder = os.path.join(app.root_path, 'templates')
html_files = [f for f in os.listdir(template_folder) if f.endswith('.html')]

@app.route('/')
def index():
    # Default route serves index.html
    return render_template('index.html')

# Create a route for each HTML file except index.html
for html_file in html_files:
    if html_file == 'index.html':
        continue
    route = f"/{os.path.splitext(html_file)[0]}"
    def make_route(template_name):
        def route_func():
            return render_template(template_name)
        return route_func
    app.add_url_rule(route, html_file, make_route(html_file))

if __name__ == "__main__":
    # Run the Flask development server
    app.run(debug=True, host="127.0.0.1", port=5000)
