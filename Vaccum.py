class VacuumCleaner:
    def __init__(self):
        self.location = (0, 0)  # Initial location of the vacuum cleaner
        self.clean_count = 0    # Counter for cleaned cells

    def clean(self):
        print(f"Cleaning cell {self.location}")
        self.clean_count += 1

    def move_left(self):
        print("Moving left")
        self.location = (self.location[0], self.location[1] - 1)

    def move_right(self):
        print("Moving right")
        self.location = (self.location[0], self.location[1] + 1)

    def move_up(self):
        print("Moving up")
        self.location = (self.location[0] - 1, self.location[1])

    def move_down(self):
        print("Moving down")
        self.location = (self.location[0] + 1, self.location[1])

def main():
    cleaner = VacuumCleaner()
    grid = [
        [1, 0],
        [0, 1]
    ]

    while cleaner.clean_count < 4:
        row, col = cleaner.location
        if grid[row][col] == 1:
            cleaner.clean()
        if col < 1:
            cleaner.move_right()
        else:
            cleaner.move_left()
        if row < 1:
            cleaner.move_down()
        else:
            cleaner.move_up()

if __name__ == "__main__":
    main()
