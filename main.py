import toml
from collections import defaultdict

def main():
    """
    This script generates a consolidated grocery list based on recipe ingredients and
    serving sizes specified in two TOML files.

    The script performs the following steps:
    1. Loads two TOML files:
        - `recipes.toml`: Contains the ingredients and their quantities and units for each recipe.
        - `servings.toml`: Specifies the scaling factor (servings) for each recipe.
          If a recipe does not have a specified serving size, it defaults to 0, meaning
          that recipe will not be included in the grocery list.
    2. Multiplies the quantity of each ingredient by the serving size for each recipe.
    3. Aggregates the total quantity needed for each ingredient across all recipes, grouped by unit.

    Output:
    - Prints a header listing the recipes to be made, followed by a grocery list showing
      each ingredient with its total required amount and unit.
    - Saves the output to a "list.txt" file.

    Assumptions:
    - If a recipe's servings are not specified in `servings.toml`, it defaults to 0,
      effectively excluding that recipe from the grocery list.

    Dependencies:
    - The `toml` library for loading TOML files.
    - The `collections.defaultdict` class for aggregating ingredient totals.
    """

    # Load the TOML files
    with open("recipes.toml", encoding='utf-8') as f:
        recipes = toml.load(f)

    with open("servings.toml", encoding='utf-8') as f:
        servings_data = toml.load(f)

    # Dictionary to store the total ingredients required, grouped by unit
    grocery_list = defaultdict(lambda: defaultdict(float))

    # List to store the output content for writing to the file
    output_content = []

    # Header for recipes to be made
    output_content.append("Recipes to be made:\n")
    for recipe, ingredients in recipes.items():
        servings = servings_data.get(recipe, 0)
        if servings > 0:
            # Retrieve the URL if available
            url = ingredients.get("URL", "No URL provided")
            output_content.append(f"- {recipe} (Servings: {servings}kg)")
            output_content.append(f"  URL: {url}\n")
    output_content.append("\nGrocery List:")

    # Process each recipe
    for recipe, ingredients in recipes.items():
        servings = servings_data.get(recipe, 0)

        for ingredient, details in ingredients.items():
            # Skip metadata (e.g., URL or other non-dictionary entries)
            if not isinstance(details, dict):
                continue
            
            quantity = details.get("quantity", 0)
            unit = details.get("unit", "")

            # Sum the quantities, keeping units grouped
            grocery_list[ingredient][unit] += quantity * servings

    # Sort grocery list alphabetically by ingredient
    sorted_grocery_list = sorted(grocery_list.items())

    # Add the sorted grocery list to output content
    for ingredient, units in sorted_grocery_list:
        for unit, total_amount in units.items():
            output_content.append(f"{ingredient}: {round(total_amount)} {unit}")

    # Print the output to the console
    for line in output_content:
        print(line)

    # Save the output to a file
    with open("list.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(output_content))

# Run the main function
if __name__ == "__main__":
    main()
