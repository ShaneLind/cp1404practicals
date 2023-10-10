"""
wimbledon
Estimate: 60 minutes
Actual: ?? minutes
"""

filename = "wimbledon.csv"
with open(filename, encoding="utf-8-sig") as in_file:
    try:
        line = in_file.readline(100)
        champion_info = line.strip().split(',')
    except ValueError:
        print("Invalid contents on wimbledon.csv")
    except FileNotFoundError:
        print("wimbledon.csv not found")
    else:
        in_file.close()

print(champion_info[1:3])

