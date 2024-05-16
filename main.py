from config import config
from lib.recipe_normalizer import RecipeNormalizer


if __name__ == "__main__":
    recipe_directory = config.get("data_dir", "./data")
    normalizer = RecipeNormalizer()
    normalizer.process_directory(recipe_directory)
