from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self):
        self.data_list = []
        self.rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        return True

    @abstractmethod
    def ingest(self, data: Any) -> None:
        self.data_list.append(data)

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
            else:
                self.data_list.append(data)
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
            else:
                self.data_list.append(data)
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
            else:
                self.data_list.append(data)
        else:
            raise ValueError("Improper log data")


def data_processor() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    number = 42
    str1 = "Hello"
    str2 = "foo"
    data1 = [1, 2, 3, 4, 5]
    data2 = ['Hello', 'Nexus', 'World']
    data3 = [{
        'log_level': 'NOTICE', 'log_message': 'Connection to server'}, {
        'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print("Testing Numeric Processor...")
    print(f" Trying to validate input '{number}': {numeric.validate(number)}")
    print(f" Trying to validate input '{str1}': {numeric.validate(str1)}")
    print(f" Test invalid ingestion of string '{str2}'", end="")
    print(" without prior validation:")
    try:
        numeric.ingest(str2)  # type: ignore
    except ValueError as e:
        print(f" Got exception: {e}")
    print(f" Processing data: {data1}")
    numeric.ingest(data1)
    print(" Extracting 3 values...")
    for i in range(3):
        rank, value = numeric.output()
        print(f" Numeric value {rank}: {value}")
    print("\nTesting Text Processor...")
    print(f" Trying to validate input '{number}': {text.validate(number)}")
    print(f" Processing data: {data2}")
    text.ingest(data2)
    print(" Extracting 1 value...")
    rank, value = text.output()
    print(f" Text value {rank}: {value}\n")
    print("Testing Log Processor...")
    print(f" Trying to validate input '{str1}': {log.validate(str1)}")
    print(f" Processing data: {data3}")
    log.ingest(data3)
    print(" Extracting 2 values...")
    for i in range(2):
        rank, value = log.output()
        print(f" Log entry {rank}: {value}")


if __name__ == "__main__":
    data_processor()
