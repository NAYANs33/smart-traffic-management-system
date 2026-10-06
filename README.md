# AI Traffic Signal System

A beginner-friendly Python console program that simulates one traffic-light
cycle. Enter the number of cars to calculate how long the green light stays on.

## Traffic-light timings

- **Green:** 10 seconds when there are fewer than 5 cars.
- **Green:** `10 + (cars - 5) * 2` seconds when there are 5 or more cars.
- **Green maximum:** 30 seconds.
- **Yellow:** 3 seconds.
- **Red:** 30 seconds.

The program accepts only non-negative whole numbers. It asks again if the
input is invalid.

## Requirements

- Python 3
- No extra packages

## Run

Open a terminal in the project folder and run:

```bash
python traffic.py
```

On Windows, you can also run:

```powershell
py traffic.py
```

Enter the number of cars when prompted. The program then displays the green,
yellow, and red countdowns.

## Example

With 6 cars, the green time is:

```text
10 + (6 - 5) * 2 = 12 seconds
```

## Project files

- `traffic.py` - traffic signal simulation
- `README.md` - project documentation

## Disclaimer

This is a console-based educational simulation. It does not connect to or
control real traffic lights.
