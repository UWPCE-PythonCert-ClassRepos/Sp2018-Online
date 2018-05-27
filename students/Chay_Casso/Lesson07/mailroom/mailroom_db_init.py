"""
Mailroom DB Init

Describes the classes necessary to instantiate the database for mailroom
and populates it with the default information.
"""

from functools import partial
import logging
import peewee

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('One off program to build the classes from the model in the database')

logger.info('Here we define our data (the schema)')

database = peewee.SqliteDatabase('mailroom.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only


class BaseModel(peewee.Model):
    class Meta:
        database = database


class Donor_Person(BaseModel):
    """
    This class provides a list of donor contact information.
    """

    person_name = peewee.CharField(primary_key = True, max_length = 40)
    email_address = peewee.CharField(max_length = 50)


class Donation(BaseModel):
    """
    This class provides a list of donations and a link to the Donor table.
    Because we have no unique identifiers, we'll let Peewee autocreate a PK.
    """

    gift_value = peewee.DecimalField(decimal_places=2)
    gift_date = peewee.DateField(formats = "YYYY-MM-DD")
    gift_donor = peewee.ForeignKeyField(Donor_Person, column_name="person_name", null=False)

if __name__ == '__main__':

    try:
        database.create_tables([
            Donor_Person,
            Donation
        ])

        logger.info("Populating Donor database.")

        person_name = 0
        email_address = 1

        donors = [
            ("William Gates III", "bill.gates@msn.com"),
            ("Jeff Bezos", "bezos@amazon.com"),
            ("Paul Allen", "paul.allen@hotmail.com"),
            ("Mark Zuckerberg", "zuck@facebook.com")
        ]
        for donor in donors:
            with database.transaction():
                new_donor = Donor_Person.create(
                    person_name = donor[person_name],
                    email_address = donor[email_address]
                )
                new_donor.save()
                logger.info("Database add successful")

        logger.info("Now we set up the Donation table.")
        gift_value = 0
        gift_date = 1
        gift_donor = 2

        donations = [
            (653772.32, "2015-01-01", "William Gates III"),
            (12.17, "2016-01-01", "William Gates III"),
            (877.33, "2017-01-01", "Jeff Bezos"),
            (663.23, "2015-01-01", "Paul Allen"),
            (43.87, "2016-01-01", "Paul Allen"),
            (1.32, "2017-01-01", "Paul Allen"),
            (1663.23, "2015-01-01", "Mark Zuckerberg"),
            (4300.87, "2016-01-01", "Mark Zuckerberg"),
            (10432.0, "2017-01-01", "Mark Zuckerberg")
        ]
        for donation in donations:
            with database.transaction():
                new_donation = Donation.create(
                    gift_value = donation[gift_value],
                    gift_date = donation[gift_date],
                    gift_donor = donation[gift_donor]
                )
                new_donation.save()
                logger.info("Database add successful")


    except Exception as e:
        logger.info(e)

    finally:
        database.close()