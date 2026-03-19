def validate_ingredients(ingredients: str) -> str:
    lowered = ingredients.lower()
    valid_elements = ("fire", "water", "earth", "air")
    if any(element in lowered for element in valid_elements):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
