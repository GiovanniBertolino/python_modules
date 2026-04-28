from pydantic import BaseModel, ValidationError, Field
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    valid_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2024, 1, 15, 10, 30)
        )
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    print(f"ID: {valid_station.station_id}")
    print(f"Name: {valid_station.name}")
    print(f"Crew: {valid_station.crew_size} people")
    print(f"Power: {valid_station.power_level}%")
    print(f"Oxygen: {valid_station.oxygen_level}%")
    if valid_station.is_operational:
        print("Status: Operational")
    else:
        print("Status: Not operational")
    print("\n========================================")

    print("Expected validation error:")
    try:
        invalid_station = SpaceStation(
            station_id="CHINA001",
            name="China Space Station",
            crew_size=25,
            power_level=45.5,
            oxygen_level=62.3,
            last_maintenance=datetime(2026, 2, 17, 3, 25)
            )
        print(f"Crew: {invalid_station.crew_size} people")
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
