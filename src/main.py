def greet(name):
    return f"Hello, {name}!"


def main():
    name = input("Enter your name: ")

    if name.strip():
        message = greet(name)
        print(message)
    else:
        print("Name cannot be empty.")


if __name__ == "__main__":
    main()