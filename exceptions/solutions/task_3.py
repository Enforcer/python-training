while True:
    try:
        data = input("Give me your name!").strip()
        if data:
            print(f"Oh, finally - nice to meet you {data}!")
            break
    except KeyboardInterrupt:
        print("\nYou're not going out!")
