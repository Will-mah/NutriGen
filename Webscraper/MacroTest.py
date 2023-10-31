import csv
import os
import re

print("Current working directory:", os.getcwd())



# Function to read the CSV and convert it into a dictionary
def read_macro_csv(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        macro_dict = {row['name'].lower(): row for row in reader}
    return macro_dict

scraped_ingredients = [
    {'name': 'vegetable oil', 'quantity': '2 tbsp'},
    {'name': 'onion', 'quantity': '1 large'},
    {'name': 'potato', 'quantity': '300g'},
    {'name': 'leeks', 'quantity': '2'},
    {'name': 'vegetable stock', 'quantity': '500ml'},
    {'name': 'crème fraîche', 'quantity': '100ml'}
]

# Read the CSV file
csv_file_name = "MacroTest.csv"
macro_dict = read_macro_csv(csv_file_name)

# Function to normalize ingredient names (basic example, you might need a more sophisticated approach)
def normalize_name(ingredient_name):
    return ingredient_name.lower().strip()

# New function to parse quantity and unit from the ingredient string
def parse_quantity(quantity_str):
    # This regex will match numbers and common units, expand as necessary.
    pattern = re.compile(r'(?P<quantity>\d+(\.\d+)?)(?P<unit>\s*(g|ml|tbsp|oz|cup|large|small)?)')
    match = pattern.match(quantity_str)
    if match:
        quantity = match.group('quantity')
        unit = match.group('unit').strip() if match.group('unit') else 'unit unknown'
        return (float(quantity), unit)
    else:
        return (quantity_str, 'unit unknown')

# Now let's parse your scraped ingredients
for ingredient in scraped_ingredients:
    name = ingredient['name']
    quantity_str = ingredient['quantity']
    parsed_quantity = parse_quantity(quantity_str)
    print(f"Processing ingredient: {name}, quantity: {quantity_str}")
    print(f"Parsed quantity: {parsed_quantity}")

# New function to adjust macro values based on quantity needed and serving size
def adjust_macros(macro_info, quantity_needed, serving_size):
    adjustment_factor = quantity_needed / serving_size
    adjusted_macros = {key: float(value) * adjustment_factor for key, value in macro_info.items() if key != 'serving_size'}
    return adjusted_macros

# Modified function to attach macros to ingredients and adjust based on serving size
def attach_macros(ingredients, macro_dict):
    enriched_ingredients = []
    for ingredient in ingredients:
        name, quantity_str = ingredient
        print(f"Processing ingredient: {name}, quantity: {quantity_str}")
        
        parsed_quantity = parse_quantity(quantity_str)
        print(f"Parsed quantity: {parsed_quantity}")
        
        if parsed_quantity:
            quantity_needed, unit = parsed_quantity
            normalized_name = normalize_name(name)
            print(f"Normalized name: {normalized_name}")
            
            if normalized_name in macro_dict:
                serving_info = macro_dict[normalized_name]
                print(f"Found serving info: {serving_info}")
                
                serving_size = float(serving_info['serving_size'])
                macros = {k: v for k, v in serving_info.items() if k != 'serving_size'}
                adjusted_macros = adjust_macros(macros, quantity_needed, serving_size)
                enriched_ingredients.append({'name': name, 'quantity': quantity_str, 'macros': adjusted_macros})
            else:
                print(f"Macros not found for: {normalized_name}")
                enriched_ingredients.append({'name': name, 'quantity': quantity_str, 'macros': 'Macros not found'})
        else:
            print(f"Could not parse quantity for: {quantity_str}")
            enriched_ingredients.append({'name': name, 'quantity': 'Unknown', 'macros': 'Macros not found'})
    return enriched_ingredients

# Assuming you have your scraped ingredients in a list:

# Compare and attach macros to the scraped ingredients
enriched_ingredients = attach_macros(scraped_ingredients, macro_dict)

# Print the results
for ingredient_info in enriched_ingredients:
    name = ingredient_info['name']
    quantity = ingredient_info['quantity']
    macros = ingredient_info['macros']
    if isinstance(macros, dict):
        macros_info = ', '.join([f"{key}: {value}" for key, value in macros.items()])
    else:
        macros_info = macros
    print(f'Ingredient: {name}, Quantity: {quantity}, Macros: {macros_info}')
