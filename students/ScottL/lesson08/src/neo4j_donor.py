#!/usr/bin/env python3

# -------------------------------------------------#
# Title: neo4j_donor.py
# Dev: Scott Luse
# Date: 06/02/2018
# Comments: need to add delete record; more investigation
# required to use the cyph MATCH for a specific persons
# donation records
# -------------------------------------------------#

import login_database
import utilities

log = utilities.configure_logger('default', '../logs/neo4j_donor.log')


def donor_create_update(gift_amount, donor_name):
    """
    neo4j add donor record
    """
    log.info("Login to database")
    driver = login_database.login_neo4j_cloud()
    with driver.session() as session:
        log.info('Add Donation record')
        cyph = "CREATE (n:Donation {name:'%s', gift: '%s'})" % (
            gift_amount, donor_name)
        session.run(cyph)

        log.info("Show all donations for: " + donor_name)
        cyph = """MATCH (p:Donation)
                  RETURN p.name as name, p.gift as gift
                """
        result = session.run(cyph)
        print("Donations in database for: " + donor_name)
        for record in result:
            print(record['name'], record['gift'])

def donor_screen_report():
    """
    neo4j screen reporting
    """
    log.info("Login to database")
    driver = login_database.login_neo4j_cloud()
    with driver.session() as session:
        log.info("Show all donations")
        cyph = """MATCH (p:Donation)
                  RETURN p.name as name, p.gift as gift
                """
        result = session.run(cyph)
        print("All donation database records:")
        for record in result:
            print(record['name'], record['gift'])

def donor_detach_delete():
    """
    neo4j detach_delete
    """
    log.info("Running clear_all")
    driver = login_database.login_neo4j_cloud()
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")
