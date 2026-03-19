def record_spell(spell_name: str, ingredients: str) -> str:
    # Late import avoids circular dependency at module import time.
    from .validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)

    if validation_result.endswith(" - VALID"):
        return f"Spell recorded: {spell_name} ({validation_result})"
    return f"Spell rejected: {spell_name} ({validation_result})"
