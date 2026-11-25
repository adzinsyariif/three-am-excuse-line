import os

LINE = "Denied. You only wake me at 3 AM when you're lonely and leveraged — I'm your hardware wallet, not your booty call."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
