from pydantic import BaseModel, ValidationError
from pydantic import Field, model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        has_leader = any(
            m.rank in (Rank.captain, Rank.commander) for m in self.crew
            )
        if not has_leader:
            raise ValueError('Must have at least one Commander or Captain')
        experienced = sum(1 for m in self.crew if m.years_experience >= 5)
        if self.duration_days > 365 and experienced / len(self.crew) < 0.5:
            raise ValueError(
                'Long missions (> 365 days) need 50% '
                'experienced crew (5+ years)'
                )
        if not all(m.is_active for m in self.crew):
            raise ValueError('All crew members must be active')
        return self


def main() -> None:
    sarah = CrewMember(
        member_id="test1",
        name="Sarah Connor",
        rank=Rank.commander,
        age=45,
        specialization="Mission Command",
        years_experience=10
        )
    john = CrewMember(
        member_id="test2",
        name="John Smith",
        rank=Rank.lieutenant,
        age=35,
        specialization="Navigation",
        years_experience=6
        )
    alice = CrewMember(
        member_id="test3",
        name="Alice Johnson",
        rank=Rank.officer,
        age=26,
        specialization="Engineering",
        years_experience=3
        )
    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2026, 1, 15, 10, 30),
        duration_days=900,
        crew=[sarah, john, alice],
        budget_millions=2500.0
        )

    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    for m in valid_mission.crew:
        print(f"- {m.name} ({m.rank.value}) - {m.specialization}")
    print("\n=========================================")
    print("Expected validation error:")
    try:
        sarah_error = CrewMember(
            member_id="test1",
            name="Sarah Connor",
            rank=Rank.cadet,
            age=45,
            specialization="Mission Command",
            years_experience=10
            )
        invalid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 1, 15, 10, 30),
            duration_days=900,
            crew=[sarah_error],
            budget_millions=2500.0
            )
        print(f"{invalid_mission.mission_name}")
    except ValidationError as e:
        message = str(e.errors()[0]['ctx']['error'])
        print(f"Mission {message[0].lower() + message[1:]}")


if __name__ == "__main__":
    main()
