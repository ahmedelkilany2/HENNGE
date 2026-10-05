import sys


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    test_cases = int(lines[0].strip())
    results = []
    line_index = 1

    for _ in range(test_cases):
        count = int(lines[line_index].strip())
        line_index += 1

        values = list(map(int, lines[line_index].split()))
        line_index += 1

        if len(values) != count:
            results.append("-1")
        else:
            results.append(str(sum(value ** 4 for value in values if value <= 0)))

    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    main()
