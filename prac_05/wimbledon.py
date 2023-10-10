"""
wimbledon
Estimate: 60 minutes
Actual: 70 minutes
"""


def main():
    """Get and print the number of wins per champion and the countries of champions in alphabetical order"""
    filename = "wimbledon.csv"
    countries = []
    names = []

    # open file
    with open(filename, encoding="utf-8-sig") as in_file:
        countries, names = get_champion_information(countries, in_file, names)

        champion_to_wins = get_number_of_wins_per_champion(names)
        countries_alphabetical = get_countries_in_alphabetical_order(countries)

        # print results
        max_length = get_max_length_for_printing(champion_to_wins)
        print("Wimbledon Champions:")
        for name, wins in champion_to_wins.items():
            print(f"{name:{max_length + 1}}- Wins: {wins:1}")
        print(f"These 12 countries have won Wimbledon:\n {countries_alphabetical}")


def get_max_length_for_printing(champion_to_wins):
    keys = list(champion_to_wins.keys())
    max_length = max(len(key) for key in keys)
    return max_length


def get_countries_in_alphabetical_order(countries):
    """Get alphabetical order of countries"""
    countries_alphabetical = ', '.join(sorted(list({country: countries.count(country) for country in countries})))
    return countries_alphabetical


def get_number_of_wins_per_champion(names):
    """Count champion wins"""
    champion_to_wins = {name: names.count(name) for name in names}
    return champion_to_wins


def get_champion_information(countries, in_file, names):
    """Collect champion names and countries"""
    in_file.readline()  # ignore header
    for line in in_file:
        parts = line.strip().split(',')
        countries += [parts[1]]
        names += [parts[2]]
    in_file.close()  # close file
    return countries, names


main()
