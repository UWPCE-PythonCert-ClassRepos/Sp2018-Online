#!/usr/bin/env python3
"""
Donor report for Mailroom using MongoDB
"""
import login_database

def create_donor_report():
    """
    Prints a formatted report on the donors with name, total donation, number of donations,
    and average donation amount.
    """
    with login_database.login_mongodb_cloud() as client:
        db = client['dev']
        donor_db = db['mailroom']

    cursor = donor_db.find({})

    print("{:26s} | {:13s} | {:9s} | {:13s}".format("Donor name", "Total Donation", "Number of Gifts",
                                                    "Average Gifts"))
    print("-" * 80)

    for d in cursor:
        print(f"{d['donor']:26s}  $ {sum(d['donations']):14.2f}" +
              f"{len(d['donations']):15d}  ${sum(d['donations'])/len(d['donations']):.2f}")

if __name__ == '__main__':
    create_donor_report()