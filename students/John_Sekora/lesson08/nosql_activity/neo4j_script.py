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

        # Added extra names
        log.info('Adding a few Person nodes')
        log.info('The cyph language is analagous to sql for neo4j')
        for first, last in [('Bob', 'Jones'),
                            ('Nancy', 'Cooper'),
                            ('Alice', 'Cooper'),
                            ('Fred', 'Barnes'),
                            ('Mary', 'Evans'),
                            ('William', 'Duke'),
                            ('Jake', 'Smith'),
                            ('Matt', 'Springer'),
                            ]:
            cyph = "CREATE (n:Person {first_name:'%s', last_name: '%s'})" % (first, last)
            session.run(cyph)

        log.info("Step 3: Get all of people in the DB:")
        cyph = """MATCH (p:Person)
                  RETURN p.first_name as first_name, p.last_name as last_name
                """
        result = session.run(cyph)
        print("People in database:")
        for record in result:
            print(record['first_name'], record['last_name'])

        # Added colors
        log.info('Adding colors to Redis')
        for color in [('Red'),
                      ('Blue'),
                      ('Yellow'),
                      ('Green'),
                      ('Pink'),
                      ('Purple'),
                      ]:
            cyph = "CREATE (n:Color {color:'%s'})" % (color)
            session.run(cyph)

        # Displaying colors
        log.info("Displaying colors from Redis")
        cyph = """MATCH (p:Color)
                  RETURN p.color as color
                """
        result = session.run(cyph)
        print("Colors in database:")
        for record in result:
            print(record['color'])

        # Creating associations between Person and Color
        log.info('Creating associations between Person and Color')
        log.info("William Duke, Bob Jones, Nancy Cooper, and Jake Smith all like the color Red")

        for first, last in [('William', 'Duke'),
                            ('Bob', 'Jones'),
                            ('Nancy', 'Cooper'),
                            ('Jake', 'Smith'),
                           ]:
            cyph = """
              MATCH (p1:Color {color:'Red'})
              CREATE (p1)-[association:Associate]->(p2:Person {first_name:'%s', last_name:'%s'})
              RETURN p1
            """ % (first, last)
            session.run(cyph)

        log.info("Adding the color Red association to William Duke, Bob Jones, Nancy Cooper, and Jake Smith")
        cyph = """
          MATCH (p1:Color {color:'Red'})
                -[:likes]->(Likes)
          RETURN Likes
          """
        result = session.run(cyph)
        print("The people who like Red are: ")
        for rec in result:
            for like_red in rec.values():
                print(like_red['first_name'], like_red['last_name'])

        # Adding a color for Mary Evans
        cyph = """
                 MATCH (p1:Person {first_name:'Mary', last_name:'Evans'})
                 CREATE (p1)-[like:Likes]->(p2:Color {color:'red'})
                 RETURN p1
                 """
        session.run(cyph)

        log.info("Adding the color Red for Mary Evans")
        cyph = """
          MATCH (red {color:'Red'})
                -[:likes]->(Likes)
          RETURN Likes
          """
        result = session.run(cyph)
        print("Mary likes Red, her full name is: ")
        for rec in result:
            for like_red in rec.values():
                print(like_red['first_name'], like_red['last_name'])

        # Adding the color Yellow for William Duke
        cyph = """
                 MATCH (p1:Person {first_name:'William', last_name:'Duke'})
                 CREATE (p1)-[likes:Likes]->(p2:Color {color:'yellow'})
                 RETURN p1
                 """
        session.run(cyph)

        log.info("Adding the color Yellow for William Duke")
        cyph = """
          MATCH (yellow {color:'Yellow'})
                -[:likes]->(Likes)
          RETURN Likes
          """
        result = session.run(cyph)
        print("William likes Yellow, his full name is: ")
        for rec in result:
            for like_red in rec.values():
                print(like_red['first_name'], like_red['last_name'])

        # Listing all of the people and their favorite colors
        for per in session.run("MATCH (p:Person) RETURN p.first_name as first_name, p.last_name as last_name"):
            cyph = "MATCH (person {first_name:'%s', last_name:'%s'})-[:likes]->(Likes) RETURN Likes" % (
                per['first_name'], per['last_name'])
            res = session.run(cyph)
            for like in res:
                print(f": {like['first_name']} {like['last_name']} likes the colors:")
                for hue in like.values():
                    print(hue['color'] + "\n")

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
