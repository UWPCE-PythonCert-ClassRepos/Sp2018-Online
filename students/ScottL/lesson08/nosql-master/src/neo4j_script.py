"""
    neo4j example
"""

# -------------------------------------------------#
# Title: neo4j_script.py
# Dev: Scott Luse
# Changelog:
# 0/02/2018: added new people and colors to database
# setup favorite color associations
# save out Pickle and Shelve
# -------------------------------------------------#

import login_database
import utilities
import pickle
import shelve

log = utilities.configure_logger('default', '../logs/neo4j_script.log')


def run_example():

    log.info('Step 1: First, clear the entire database, so we can start over')
    log.info("Running clear_all")

    driver = login_database.login_neo4j_cloud()
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")

    log.info("Step 2: Add a few people")

    with driver.session() as session:

        log.info('Adding a few Person nodes')
        log.info('The cyph language is analagous to sql for neo4j')
        for first, last in [('Bob', 'Jones'),
                            ('Nancy', 'Cooper'),
                            ('Alice', 'Cooper'),
                            ('Fred', 'Barnes'),
                            ('Mary', 'Evans'),
                            ('Marie', 'Curie'),
                            ('Peter', 'Parker'),
                            ('MaryJane', 'Watson'),
                            ('Spider', 'Man'),
                            ]:
            cyph = "CREATE (n:Person {first_name:'%s', last_name: '%s'})" % (
                first, last)
            session.run(cyph)

        log.info("Step 3: Get all of people in the DB:")
        cyph = """MATCH (p:Person)
                  RETURN p.first_name as first_name, p.last_name as last_name
                """
        result = session.run(cyph)
        print("People in database:")
        for record in result:
            print(record['first_name'], record['last_name'])

        # Add new colors
        log.info('Adding a few Color nodes...')
        for color in [('Blue'),
                      ('Red'),
                      ('Green'),
                      ('Yellow'),
                      ('Orange'),
                      ]:
            cyph = "CREATE (n:RGBColors {color_name:'%s'})" % (
                color)
            session.run(cyph)

        # Show new colors
        log.info("Step 3.2: Get all of colors in the DB:")
        cyph = """MATCH (p:RGBColors)
                  RETURN p.color_name as color_name
                """
        result = session.run(cyph)
        print("Colors in database:")
        for record in result:
            print(record['color_name'])

        # Setup favorite colors, people that like BLUE color
        for first, last in [("Alice", "Cooper"),
                            ("Fred", "Barnes"),
                            ("Marie", "Curie")]:
            cypher = """
              MATCH (p1:RGBColors {color_name:'Blue'})
              CREATE (p1)-[favColor:FAVCOLOR]->(p2:Person {first_name:'%s', last_name:'%s'})
              RETURN p1
            """ % (first, last)
            session.run(cypher)

        log.info("Step 5.2: Find everyone that likes BLUE")
        cyph = """
          MATCH (blue {color_name:'Blue'})
                -[:FAVCOLOR]->(blueFavorites)
          RETURN blueFavorites
          """
        blue_people = ""
        result = session.run(cyph)
        print("People who like BLUE are:")
        for rec in result:
            for friend in rec.values():
                print(friend['first_name'], friend['last_name'])
                blue_people = blue_people + friend['first_name'] + " " + friend['last_name'] + "\n"

        log.info("Step 5.3: store the data with the pickle.dump method")
        pickle_file = open("../logs/blue_pickle.dat", "ab")
        pickle.dump(blue_people, pickle_file)
        pickle_file.close()

        log.info("Step 5.4: store the data with the shelve method")
        s = shelve.open('../logs/test_shelf.db')
        try:
            s['key1'] = {'int': 10, 'float': 9.5, 'first': 'Alice', 'last': 'Cooper', 'favcolor': 'blue'}
            s['key2'] = {'int': 10, 'float': 9.5, 'first': 'Bob', 'last': 'Smith', 'favcolor': 'blue'}
            s['key3'] = {'int': 10, 'float': 9.5, 'first': 'John', 'last': 'Johns', 'favcolor': 'red'}
            s['key4'] = {'int': 10, 'float': 9.5, 'first': 'Sam', 'last': 'Green', 'favcolor': 'blue'}
            s['key5'] = {'int': 10, 'float': 9.5, 'first': 'Sue', 'last': 'Asher', 'favcolor': 'green'}
            s['key6'] = {'int': 10, 'float': 9.5, 'first': 'Sally', 'last': 'Griffith', 'favcolor': 'blue'}
            s['key7'] = {'int': 10, 'float': 9.5, 'first': 'Ashly', 'last': 'Walsh', 'favcolor': 'red'}
            s['key8'] = {'int': 10, 'float': 9.5, 'first': 'Malory', 'last': 'Jones', 'favcolor': 'blue'}
            s['key9'] = {'int': 10, 'float': 9.5, 'first': 'Rhonda', 'last': 'Garret', 'favcolor': 'yellow'}
            s['key10'] = {'int': 10, 'float': 9.5, 'first': 'Annie', 'last': 'Dobson', 'favcolor': 'blue'}
            s['key11'] = {'int': 10, 'float': 9.5, 'first': 'Emma', 'last': 'Bruce', 'favcolor': 'orange'}
            s['key12'] = {'int': 10, 'float': 9.5, 'first': 'Scott', 'last': 'Cooper', 'favcolor': 'blue'}

        finally:
            s.close()

        # Setup Bob's friends
        log.info('Step 4: Create some relationships')
        log.info("Bob Jones likes Alice Cooper, Fred Barnes and Marie Curie")

        for first, last in [("Alice", "Cooper"),
                            ("Fred", "Barnes"),
                            ("Marie", "Curie")]:
            cypher = """
              MATCH (p1:Person {first_name:'Bob', last_name:'Jones'})
              CREATE (p1)-[friend:FRIEND]->(p2:Person {first_name:'%s', last_name:'%s'})
              RETURN p1
            """ % (first, last)
            session.run(cypher)

        log.info("Step 5: Find all of Bob's friends")
        cyph = """
          MATCH (bob {first_name:'Bob', last_name:'Jones'})
                -[:FRIEND]->(bobFriends)
          RETURN bobFriends
          """
        result = session.run(cyph)
        print("Bob's friends are:")
        for rec in result:
            for friend in rec.values():
                print(friend['first_name'], friend['last_name'])

        log.info("Setting up Marie's friends")

        for first, last in [("Mary", "Evans"),
                            ("Alice", "Cooper"),
                            ('Fred', 'Barnes'),
                            ]:
            cypher = """
              MATCH (p1:Person {first_name:'Marie', last_name:'Curie'})
              CREATE (p1)-[friend:FRIEND]->(p2:Person {first_name:'%s', last_name:'%s'})
              RETURN p1
            """ % (first, last)

            session.run(cypher)

        print("Step 6: Find all of Marie's friends?")
        cyph = """
          MATCH (marie {first_name:'Marie', last_name:'Curie'})
                -[:FRIEND]->(friends)
          RETURN friends
          """
        result = session.run(cyph)
        print("\nMarie's friends are:")
        for rec in result:
            for friend in rec.values():
                print(friend['first_name'], friend['last_name'])
