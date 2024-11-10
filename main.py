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
    - Prints a grocery list showing each ingredient with its total required amount and unit.

    Assumptions:
    - If a recipe's servings are not specified in `servings.toml`, it defaults to 0,
      effectively excluding that recipe from the grocery list.

    Dependencies:
    - The `toml` library for loading TOML files.
    - The `collections.defaultdict` class for aggregating ingredient totals.

    TOML File Structure:
    - `recipes.toml` example:
        [recipe1]
        ingredient1 = { quantity = 2, unit = "kg" }
        ingredient2 = { quantity = 1, unit = "unid" }

    - `servings.toml` example:
        [recipe1]
        servings = 4
    """

    # Load the TOML files
    with open("recipes.toml", encoding='utf-8') as f:
        recipes = toml.load(f)

    with open("servings.toml", encoding='utf-8') as f:
        servings_data = toml.load(f)

    # Dictionary to store the total ingredients required, grouped by unit
    grocery_list = defaultdict(lambda: defaultdict(float))

    # Process each recipe
    for recipe, ingredients in recipes.items():
        servings = servings_data.get(recipe, {}).get("servings", 0)

        for ingredient, details in ingredients.items():
            quantity = details.get("quantity", 0)
            unit = details.get("unit", "")
            
            # Sum the quantities, keeping units grouped
            grocery_list[ingredient][unit] += quantity * servings

    # Print the grocery list
    print("Grocery List:")
    for ingredient, units in grocery_list.items():
        for unit, total_amount in units.items():
            print(f"{ingredient}: {round(total_amount)} {unit}")

# Run the main function
if __name__ == "__main__":
    main()
