"""
Wimbledon
Estimate: 60 minutes
Actual: 70 minutes
"""


def main():
    """Get and print the number of wins per champion and the countries of champions in alphabetical order"""
    filename = "wimbledon.csv"

    countries, names = get_champion_information(filename)
    champion_to_wins = populate_champion_to_wins(names)
    countries_alphabetical = reorder_countries(countries)

    # print results
    max_length = get_max_length_for_printing(champion_to_wins)
    print("Wimbledon Champions:")
    for name, wins in champion_to_wins.items():
        print(f"{name:{max_length}} - Wins: {wins:2}")
    print(f"These {len(countries_alphabetical.split(','))} countries have won Wimbledon:\n {countries_alphabetical}")


def get_max_length_for_printing(champion_to_wins):
    """Get length of longest player name"""
    keys = list(champion_to_wins.keys())
    max_length = max(len(key) for key in keys)
    return max_length


def reorder_countries(countries):
    """Get alphabetical order of countries"""
    countries_alphabetical = ', '.join(sorted(list({country: countries.count(country) for country in countries})))
    print(countries_alphabetical)
    return countries_alphabetical


def populate_champion_to_wins(names):
    """Count champion wins"""
    champion_to_wins = {name: names.count(name) for name in names}
    return champion_to_wins


def get_champion_information(filename):
    """Collect champion names and countries"""
    countries = []
    names = []
    # open file
    with open(filename, encoding="utf-8-sig") as in_file:
        in_file.readline()  # ignore header
        for line in in_file:
            parts = line.strip().split(',')
            countries += [parts[1]]
            names += [parts[2]]
    in_file.close()  # close file
    return countries, names


main()
