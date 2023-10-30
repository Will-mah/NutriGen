import requests
from bs4 import BeautifulSoup
import re

# URL of the page with the ingredients list
url = 'https://www.bbc.co.uk/food/recipes/fluffyamericanpancak_74828'

# Fetch the content from the URL
response = requests.get(url)
page_content = BeautifulSoup(response.text, 'html.parser')

# Find the container that holds the ingredients
ingredients_container = page_content.find('div', {'class': 'recipe-ingredients-wrapper'})

# Extract the individual ingredients
ingredients = ingredients_container.find_all('li')  # e.g., 'li' for list items

# Process and store the ingredients
ingredient_list = [ingredient.get_text().strip() for ingredient in ingredients]

print(ingredient_list)

#############################


# Mapping of Unicode fraction characters to their string equivalents
unicode_fraction_mapping = {
    '\u00BC': ' 1/4',
    '\u00BD': ' 1/2',
    '\u00BE': ' 3/4',
    '\u2150': ' 1/7',
    '\u2151': ' 1/9',
    '\u2152': ' 1/10',
    '\u2153': ' 1/3',
    '\u2154': ' 2/3',
    '\u2155': ' 1/5',
    '\u2156': ' 2/5',
    '\u2157': ' 3/5',
    '\u2158': ' 4/5',
    '\u2159': ' 1/6',
    '\u215A': ' 5/6',
    '\u215B': ' 1/8',
    '\u215C': ' 3/8',
    '\u215D': ' 5/8',
    '\u215E': ' 7/8',
 }

ingredient_pattern = re.compile(
        r'('
        r'\b\d*[\s]*'  # Matches the optional whole number part of the quantity
        r'(?:\d+/\d+|[\u00BC-\u00BE\u2150-\u215E])?'  # Matches fractional part of the quantity (including unicode fractions)
        r'[\s]*'  # Matches any spaces following the numbers
        r'(?:fl\.?\s?)?'  # Optionally matches 'fl' abbreviation for fluid measurements
        r'(?:g|oz|lbs?|kg|tbsp?|tsp|cups?|ml|l|pints?|quarts?|gallons?|litres?|liters?)'  # Matches the unit including long-form like 'litres'
        r'[\s\/]*'  # Matches spaces or slashes after the unit
        r'(?:\d*[\s]*'  # Matches an optional whole number for alternative measurements
        r'(?:\d+/\d+|[\u00BC-\u00BE\u2150-\u215E])?'  # Matches fractional part of the alternative measurements (including unicode fractions)
        r'[\s]*'  # Matches any spaces following the alternative measurements
        r'(?:fl\.?\s?)?'  # Optionally matches 'fl' abbreviation for fluid measurements
        r'(?:g|oz|lbs?|kg|tbsp?|tsp|cups?|ml|l|pints?|quarts?|gallons?|litres?|liters?)?'  # Optionally matches the unit for alternative measurements including long-form
        r')?'  # Makes the entire alternative measurements part optional
        r'\b\.?'  # Matches a word boundary and an optional period
        r')'
        r'(\s.*$)',  # The rest is the ingredient name
        re.IGNORECASE
    )

def convert_unicode_fractions(ingredient):
    for unicode_fraction, string_fraction in unicode_fraction_mapping.items():
        ingredient = ingredient.replace(unicode_fraction, string_fraction)
    return ingredient

# Define a function to split ingredient strings into quantity and name

def split_ingredient(ingredient):
    # Convert Unicode fractions to string fractions
    ingredient = convert_unicode_fractions(ingredient)
    
    # Use the precompiled regex pattern
    match = ingredient_pattern.match(ingredient)
    
    if match:
        quantity = match.group(1).strip()
        name = match.group(2).strip()
    else:
        # If the regex pattern does not match, then check if the ingredient starts with a standalone number
        standalone_number_match = re.match(r'^(\d+)\s+(.*)$', ingredient)
        if standalone_number_match:
            quantity = standalone_number_match.group(1)
            name = standalone_number_match.group(2)
        else:
            quantity = 'Unknown quantity'
            name = ingredient

    # Post-processing to remove known long-form units from the ingredient name and add them to the quantity
    long_form_units = ['litre', 'liter', 'pint', 'quart', 'gallon', 'cup', 'tablespoon', 'teaspoon']
    name_components = name.lower().split()
    for unit in long_form_units:
        if unit in name_components:
            quantity += f' {unit}'
            name = ' '.join(word for word in name_components if word != unit)
            break  # Stop the loop once the unit is found and processed

    # Capitalize the first letter of each word in the ingredient name for better readability
    name = ' '.join(word.capitalize() for word in name.split())

    return quantity, name

# Test the function
# ingredient_list = [
#     '75g/2½oz self-raising flour',
#     '1 cup/240ml milk',
#     '1/2 tbsp vanilla extract',
#     '140g/5oz butter, softened',
#     '4 eggs',
#     '1 litre/1¾ pints vegetable stock',
#     '½ tsp salt'  # Added this test case
# ]


split_ingredients = [split_ingredient(ingredient) for ingredient in ingredient_list]


# Display the results
for quantity, name in split_ingredients:
    print(f'Ingredient: {name}, Quantity: {quantity}')

