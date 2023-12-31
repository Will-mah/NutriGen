# Recipe Ingredient Parser and Macro Calculator with Flask Web App Interface

## Overview
The Recipe Ingredient Parser and Macro Calculator is a comprehensive tool that extracts ingredient information from online recipes, calculates their nutritional macros, and now features a Flask web application interface for ease of use. This tool is perfect for anyone looking to gain detailed insights into the nutritional content of recipes for diet planning, meal prep, or culinary analysis. (currently only works on BBC recipes: https://www.bbc.co.uk/food/recipes)

## Key Features
- **Web-Based Interface**: Utilizes a Flask web app for easy interaction with the tool through a browser.
- **Ingredient Extraction**: Automatically scrapes ingredients from recipes listed on web pages.
- **Advanced Text Processing**: Processes ingredient text to accommodate various formats and units.
- **Nutritional Macro Calculation**: Calculates macros based on ingredient quantity and standard serving sizes from a nutritional database.
- **Quantity Parsing and Adjustment**: Parses quantities from the recipe and adjusts macro values accordingly.
- **Unicode and Fraction Handling**: Converts Unicode fractions for precise measurements.
- **Structured Output with Macros**: Outputs ingredients with names, quantities, and corresponding nutritional information in a user-friendly format.

## How It Works
1. The user inputs the URL of a recipe into the Flask web app interface.
2. The tool scrapes the recipe webpage to gather ingredients and quantities.
3. Ingredients are normalized and matched with nutritional information from a database.
4. Quantities are parsed and nutritional information is adjusted based on the recipe's serving sizes.
5. The web app displays a structured list of ingredients along with their detailed macro calculations.

## Technologies Used
- Python for backend development, providing a solid foundation for the tool's logic.
- Flask for creating a user-friendly web app interface.
- `requests` and `BeautifulSoup` for web scraping functionality.
- Regular expressions and custom parsing algorithms for processing text data.
- CSV database integration for accessing and calculating nutritional information.

## Usage
1. Launch the Flask web app and navigate to the provided URL in a web browser.
2. Enter the URL of the recipe into the app's input field and submit.
3. The web app processes the input, displaying each ingredient's name, required quantity, and calculated macros in an organized table.

## Conclusion
The Recipe Ingredient Parser and Macro Calculator's integration with a Flask web app significantly enhances its accessibility and user experience. It provides an intuitive and interactive way to analyze recipes, offering immediate nutritional insights within a web interface. This powerful tool is an asset for anyone aiming to understand and manage their dietary habits through informed recipe analysis.
