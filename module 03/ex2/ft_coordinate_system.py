import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        pos = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = pos.split(',')
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        converted = []
        error = False
        for part in parts:
            try:
                converted.append(float(part.strip()))
            except ValueError as e:
                print(f"Error on parameter '{part.strip()}': {e}")
                error = True
                break
        if not error:
            return (converted[0], converted[1], converted[2])


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    pos = get_player_pos()
    print(f"Got a first tuple: {pos}")
    print(f"It includes: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")
    dist = round(math.sqrt(pos[0]**2 + pos[1]**2 + pos[2]**2), 4)
    print(f"Distance to center: {dist}\n")
    print("Get a second set of coordinates")
    new_pos = get_player_pos()
    dist2 = round(math.sqrt(
        (pos[0] - new_pos[0])**2
        + (pos[1] - new_pos[1])**2
        + (pos[2] - new_pos[2])**2
    ), 4)
    print(f"Distance between the 2 sets of coordinates: {dist2}")


if __name__ == "__main__":
    ft_coordinate_system()
