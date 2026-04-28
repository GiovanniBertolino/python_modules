import typing
from typing import Any, Protocol
from abc import ABC, abstractmethod


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.procs:
            data = []
            for i in range(nb):
                if proc.data_list:
                    data.append(proc.output())
            plugin.process_output(data)


class CSVExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [e[1] for e in data]
        # liste de tuples
        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        elements = [f'"item_{e[0]}": "{e[1]}"' for e in data]
        print("JSON Output:")
        print("{" + ", ".join(elements) + "}")


def data_pipeline() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()
    print("Registering Processors\n")
    data_stream.register_processor(NumericProcessor())
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())
    log_data1 = [
        {
            'log_level': 'WARNING',
            'log_message': 'Telnet access! Use ssh instead'
        },
        {
            'log_level': 'INFO',
            'log_message': 'User wil isconnected'
        }
    ]
    data1 = ['Hello world', [3.14, -1, 2.71], log_data1, 42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data1}\n")
    data_stream.process_stream(data1)
    data_stream.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CSVExportPlugin())
    print()
    data_stream.print_processors_stats()
    log_data2 = [
        {
            'log_level': 'ERROR',
            'log_message': '500 server crash'
        },
        {
            'log_level': 'NOTICE',
            'log_message': 'Certificateexpires in 10 days'
        }
    ]
    data2 = [
            21,
            ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
            log_data2,
            [32, 42, 64, 84, 128, 168],
            'World hello'
    ]
    print(f"\nSend another batch of data: {data2}\n")
    data_stream.process_stream(data2)
    data_stream.print_processors_stats()
    print("Send 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JSONExportPlugin())
    print()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    data_pipeline()
