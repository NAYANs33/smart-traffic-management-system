import time


def calculate_green_time(cars: int) -> int:
    """Return the green-light duration, capped at 30 seconds."""
    if cars < 5:
        return 10
    return min(30, 10 + (cars - 5) * 2)


def countdown(light: str, message: str, duration: int) -> None:
    print(f"\n{light} {message}")
    for seconds in range(duration, 0, -1):
        print(f"{message.split()[0].capitalize()}: {seconds} seconds remaining")
        time.sleep(1)


def main() -> None:
    print("====================================")
    print("      AI TRAFFIC SIGNAL SYSTEM")
    print("====================================")
    while True:
        try:
            cars = int(input("Enter number of cars: "))
            if cars < 0:
                print("Please enter a non-negative whole number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    green_time = calculate_green_time(cars)
    print(f"\nCars detected: {cars}")
    print(f"Green light time: {green_time} seconds")

    countdown("[GREEN]", "GREEN LIGHT - GO", green_time)
    countdown("[YELLOW]", "YELLOW LIGHT - SLOW", 3)
    countdown("[RED]", "RED LIGHT - STOP", 30)

    print("\n====================================")
    print("       TRAFFIC CYCLE COMPLETE")
    print("====================================")


if __name__ == "__main__":
    main()