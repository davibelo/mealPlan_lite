import toml
from collections import defaultdict

def main():
    """
    This script generates a consolidated grocery list based on recipe ingredients and
    serving sizes specified in two TOML files.

    The script performs the following steps:
    1. Loads two TOML files:
        - `recipes.toml`: Contains the ingredients and their quantities for each recipe.
        - `servings.toml`: Specifies the scaling factor (servings) for each recipe.
          If a recipe does not have a specified serving size, it defaults to 0, meaning
          that recipe will not be included in the grocery list.
    2. Multiplies the quantity of each ingredient by the serving size for each recipe.
    3. Aggregates the total quantity needed for each ingredient across all recipes.

    Output:
    - Prints a grocery list showing each ingredient with its total required amount.

    Assumptions:
    - If a recipe's servings are not specified in `servings.toml`, it defaults to 0,
      effectively excluding that recipe from the grocery list.

    Dependencies:
    - The `toml` library for loading TOML files.
    - The `collections.defaultdict` class for aggregating ingredient totals.

    TOML File Structure:
    - `recipes.toml` example:
        [recipe1]
        ingredient1 = quantity
        ingredient2 = quantity

    - `servings.toml` example:
        [recipe1]
        servings = scale_factor
    """

    # Load the TOML files
    with open("recipes.toml", encoding='utf-8') as f:
        recipes = toml.load(f)

    with open("servings.toml", encoding='utf-8') as f:
        servings_data = toml.load(f)

    # Dictionary to store the total ingredients required
    grocery_list = defaultdict(float)

    # Process each recipe
    for recipe, ingredients in recipes.items():
        servings = servings_data.get(recipe, {}).get("servings", 0)

        for ingredient, amount in ingredients.items():
            grocery_list[ingredient] += amount * servings

    # Print the grocery list
    print("Grocery List:")
    for ingredient, total_amount in grocery_list.items():
        print(f"{ingredient}: {total_amount}")

# Run the main function
if __name__ == "__main__":
    main()
