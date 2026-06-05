from operations import add


def main():
    print("Calculator. Commands: add <num> <num> | quit")
    while True:
        line = input("> ").strip()
        if line == "quit":
            break
        parts = line.split()
        if len(parts) != 3:
            print("Usage: <operation> <num1> <num2>")
            continue
        op, a, b = parts[0], parts[1], parts[2]
        try:
            a, b = float(a), float(b)
        except ValueError:
            print("Error: both arguments must be numbers")
            continue
        if op == "add":
            print(add(a, b))
        else:
            print(f"Unknown operation: {op}")


if __name__ == "__main__":
    main()
