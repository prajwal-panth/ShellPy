from commands import CommandHandler

def main():
    print("Welcome to the Python Shell!")
    handler = CommandHandler()

    while True:
        try:
            user_input = input("\U0001F4BB >> ").strip()
            handler.execute(user_input)
            print()
        except KeyboardInterrupt:
            print("\nExiting Shell. Goodbye!")
            break

if __name__ == "__main__":
    main()