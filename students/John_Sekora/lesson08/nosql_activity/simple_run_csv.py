"""
    Persistence
"""

import csv
import pprint
import utilities

log = utilities.configure_logger('default', '../logs/mongodb_script.log')


def run_csv():
    """
    write and read a csv
    """
    log.info("\n\n====")
    pokemon = [
        ('Charizard', 'dragon', 'red', 117.45, 123.04),
        ('Pikachu', 'rodent', 'yellow', 22.01, 1.32),
        ('Blastoise', 'dinosaur', 'blue', 45.99, 98.54),
        ('Mew', 'cat', 'white', 77.0, 24.2),
        ('Mewtwo', 'cat', 'white', 12.5, 345.4),
        ('Muk', 'slime', 'purple', 6.25, 21.6),
        ('Zapados', 'bird', 'yellow', 0.1, 54.37),
        ('Chansey', 'thing', 'pink', 89.71, 3.23),
        ('Venusaur', 'dinosaur', 'green', 89.71, 7.43),
        ('Ditto', 'thing', 'pink', 89.71, 54.58)
    ]

    log.info("Writing to csv file")
    with open('../data/pokemon_data.csv', 'w') as poke:
        poke_writer = csv.writer(poke)
        poke_writer.writerow(pokemon)

    log.info("Read csv file back")
    with open('../data/pokemon_data.csv', 'r') as poke:
        poke_reader = csv.reader(poke, delimiter=',', quotechar='"')
        for row in poke_reader:
            pprint.pprint(row)


if __name__ == "__main__":
    run_csv()
