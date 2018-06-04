from textwrap import dedent
from peewee import *
from src.data_model import Person, Donation

class DonorData():

    @staticmethod
    def gen_letter(donor):
        return dedent('''Dear {},

              Thank you for your very kind donation of ${:.2f}.
              It will be put to very good use.

                Sincerely,
                -The Team'''.format(donor.last_name, donor.donation.donation_amount))

    @staticmethod
    def save_letters(self):
        database = SqliteDatabase('mailroom.db')
        try:
            database.connect()
            database.execute_sql('PRAGMA foreign_keys = ON;')
            query = (Person
                     .select(Person, Donation)
                     .join(Donation, JOIN.INNER)
                     )

            for person in query:
                with open(person.name + '.txt', 'w') as file:
                    file.write(self.gen_letter(person))

        except Exception as e:
            print(e)

        finally:
            database.close()

    @staticmethod
    def print_report():
        database = SqliteDatabase('mailroom.db')
        report = []
        try:
            database.connect()
            database.execute_sql('PRAGMA foreign_keys = ON;')

            query = (Person
                     .select(Person, Donation)
                     .join(Donation, JOIN.INNER)
                     )
            line = []
            for person in query:
                fist_name = person.fist_name
                last_name = person.last_name
                donation = person.donation.donation_amount
                line.append((fist_name, last_name, donation))

            header = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
            report.append('{:25} |{:^15} |{:^15} |{:^15}'.format(*header))
            report.append("-" * 75)
            for l in line:
                report.append("{:25}   ${:^15.2f}   {:^15d}   ${:^15.2f}".format(*l))

        except Exception as e:
            print(e)

        finally:
            database.close()
            return "\n".join(report)

