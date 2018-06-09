"""This module will clean neo4j cloud db, then add and check initial data.

I tried to simplify the db as much as possible, so my db contain
the minimum data necessary to run the mailroom project:
    node label: Person; parameter: person_name (str)
    node label: {PersonName}Donation;
                         parameters: donataion (float),
                                     id (int) (this one helps to sort donations)
    relationship: HAS_DONATIONS,
          which is a link between a Person.person_name and {PersonName}Donation

This is a crude visual represenation of the current db structure:

                                            AlexSkrnDonation
                                            id: 0
                                            donation: 100.05
                                                  |
                                                  | HAS_DONATIONS
                                                  |

AlexSkrnDonation     HAS_DONATIONS             Person
id: 1                  ----------              person_name: Alex Skrn
donation: 1.05

                                                  |
                                                  | HAS_DONATIONS
                                                  |
                                            AlexSkrnDonation
                                            id: 2
                                            donation: 15.05


"""

# import login_database
import configparser
from pathlib import Path
from neo4j.v1 import GraphDatabase, basic_auth

# GETTING USER AND PASSWORD DATA FROM CONFIG FILE
config_file = Path(__file__).parent.parent / '.config/config'
config = configparser.ConfigParser()
config.read(config_file)
graphenedb_user = config["configuration"]["user"]
graphenedb_pass = config["configuration"]["pw"]
graphenedb_url = "bolt://hobby-bjkmfeabkpihgbkeddhdlgbl.dbs.graphenedb.com:24786"

driver = GraphDatabase.driver(graphenedb_url,
                              auth=basic_auth(graphenedb_user, graphenedb_pass))

"""
Initially I implemented helper functions to add / retrieve data to/from db,
but it turned out not to work because it seems that I can't pass
the session parameter to each of those functions.
I wanted it to look like this:

  def func(session, element):
      modify database

  with driver.session() as session:

      some_data = [some date]

      for element in some_data:
          func(session, element)
"""

def add_data():

    # The following line didn't work (see login_database.py for comments)
    # driver = login_database.login_neo4j_cloud()

    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")


    with driver.session() as session:

        #  I copied names from class repo and left them as is
        sample_donors = [('Bob', 'Jones'),
                         ('Nancy', 'Cooper'),
                         ('Alice', 'Cooper'),
                         ('Fred', 'Barnes'),
                         ('Mary', 'Evans'),
                         ('Marie', 'Curie'),
                         ]
        sample_gifts = [[79.05, 31, 68, 33, 31],
                        [22, 25.1, 62, 62, 95],
                        [10.1, 39, 33.33, 41, 29],
                        [13, 23, 17, 1, 88],
                        [21, 17, 34, 9, 88],
                        [27, 51, 24, 76, 23],
                        ]

        assert len(sample_donors) == len(sample_gifts)

        # Iterate over donor list and gift list and add data to db
        # E.g. Bob Jones BobJonesDonation [79.05, 31, 68, 33, 31]
        for i in range(len(sample_donors)):
            combined_person_name = f'{sample_donors[i][0]} {sample_donors[i][1]}'

            # Add single person
            try:
                cyph = "CREATE (n:Person {person_name:'%s'})" % (combined_person_name)
                session.run(cyph)
            except Exception as e:
                print(f"Error adding person {combined_person_name}: {e}")

            # Check single person exists
            try:
                cyph = """MATCH (p:Person {person_name: '%s'})
                      RETURN p.person_name as person_name
                   """ % (combined_person_name)
                result = session.run(cyph)
                for record in result:
                    print("Added: ", record['person_name'])
                    assert combined_person_name == record['person_name']
            except Exception as e:
                print(f"Error checking on person {combined_person_name}: {e}")

            node_name = f'{sample_donors[i][0]}{sample_donors[i][1]}Donation'

            # Add many donations
            try:
                for index, value in enumerate(sample_gifts[i]):
                    # Note: label names can't be parametrized in cypher
                    # so the following line won't work
                    # cyph = "CREATE (c:'%s' {donation: '%d'})" % (node, donation)
                    # hence string concatenation below
                    cyph = ("CREATE (c:" + node_name + "{donation: " + str(value)
                            + ", id: " + str(index) + "})")
                    session.run(cyph)

                cyph = ("MATCH (c:" + node_name + ")"
                        + "RETURN c.donation as donation" + "\n"
                        + "ORDER by c.id")
                result = session.run(cyph)
                print("Added donations  and checking if they are ok...")
                resulting_donations = []
                for record in result:
                    resulting_donations.append(record['donation'])
                print("Retreived:", resulting_donations, "Original:", sample_gifts[i])
                if resulting_donations == sample_gifts[i]:
                    print("list of donations is good")
            except Exception as e:
                print(f"Error adding donation with {sample_gifts[i]} {node_name}: {e}", e)

            # Create a relationship between the donor and gifts
            cyph = ("MATCH (a:Person), (b:" + node_name + ")" + "\n"
                    + "WHERE a.person_name = " + "'" + combined_person_name + "'" + "\n"
                    + "CREATE  (a)-[h:HAS_DONATIONS]->(b) " + "\n"
                    + "RETURN h" + "\n")
            session.run(cyph)

            # Check that the person has the right donations list
            try:
                # FIND ALL OF person'S DONATIONS
                cyph = """
                  MATCH (p:Person {person_name: '%s'})
                        -[:HAS_DONATIONS]->(personDonations)
                  RETURN personDonations
                  ORDER by personDonations.id
                  """ % (combined_person_name)
                result = session.run(cyph)
                a_list_gifts = []
                for rec in result:
                    for donation in rec.values():
                        a_list_gifts.append(float(donation['donation']))
                print("Retreiving donations by person name...")
                print("Retrived:", a_list_gifts, "Actual:", sample_gifts[i])
                if a_list_gifts == sample_gifts[i]:
                    print(" Retrived donations match actual ones.")

            except Exception as e:
                print(f"Error getting donations for {combined_person_name}: {e}")


def see_data_in_db():
    """Print out people and donations from the db as a dict."""
    # Step 1: Get people names from db.
    # Step 2: Get donations for each person
    # Step 3: Convert into a dict
    with driver.session() as session:
        # Step 1:
        try:
            people_names = []
            cyph = """MATCH (p:Person)
                      RETURN p.person_name as person_name
                      """
            result = session.run(cyph)
            for donor in result:
                people_names.append(donor['person_name'])
            # print(people_names)
        except Exception as e:
            print("Failed to query for people in the db: ", e)

        # Step 2:
        try:
            people_donations = []
            for name in people_names:
                cyph = """
                  MATCH (p:Person {person_name: '%s'})
                        -[:HAS_DONATIONS]->(personDonations)
                  RETURN personDonations
                  ORDER by personDonations.id
                  """ % (name)
                result = session.run(cyph)
                a_list_gifts = []
                for rec in result:
                    for donation in rec.values():
                        a_list_gifts.append(float(donation['donation']))
                people_donations.append(a_list_gifts)
            # print(people_donations)
        except Exception as e:
            print("Failed to query for donations in the db: ", e)

        # Step 3:
        dict_people_gifts = dict(zip(people_names, people_donations))
        print(dict_people_gifts)


if __name__ == "__main__":
    add_data()
    see_data_in_db()
