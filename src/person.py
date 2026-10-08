class Person:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")

        if not name.strip():
            raise ValueError("Name cannot be empty.")

        self.name = name.strip()

    def introduce(self):
        return f"My name is {self.name}."