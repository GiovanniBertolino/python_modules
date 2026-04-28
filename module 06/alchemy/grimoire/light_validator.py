def validate_ingredients(ingredients: str) -> str:
    allowed = ["earth", "air", "fire", "water"]
    for e in allowed:
        if e.lower() in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
