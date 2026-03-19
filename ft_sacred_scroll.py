import alchemy
import alchemy.elements


def test_package_level_access(function_name: str) -> None:
    try:
        func = getattr(alchemy, function_name)
        print(f"alchemy.{function_name}(): {func()}")
    except AttributeError:
        print(f"alchemy.{function_name}(): AttributeError - not exposed")


if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(
        f"alchemy.elements.create_water(): {alchemy.elements.create_water()}"
    )
    print(
        f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}"
    )
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    test_package_level_access("create_fire")
    test_package_level_access("create_water")
    test_package_level_access("create_earth")
    test_package_level_access("create_air")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")
