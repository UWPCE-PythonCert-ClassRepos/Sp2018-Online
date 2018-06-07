import logging
import login_database


class Mailroom(object):

    def __init__(self):
        pass

    def list_donors(self):
        with login_database.login_mongodb_cloud() as client:
            furniture = db['furniture']


    def list_donations(self):
        result =''
        query = Donor.select(Donor.first_name,
                                  Donor.last_name,
                                  Donation.amount,
                                  Donation.created_date)\
                                  .join(Donation)
        for row in query.dicts():
            result += f"{row['first_name']} " \
                      f"{row['last_name']} " \
                      f"${row['amount']}" \
                      f"\n"
        return result

    def seperator(self,str):
        """return line that equals string length ignoring newline."""
        return "-" * (len(str) - str.count('\n'))

    def create_report(self):
        heading = "Donor Name | Total Given | Num Gifts | Average Gift\n"
        heading += self.seperator(heading)
        query = Donor.select(Donor.first_name,
                                  Donor.last_name,
                                  fn.sum(Donation.amount).alias('sum_donation'),
                                  fn.count(Donation.amount).alias('count_donation'),
                                  fn.avg(Donation.amount).alias('average_donation'))\
            .join(Donation)\
            .group_by(Donor.first_name)
        result = ''
        for row in query.dicts():
             result += "{:10} ${:10.2f} {:10} {:15.2f}\n".format(row['first_name'],
                                                                 row['sum_donation'],
                                                                 row['count_donation'],
                                                                 row['average_donation'])
        return(f"{heading}\n{result}")