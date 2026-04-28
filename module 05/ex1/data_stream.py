import typing
from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self):
        self.data_list = []
        self.rank = 0
        self.total = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        return True

    @abstractmethod
    def ingest(self, data: Any) -> None:
        self.data_list.append(data)
        self.total += 1

    def output(self) -> tuple[int, str]:
        value = self.data_list.pop(0)
        current_rank = self.rank
        self.rank += 1
        return (current_rank, str(value))


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, int | float):
            return True
        if isinstance(data, list) and all(
            isinstance(e, (int, float)) for e in data
        ):
            return True
        return False

    def ingest(self, data: int | float | list[int] | list[float]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for element in data:
                    self.data_list.append(element)
                    self.total += 1
            else:
                self.data_list.append(data)
                self.total += 1
        else:
            raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and all(
            isinstance(element, str) for element in data
        ):
            return True
        return False

    def ingest(self, data: str | list) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for element in data:
                    self.data_list.append(element)
                    self.total += 1
            else:
                self.data_list.append(data)
                self.total += 1
        else:
            raise ValueError("Improper textual data")


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True
        if isinstance(data, list) and all(
            isinstance(element, dict) for element in data
        ):
            return True
        return False

    def ingest(self, data: dict | list[dict]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for element in data:
                    element1 = element['log_level']
                    element2 = element['log_message']
                    self.data_list.append(f"{element1}: {element2}")
                    self.total += 1
            else:
                self.data_list.append(data)
                self.total += 1
        else:
            raise ValueError("Improper log data")


class DataStream():
    def __init__(self):
        self.procs = []
        self.data_list = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.procs.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for e in stream:
            handled = False
            for proc in self.procs:
                if proc.validate(e):
                    proc.ingest(e)
                    handled = True
            if not handled:
                x = f"DataStream error - Can't process element in stream: {e}"
                print(x)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if self.procs == []:
            print("No processor found, no data\n")
        else:
            for proc in self.procs:
                a = " total "
                b = f" items processed, remaining {len(proc.data_list)}"
                if isinstance(proc, NumericProcessor):
                    print(f"Numeric Processor:{a}{proc.total}{b} on processor")
                if isinstance(proc, TextProcessor):
                    print(f"Text Processor:{a}{proc.total}{b} on processor")
                if isinstance(proc, LogProcessor):
                    print(f"Log Processor:{a}{proc.total}{b} on processor")


def data_stream() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()
    print("Registering Numeric Processor\n")
    data_stream.register_processor(NumericProcessor())
    log_data = [
        {
            'log_level': 'WARNING',
            'log_message': 'Telnet access! Use ssh instead'
        },
        {
            'log_level': 'INFO',
            'log_message': 'User wil isconnected'
        }
    ]
    data = ['Hello world', [3.14, -1, 2.71], log_data, 42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data}")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()
    print("\nRegistering other data processors")
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())
    print("Send the same batch again")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()
    consume = "Numeric 3, Text 2, Log 1"
    print(f"\nConsume some elements from the data processors: {consume}")
    for proc in data_stream.procs:
        if isinstance(proc, NumericProcessor):
            for i in range(3):
                proc.output()
        if isinstance(proc, TextProcessor):
            for i in range(2):
                proc.output()
        if isinstance(proc, LogProcessor):
            proc.output()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    data_stream()
