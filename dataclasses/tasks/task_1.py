# Create a dataclass named TimeInterval with fields start_hour and end_hour (both int).
# Implement __post_init__ to perform two checks:
# - both hours are within the valid 24-hour range (0-23)
# - end_hour is greater (not equal) than start_hou
# If any of those conditions is not met, raise ValueError exception


TimeInterval(10, 12)  # should not raise exception
try:
    TimeInterval(20, 15)  # should raise exception
except ValueError:
    print("OK")
