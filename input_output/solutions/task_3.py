# Write an infinite loop that will be accepting user's input using input() function
# When user enters 'END', use break to stop the loop.
#
# In every other case, open the file "task_3_file" in APPEND mode and write additional text, then close the file.
# Once user enters 'END', open the file again and read its contents, then print it.

while (data := input("Enter data: ").strip()) != "END":
    with open("task_3_file", "a") as f:
        f.write(data)

with open("task_3_file") as f:
    print(f.read())
