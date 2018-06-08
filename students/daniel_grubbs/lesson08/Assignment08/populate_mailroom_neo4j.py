"""
    Data for Donor Management System database - Neo4j
"""

import login_database
import utilities

log = utilities.configure_logger('default', 'logs/neo4j_script.log')


def populate_donor_data():
    """
    Populate donor data
    """
    log.info('Step 1: First, clear the entire database, so we can start over')
    log.info("Running clear_all")

    driver = login_database.login_neo4j_cloud()
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")

    log.info("set some data for database")

    log.info("Step 2: Add a few people")

    with driver.session() as session:
        # Define our initial donor data
        donor_data = [('Jimmy Nguyen', 'Houston'),
                  ('Steve Smith', 'Seattle'),
                  ('Julia Norton', 'Portland'),
                  ('Ed Johnson', 'Atlanta'),
                  ('Elizabeth McBath', 'Austin'),
                  ]

        for donor, city in donor_data:
            cyph = "CREATE (n:Donor {donor_name:'%s', city: '%s'})" % (
                donor, city)
            session.run(cyph)


if __name__ == '__main__':
    log.info('running function to populate data')
    populate_donor_data()
