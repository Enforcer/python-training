data = {"name": "Sebastian"}

match data:
    case {"name": _}:
        print("That's a dict with 'name'")
    case {}:
        print("It's a dict!")
    case _:
        print("No idea")
