import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    names = ['alice', 'bob', 'charlie', 'dylan']
    actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb',
               'swim', 'release', 'use']
    while True:
        yield (random.choice(names), random.choice(actions))


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        element = random.choice(events)
        events.remove(element)
        yield element


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    event_gen = gen_event()
    for i in range(1000):
        name, action = next(event_gen)
        print(f"Event {i}: Player {name} did action {action}")

    tuples_list = [next(event_gen) for _ in range(10)]
    print(f"Built list of 10 events: {tuples_list}")

    for event in consume_event(tuples_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {tuples_list}")


if __name__ == "__main__":
    ft_data_stream()
