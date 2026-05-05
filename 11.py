def parse_error_value(line):
    marker = "Xerror:"
    index = line.find(marker)
    if index == -1:
        return None

    value_part = line[index + len(marker):].strip()
    if not value_part:
        return None

    try:
        return float(value_part)
    except ValueError:
        return None


def process_lines(lines):
    error_values = []

    for line in lines:
        value = parse_error_value(line)
        if value is not None:
            error_values.append(value)

    total = sum(error_values)
    count = len(error_values)
    average = total / count if count else 0.0

    print(f"Error lines found = {count}")
    if count:
        print("Error values:")
        for value in error_values:
            print(f"{value}")
        print(f"Total = {total}")
        print(f"Average = {average}")
