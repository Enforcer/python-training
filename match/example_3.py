data = {"name": "Sebastian"}

match data:
    case {}:
        print("It's a dict!")
    case {"name": _}:
        print("That's a dict with 'name'")
    case _:
        print("No idea")
