from peewee import *

database = SqliteDatabase('./mailroom.db')


class BaseModel(Model):
    class Meta:
        database = database


class Donor(BaseModel):
    name = CharField(primary_key=True, max_length=30)
    first = CharField(max_length=30)
    last = CharField(max_length=30)


class Donation(BaseModel):
    donor = ForeignKeyField(Donor, null=False)
    amount = FloatField(null=False)


if __name__ == "__main__":

    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')  # needed for sqlite only

    database.create_tables([
            Donor,
            Donation
        ])

    database.close()


