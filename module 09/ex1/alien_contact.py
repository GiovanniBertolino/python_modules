from pydantic import BaseModel, ValidationError
from pydantic import Field, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_contact(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')
        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError(
                'Telepathic contact requires at least 3 witnesses'
                )
        if self.signal_strength > 7 and self.message_received is None:
            raise ValueError("Strong signals must include a received message")
        return self


def main() -> None:
    aliencontact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2026, 1, 15, 10, 30),
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="'Greetings from Zeta Reticuli'",
        is_verified=True
    )
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    print(f"ID: {aliencontact.contact_id}")
    print(f"Type: {aliencontact.contact_type.value}")
    print(f"Location: {aliencontact.location}")
    print(f"Signal: {aliencontact.signal_strength}/10")
    print(f"Duration: {aliencontact.duration_minutes} minutes")
    print(f"Witnesses: {aliencontact.witness_count}")
    print(f"Message: {aliencontact.message_received}")
    print("\n======================================")

    print("Expected validation error:")
    try:
        invalid_aliencontact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2026, 2, 13, 4, 34),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=9.1,
            duration_minutes=60,
            witness_count=1,
            )
        print(f"Witnesses: {invalid_aliencontact.witness_count}")
    except ValidationError as e:
        print(e.errors()[0]['ctx']['error'])


if __name__ == "__main__":
    main()
