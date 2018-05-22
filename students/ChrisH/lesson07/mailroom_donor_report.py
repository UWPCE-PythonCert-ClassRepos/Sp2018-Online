
from peewee import *
from create_mailroom_db import Donor, Donation


def print_donor_report(database):
    """
    Prints a formatted report on the donors with name, amount given, number of gifts, and average gift.
    :return: None
    """
    name_max = 30

    rpt_title = "Donor Name" + ' ' * (name_max - 9) + "| Total Given | Num Gifts | Average Gift"
    print(rpt_title)
    print("-" * len(rpt_title))

    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')

    query = (Donor
             .select(Donor.name,
                     fn.COUNT(Donation.amount).alias('ccount'),
                     fn.SUM(Donation.amount).alias('csum'),
                     fn.AVG(Donation.amount).alias('cavg'))
             .join(Donation, JOIN.LEFT_OUTER)
             .group_by(Donor.name)
             )

    for d in query:
        # print(f'aggregate {d.donor_name} {d.ccount} {d.csum} {d.cavg}')
        print(f"{d.name:{name_max}}  $ {d.csum:>10.2f}   {d.ccount:>9}  ${d.cavg:>12.2f}")

    database.close()
