def healing_potion() -> str:
    from .elements import create_fire, create_water

    fire_result = create_fire()
    water_result = create_water()
    return (
        "Healing potion brewed with "
        f"{fire_result} and {water_result}"
    )


def strength_potion() -> str:
    from .elements import create_earth, create_fire

    earth_result = create_earth()
    fire_result = create_fire()
    return (
        "Strength potion brewed with "
        f"{earth_result} and {fire_result}"
    )


def invisibility_potion() -> str:
    from .elements import create_air, create_water

    air_result = create_air()
    water_result = create_water()
    return (
        "Invisibility potion brewed with "
        f"{air_result} and {water_result}"
    )


def wisdom_potion() -> str:
    from .elements import create_air, create_earth, create_fire, create_water

    all_four_results = ", ".join(
        [
            create_fire(),
            create_water(),
            create_earth(),
            create_air(),
        ]
    )
    return (
        "Wisdom potion brewed with all elements: "
        f"{all_four_results}"
    )
