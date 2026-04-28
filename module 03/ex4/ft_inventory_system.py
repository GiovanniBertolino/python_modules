import sys


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        parts = arg.split(':')
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, value = parts
        if name in inventory.keys():
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            quantity = int(value)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue
        inventory.update({name: quantity})

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")
    for item, quantity in inventory.items():
        print(f"Item {item} represents {round(quantity / total * 100, 1)}%")

    max_qty = max(inventory.values())
    min_qty = min(inventory.values())
    for item, qty in inventory.items():
        if qty == max_qty:
            print(f"Item most abundant: {item} with quantity {qty}")
            break
    for item, qty in inventory.items():
        if qty == min_qty:
            print(f"Item least abundant: {item} with quantity {qty}")
            break

    inventory.update({'magic_item': 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()
