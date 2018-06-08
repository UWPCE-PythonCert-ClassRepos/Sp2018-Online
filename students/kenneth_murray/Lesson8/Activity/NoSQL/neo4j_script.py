#!/usr/bin/env python3
"""
    neo4j example
    lesson8
    Add some new people to the database.
    Then add some colors. Create associations between people and their favorite colors
    (they can have more than one).
    Then list all of the people who have each color as their favorite.
"""

import utilities
import login_database

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
                            ('Ken', 'Murray'),
                            ('Nathan', 'Merrill'),
                            ('Tina', 'Tangsuk'),
                            ('color', 'red'),
                            ('color', 'blue'),
                            ('color', 'green')
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

        log.info('Step 4: Create some relationships')
        log.info("Bob Jones likes blue")

        for first, last in [("color", "blue")]:
            cypher = """
              MATCH (p1:Person {first_name:'Bob', last_name:'Jones'})
              CREATE (p1)-[color:COLOR]->(p2:Color {first_name:'%s', last_name:'%s'})
              RETURN p1
            """ % (first, last)
            session.run(cypher)

        log.info("Step 5: Find  of Bob's color")
        cyph = """
          MATCH (bob {first_name:'Bob', last_name:'Jones'})
                -[:COLOR]->(bobColors)
          RETURN bobColors
          """
        result = session.run(cyph)
        print("Bob's colors are:")
        for rec in result:
            for color in rec.values():
                print(color['last_name'])

        log.info("Setting up Marie's colors")

        for first, last in [("color", "blue"),
                            ("color", "green"),
                            ('color', 'red'),
                            ]:
            cypher = """
              MATCH (p1:Person {first_name:'Marie', last_name:'Curie'})
              CREATE (p1)-[color:COLOR]->(p2:Color {first_name:'%s', last_name:'%s'})
              RETURN p1
            """ % (first, last)

            session.run(cypher)

        print("Step 6: Find all of Marie's colors")
        cyph = """
          MATCH (marie {first_name:'Marie', last_name:'Curie'})
                -[:COLOR]->(colors)
          RETURN colors
          """
        result = session.run(cyph)
        print("\nMarie's colors are:")
        for rec in result:
            for friend in rec.values():
                print(friend['last_name'])
