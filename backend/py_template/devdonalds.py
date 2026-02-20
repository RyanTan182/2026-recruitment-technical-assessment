from dataclasses import dataclass
from typing import List, Dict, Union
from flask import Flask, request, jsonify
import re

# ==== Type Definitions, feel free to add or modify ===========================
@dataclass
class CookbookEntry:
	name: str

@dataclass
class RequiredItem():
	name: str
	quantity: int

@dataclass
class Recipe(CookbookEntry):
	required_items: List[RequiredItem]

@dataclass
class Ingredient(CookbookEntry):
	cook_time: int


# =============================================================================
# ==== HTTP Endpoint Stubs ====================================================
# =============================================================================
app = Flask(__name__)

# Store your recipes here!
cookbook = {}

# Task 1 helper (don't touch)
@app.route("/parse", methods=['POST'])
def parse():
	data = request.get_json()
	recipe_name = data.get('input', '')
	parsed_name = parse_handwriting(recipe_name)
	if parsed_name is None:
		return 'Invalid recipe name', 400
	return jsonify({'msg': parsed_name}), 200

# [TASK 1] ====================================================================
# Takes in a recipeName and returns it in a form that 
def parse_handwriting(recipeName: str) -> Union[str | None]:
	recipeName = recipeName.replace('-', ' ').replace('_', ' ')
	recipeName = re.sub(r'[^a-zA-Z\s]', '', recipeName)
	recipeName = recipeName.title()
	recipeName = " ".join(recipeName.split())
	if len(recipeName) <= 0:
		return None
	return recipeName


# [TASK 2] ====================================================================
# Endpoint that adds a CookbookEntry to your magical cookbook
@app.route('/entry', methods=['POST'])
def create_entry():
	data = request.get_json()
	# type can only be "recipe" or "ingredient".
	if data.get('type') not in ['recipe', 'ingredient']:
		return 'Invalid entry type', 400

	# entry names must be unique
	if data.get('name') in cookbook:
		return 'Entry already exists', 400

	if data.get('type') == 'recipe':
		# Recipe requiredItems can only have one element per name.
		for item in data.get('requiredItems'):
			if item.get('quantity') <= 0:
				return 'Invalid quantity', 400
	else:  # data.get('type') == 'ingredient'
		# cookTime can only be greater than or equal to 0
		if data.get('cookTime') < 0:
			return 'Invalid cook time', 400
	cookbook[data.get('name')] = data
	return '', 200
# [TASK 3] ====================================================================
# Endpoint that returns a summary of a recipe that corresponds to a query name
@app.route('/summary', methods=['GET'])
def summary():
	name = request.args.get('name')
	
	# Check if recipe exists
	if name not in cookbook:
		return 'Recipe not found', 400
	
	# Check if it's a recipe
	if cookbook[name].get('type') != 'recipe':
		return 'Ingredient, not a recipe', 400
	
	# Get recipe details (returns None if a required item is missing)
	details = get_recipe_details(name)
	if details is None:
		return 'Recipe contains items not in cookbook', 400
	
	# Convert base_ingredients dict to list of RequiredItem format
	ingredients_list = [{'name': ing_name, 'quantity': ing_qty} for ing_name, ing_qty in details['ingredients'].items()]
	
	return jsonify({'name': name, 'cookTime': details['cookTime'], 'ingredients': ingredients_list}), 200

# Helper function to recursively get base ingredients and cook time
# Returns None if any required item is missing from cookbook
def get_recipe_details(name: str, quantity: int = 1):
	if name not in cookbook:
		return None
	
	# If it's an ingredient, return its cook time and itself
	if cookbook[name].get('type') == 'ingredient':
		return {'cookTime': cookbook[name].get('cookTime') * quantity, 'ingredients': {name: quantity}}
	
	# Recursive every item in requiredItems
	total_cookTime = 0
	ingredients = {}
	
	# Loop thru each item
	for item in cookbook[name].get('requiredItems', []):
		item_name = item.get('name')
		item_quantity = item.get('quantity')

		if item_name not in cookbook:
			return None

		if cookbook[item_name].get('type') == 'ingredient':
			total_cookTime += cookbook[item_name].get('cookTime') * item_quantity * quantity
			ingredients[item_name] = ingredients.get(item_name, 0) + (item_quantity * quantity)
		else:
			result = get_recipe_details(item_name, item_quantity * quantity)
			if result is None:
				return None
			total_cookTime += result['cookTime']
			for ing_name, ing_quantity in result['ingredients'].items():
				ingredients[ing_name] = ingredients.get(ing_name, 0) + ing_quantity
	
	return {'cookTime': total_cookTime, 'ingredients': ingredients}


# =============================================================================
# ==== DO NOT TOUCH ===========================================================
# =============================================================================

if __name__ == '__main__':
	app.run(debug=True, port=8080)
