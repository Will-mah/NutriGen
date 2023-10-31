from flask import Flask, request, render_template_string, flash
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messaging

# Basic HTML template for the input form
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Flask App</title>
    <!-- Bootstrap CSS CDN -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <!-- Your custom styles after Bootstrap to override if necessary -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
<div class="vh-100 d-flex flex-column justify-content-center align-items-center">
    <h1>Recipe Ingredient Scraper</h1>
    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul class="flashes">
        {% for message in messages %}
          <li>{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    <form method="post" class="w-50">
        <div class="form-group">
            <label for="url">URL:</label>
            <input type="text" class="form-control" id="url" name="url">
        </div>
        <button type="submit" class="btn btn-primary">Generate DashBoard</button>
    </form>
    {% if ingredients %}
        <h2>Ingredients:</h2>
        <ul>
        {% for ingredient in ingredients %}
            <li>{{ ingredient }}</li>
        {% endfor %}
        </ul>
    {% endif %}
</div>
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.5.9/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>'''

@app.route('/', methods=['GET', 'POST'])
def index():
    ingredients = []
    if request.method == 'POST':
        url = request.form['url']

        # Check if the URL is not empty
        if not url:
            flash('Please enter a URL.', 'error')
        else:
            try:
                # Fetch the content from the URL
                response = requests.get(url)
                page_content = BeautifulSoup(response.text, 'html.parser')

                # Find the container that holds the ingredients
                ingredients_container = page_content.find('div', {'class': 'recipe-ingredients-wrapper'})

                if ingredients_container:
                    # Extract the individual ingredients
                    ingredients_list = ingredients_container.find_all('li')
                    ingredients = [ingredient.get_text().strip() for ingredient in ingredients_list]
            except Exception as e:
                flash(f'An error occurred: {e}', 'error')

    return render_template_string(HTML_TEMPLATE, ingredients=ingredients)

if __name__ == '__main__':
    app.run(debug=True)
