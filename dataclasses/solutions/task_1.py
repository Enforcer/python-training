# Create a dataclass named TimeInterval with fields start_hour and end_hour (both int).
# Implement __post_init__ to perform two checks:
# - both hours are within the valid 24-hour range (0-23)
# - end_hour is greater (not equal) than start_hou
# If any of those conditions is not met, raise ValueError exception
from dataclasses import dataclass


@dataclass
class TimeInterval:
    start_hour: int
    end_hour: int

    def __post_init__(self) -> None:
        if self.start_hour < 0 or self.start_hour > 23:
            raise ValueError()
        elif self.end_hour < 0 or self.end_hour > 23:
            raise ValueError()
        elif self.end_hour < self.start_hour:
            raise ValueError()

TimeInterval(10, 12)  # should not raise exception
try:
    TimeInterval(20, 15)  # should raise exception
except ValueError:
    print("OK")
