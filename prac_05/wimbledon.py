"""
wimbledon
Estimate: 60 minutes
Actual: 70 minutes
"""

filename = "wimbledon.csv"
countries = []
names = []

# open file
with open(filename, encoding="utf-8-sig") as in_file:
    in_file.readline()  # ignore header

    # collect champion names and countries
    for line in in_file:
        # print(line)
        parts = line.strip().split(',')
        # print(parts)
        country = parts[1]
        name = parts[2]
        # print(country, name)
        countries += [parts[1]]
        names += [parts[2]]
    # print(countries)
    # print(names)

    # count champion wins
    champion_to_wins = {name: names.count(name) for name in names}
    # find alphabetical order of countries
    countries_alphabetical = ', '.join(sorted(list({country: countries.count(country) for country in countries})))

    # print results
    keys = list(champion_to_wins.keys())
    max_length = max(len(key) for key in keys)
    print("Wimbledon Champions:")
    for name, wins in champion_to_wins.items():
        print(f"{name:{max_length + 1}}- Wins: {wins:1}")
    print(f"These 12 countries have won Wimbledon:\n {countries_alphabetical}")
in_file.close() # close file
