# Recipe Ingredient Parser

## Overview
The Recipe Ingredient Parser is a tool for extracting and structuring ingredient information from online recipes. It automates the conversion of recipe ingredients from text to a structured format, useful for applications like creating shopping lists or analyzing recipes.

## Key Features
- **Ingredient Extraction**: Scrapes web pages to collect ingredients lists.
- **Text Processing**: Parses and cleans ingredient text data.
- **Unicode Handling**: Converts Unicode fractions to human-readable fractions.
- **Structured Output**: Splits ingredients into quantity and name for easy use.

## How It Works
- The tool scrapes a recipe webpage, collects ingredient data, and then processes the text to split ingredients into structured data: quantity and ingredient name.

## Technologies Used
- Python for programming.
- `requests` and `BeautifulSoup` for web scraping.
- Regular expressions for text parsing.

## Usage
1. Run the scraper to collect ingredients from a recipe URL.
2. Process the list with the parser to get structured ingredient data.

## Conclusion
This parser simplifies the task of turning plain-text ingredients from recipes into a structured format, allowing for easier manipulation and analysis of culinary data.

