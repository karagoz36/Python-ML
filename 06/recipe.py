cookbook = {
	"Sandwich": {"ingredients": ["bread", "cheese", "tomatoes"], "meal": "lunch", "prep_time": 10},
	"Cake": {"ingredients": ["flour", "sugar", "eggs"], "meal": "dessert", "prep_time": 60},
	"Salad": {"ingredients": ["avocado", "arugula", "tomatoes", "spinach"], "meal": "lunch", "prep_time": 15},
}

def print_recipes():
	if not cookbook:
		print("The cookbook is empty!")
	else:
		print("Available recipes:")
		for recipe in cookbook:
			print(f"- {recipe}")

def print_details(name):
	recipe = cookbook.get(name)
	if recipe:
		print(f"Recipe for {name}:")
		print(f"Ingredients list: {recipe['ingredients']}")
		print(f"To be eaten or {recipe['meal']}.")
		print(f"Takes {recipe['prep_time']} minutes of cooking.")
	else:
		print("Recipe not found.")

def delete_recipe(name):
	if name in cookbook:
		del cookbook[name]
		print(f"{name} has been deleted.")
	else:
		print("Recipe not found.")

def add_recipe():
	name = input("Enter the name of the recipe: ")
	if name in cookbook:
		print("This recipe already exists.")
		return
	ingredients = input("Enter ingredients (comma separated): ").split(", ")
	meal_type = input("Enter meal type: ")
	try:
		prep_time = int(input("Enter preparation time (minutes): "))
	except ValueError:
		print("Invalid preparation time. Must be an integer.")
		return

	cookbook[name] = {"ingredients" : ingredients, "meal" : meal_type, "prep_time" : prep_time}
	print(f"{name} has been added to the cookbook.")

def display_menu():
	print("\nWelcome to the Python Cookbook!")
	print("List of available options:")
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit")

def main():
	display_menu()

	while True:
		choice = input("Please select an option: ")
		if choice == "1":
			add_recipe()
		elif choice == "2":
			recipe_name = input("Enter the name of the recipe to delete: ")
			delete_recipe(recipe_name)
		elif choice == "3":
			recipe_name = input("Enter the name of the recipe to get its details: ")
			print_details(recipe_name)
		elif choice == "4":
			print_recipes()
		elif choice == "5":
			print("Cookbook closed. Goodbye!")
			break
		else:
			print("Sorry, this option does not exist.")

if __name__ == "__main__":
	main()
