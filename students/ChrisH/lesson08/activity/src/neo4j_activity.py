"""
    neo4j example
"""


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

        people = [('Bob', 'Jones'),
                  ('Nancy', 'Cooper'),
                  ('Alice', 'Cooper'),
                  ('Fred', 'Barnes'),
                  ('Mary', 'Evans'),
                  ('Marie', 'Curie'),
                  ('Don', 'Domingo'),
                  ('Bill', 'Bastante'),
                  ]
        colors = ['red', 'blue', 'green']

        log.info('Adding a few Person nodes')
        log.info('The cyph language is analogous to sql for neo4j')
        for first, last in people:
            cyph = "CREATE (n:Person {first_name:'%s', last_name: '%s'})" % (
                first, last)
            session.run(cyph)

        for color in colors:
            cyph = "CREATE (n:Color {color:'%s'})" % (color)
            session.run(cyph)

        cyph = """MATCH (p:Color)
                  RETURN p.color as color
               """
        result = session.run(cyph)
        print("Colors in database:")
        for record in result:
            print(record['color'])

        log.info("Step 3: Get all of people in the DB:")
        cyph = """MATCH (p:Person)
                  RETURN p.first_name as first_name, p.last_name as last_name
                """
        result = session.run(cyph)
        print("People in database:")
        next_color = 0
        for record in result:
            print(record['first_name'], record['last_name'])

            # Add favorite colors to people
            cyph = "MATCH (p1:Person {first_name:'%s', last_name:'%s'})" % (record['first_name'], record['last_name'])
            cyph += "CREATE (p1)-[fav:FAV]->(p2:Color {color:'%s'})" % (colors[next_color % len(colors)])
            cyph += "RETURN p1"
            next_color += 1

            session.run(cyph)

        # Add another favorite color to BOB, who likes things.
        cyph = """
                 MATCH (p1:Person {first_name:'Bob', last_name:'Jones'})
                 CREATE (p1)-[fav:FAV]->(p2:Color {color:'blue'})
                 RETURN p1
                 """
        session.run(cyph)

        for p in session.run("MATCH (p:Person) RETURN p.first_name as first_name, p.last_name as last_name"):
            cyph = "MATCH (person {first_name:'%s', last_name:'%s'})-[:FAV]->(personFavs) RETURN personFavs" % (p['first_name'], p['last_name'])
            res = session.run(cyph)
            for rec in res:
                print(f"For person: {p['first_name']} {p['last_name']} favorite colors are:")
                for color_val in rec.values():
                    print("  " + color_val['color'])

        cyph = """
                  MATCH (bob {first_name:'Bob', last_name:'Jones'})
                        -[:FAV]->(bobFavs)
                  RETURN bobFavs
                  """
        result = session.run(cyph)
        print("Bob's favorite colors are:")
        for rec in result:
            for color_val in rec.values():
                print(color_val['color'])


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

if __name__ == "__main__":

    run_example()
