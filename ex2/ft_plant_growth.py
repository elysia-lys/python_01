class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.days_old = age

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days_old += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height: .1f}cm, {self.days_old} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)

    print("=== Garden Plant Growth ===")
    rose.show()

    starting_height = rose.height

    for day in range(1, 8):
        rose.grow()
        rose.age()

        print(f"=== Day {day} ===")
        rose.show()

    growth = rose.height - starting_height
    print(f"Growth this week: {growth:.1f}cm")
