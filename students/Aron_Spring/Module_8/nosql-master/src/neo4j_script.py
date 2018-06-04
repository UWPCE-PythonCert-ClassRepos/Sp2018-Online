"""
    neo4j example
"""

"""
Add some new people to the database. Then add some colors. 
Create associations between people and their favorite colors 
(they can have more than one). Then list all of the people 
who have each color as their favorite. Can you also list all 
of the everyones favorite colors?
"""

import utilities
import login_database
import utilities

log = utilities.configure_logger('default', '../logs/neo4j_script.log')


def run_example():

    log.info('Step 1: First, clear the entire database, so we can start over')
    log.info("Running clear_all")

    driver = login_database.login_neo4j_cloud()
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")

    log.info("Step 2: Add a few people and colors")

    with driver.session() as session:

        people = [('Bob', 'Jones'),
                    ('Nancy', 'Cooper'),
                    ('Alice', 'Cooper'),
                    ('Fred', 'Barnes'),
                    ('Mary', 'Evans'),
                    ('Marie', 'Curie'),
                    ('Bart', 'Simpson'),
                    ('Ned', 'Flanders'),
                    ('Chief', 'Wiggum'),
                    ('Krusty', 'TheClown')
                    ]

        colors = [('Red'), ('Blue'), ('Yellow')]

        log.info('Adding a few Person nodes')
        log.info('The cyph language is analagous to sql for neo4j')
        for first, last in people:
            cyph = "CREATE (n:Person {first_name:'%s', last_name: '%s'})" % (
                first, last)
            session.run(cyph)

        log.info('Adding a few Color nodes')
        for color in colors:
            cyph = "CREATE (n:Color {color:'%s'})" % (color)
            session.run(cyph)

        log.info("Step 3: Get all of people and colors in the DB:")
        cyph = """MATCH (p:Person)
                  RETURN p.first_name as first_name, p.last_name as last_name
                """
        result = session.run(cyph)
        print("People in database:")
        for record in result:
            print(record['first_name'], record['last_name'])

        cyph = """MATCH (p:Color)
                  RETURN p.color as color
                """
        result = session.run(cyph)
        print("Colors in database:")
        for record in result:
            print(record['color'])

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

        log.info('Step 5: Show color relationships')
        log.info('Mary Evans, Bart Simpson and Chief Wiggum all prefer the color Yellow')

        for first, last in [("Mary", "Evans"),
                            ("Bart", "Simpson"),
                            ("Chief", "Wiggum")]:
            cypher = """
              MATCH (p1:Color {color:'Yellow'})
              CREATE (p1)-[fav_color:FAV_COLOR]->(p2:Person {first_name:'%s', last_name:'%s'})
              RETURN p1
            """ % (first, last)
            session.run(cypher)

        log.info("Step 6: Find those who prefer Yellow")
        cyph = """
          MATCH (yellow {color:'Yellow'})
                -[:FAV_COLOR]->(YellowLovers)
          RETURN YellowLovers
          """
        result = session.run(cyph)
        print("Those who love Yellow are:")
        for rec in result:
            for name in rec.values():
                print(name['first_name'], name['last_name'])

        log.info("Step 7: Find all of Bob's friends")
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

        print("Step 8: Find all of Marie's friends?")
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
