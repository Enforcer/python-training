# Write the following sequence of bytes to a file using Pathlib.
# Try reading it back using read_text. See what happens.
# Do the same with another_bytes and observe result.

from pathlib import Path


some_bytes = b"The quick brown fox jumps over the lazy dog. Fox and dog are common themes in stories. The fox is fast!"
another_bytes = "żażółć gęślą jaźń".encode()

print("Writing bytes, then reading text")

file = Path(__file__).parent / "task_4_file"
file.write_bytes(some_bytes)
print(file.read_text())

print("Another bytes")

file.write_bytes(another_bytes)
print(file.read_text())
