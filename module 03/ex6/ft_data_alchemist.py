import random


def ft_data_alchemist() -> None:
    print("=== Game Data Alchemist ===\n")
    names = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
             'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {names}")

    capitalized = [n.capitalize() for n in names]
    print(f"New list with all names capitalized: {capitalized}")

    only_capitalized = [n for n in names if n.istitle()]
    print(f"New list of capitalized names only: {only_capitalized}\n")

    score_dict = {n: random.randint(0, 999) for n in capitalized}
    print(f"Score dict: {score_dict}")

    average = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {average}")

    high_scores = {n: s for n, s in score_dict.items() if s > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_data_alchemist()
