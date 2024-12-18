"""Wimbledon Mens Champions, get statistics of champions and their countries."""

# Estimated time: 2.5 hours
# Actual time: 3.5 hours

FILENAME = "wimbledon.csv"
COUNTRY = 1
CHAMPION = 2


def main():
    """Process file returning Wimbledon champions and countries."""
    records = get_records(FILENAME)
    champion_count, unique_countries = process_data(records)
    display_results(champion_count, unique_countries)


def get_records(filename):
    """Get records from file."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        records = [line.strip().split(",") for line in in_file]
    return records


def process_data(records):
    """Get champion count."""
    champion_count = {}
    countries = {record[COUNTRY] for record in records}
    for record in records:
        champion_count[record[CHAMPION]] = champion_count.get(record[CHAMPION], 0) + 1
    return champion_count, countries


def display_results(champion_count, countries):
    """Displays champions and countries."""
    print("Wimbledon Champions:")
    for champion, count in champion_count.items():
        print(f"{champion} {count}")
    sorted_countries = sorted(countries)
    print(f"\nThese {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))


main()
