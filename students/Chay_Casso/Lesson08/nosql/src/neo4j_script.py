"""
    neo4j example
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
                            ('Robert', 'Irvine'),
                            ('Bobby', 'Flay'),
                            ('Guy', 'Fieri')
                            ]:
            cyph = "CREATE (n:Person {first_name:'%s', last_name: '%s'})" % (
                first, last)
            session.run(cyph)

        log.info('Then add a set of colors to match against.')
        for color in ['Yellow',
                      'Orange',
                      'Green',
                      'Red',
                      'Blue',
                      'Purple'
                      ]:
            cyph = "CREATE (n:Color {color:'%s'})" % (color)
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

        log.info('Step 7: Associate all people with favorite colors.')

        for color in ['Yellow',
                      'Purple']:
            cypher = """
              MATCH (p1:Person {first_name:'Bob', last_name:'Jones'})
              CREATE (p1)-[favorite:FAVORITE]->(p2:Color {color:'%s'})
              RETURN p1
            """ % (color)
            session.run(cypher)

        cypher = """
                 MATCH (p1:Person {first_name:'Alice', last_name:'Cooper'})
                 CREATE (p1)-[favorite:FAVORITE]->(p2:Color {color:'Blue'})
                 RETURN p1
                 """
        session.run(cypher)

        cypher = """
                         MATCH (p1:Person {first_name:'Fred', last_name:'Barnes'})
                         CREATE (p1)-[favorite:FAVORITE]->(p2:Color {color:'Orange'})
                         RETURN p1
                         """
        session.run(cypher)

        cypher = """
                         MATCH (p1:Person {first_name:'Marie', last_name:'Curie'})
                         CREATE (p1)-[favorite:FAVORITE]->(p2:Color {color:'Red'})
                         RETURN p1
                         """
        session.run(cypher)

        cypher = """
                         MATCH (p1:Person {first_name:'Nancy', last_name:'Cooper'})
                         CREATE (p1)-[favorite:FAVORITE]->(p2:Color {color:'Orange'})
                         RETURN p1
                         """
        session.run(cypher)

        cypher = """
                         MATCH (p1:Person {first_name:'Mary', last_name:'Evans'})
                         CREATE (p1)-[favorite:FAVORITE]->(p2:Color {color:'Yellow'})
                         RETURN p1
                         """
        session.run(cypher)

        cypher = """
                         MATCH (p1:Person {first_name:'Robert', last_name:'Irvine'})
                         CREATE (p1)-[favorite:FAVORITE]->(p2:Color {color:'Green'})
                         RETURN p1
                         """
        session.run(cypher)

        cypher = """
                         MATCH (p1:Person {first_name:'Bobby', last_name:'Flay'})
                         CREATE (p1)-[favorite:FAVORITE]->(p2:Color {color:'Red'})
                         RETURN p1
                         """
        session.run(cypher)

        cypher = """
                         MATCH (p1:Person {first_name:'Guy', last_name:'Fieri'})
                         CREATE (p1)-[favorite:FAVORITE]->(p2:Color {color:'Yellow'})
                         RETURN p1
                         """
        session.run(cypher)

        log.info('Now we print out who has which favorite colors:')
        for colors in ['Yellow',
                      'Orange',
                      'Green',
                      'Red',
                      'Blue',
                      'Purple',
                      ]:
            cyph = """
                MATCH (color {color:'%s'})<-[:FAVORITE]-(persons) 
                RETURN DISTINCT persons
            """ % (colors)
            result = session.run(cyph)

            for match in result:
                for friend in match.values():
                    print(colors, ':', friend['first_name'], friend['last_name'])

        log.info("Note that for some reason this is returning duplicates. Even"
                 "though I run DISTINCT, it sees multiple nodes as having the"
                 "same value.")

        log.info("Printing everyone's favorite colors...")
        cyph = """
                  MATCH (p:Person)-[:FAVORITE]->(colors)
                  RETURN p.first_name as first_name, p.last_name as last_name, colors.color as color
                  """
        result = session.run(cyph)
        print("\nEveryone's colors:")
        for rec in result:
            print(rec['first_name'], rec['last_name'], ":", rec['color'])