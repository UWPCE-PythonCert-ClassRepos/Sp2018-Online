#!/usr/bin/env python3

from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, UUIDField, FloatField, SmallIntegerField
import logging

logging.basicConfig(level=logging.CRITICAL)

dbname = "data.db"
database = SqliteDatabase(dbname)
logging.info("Establishing connection to database")
database.connect()
# execute SQL directly
database.execute_sql('PRAGMA foreign_keys = ON;')


class BaseModel(Model):
    class Meta:
        database = database


class Donor(BaseModel):
    """
    Schema definition
    """
    name = CharField(primary_key=True, max_length=20)

class Donation(BaseModel):
    """
    Schema definition
    """
    # UUID creates a unique id that does not already exist in scope
    gift_id = UUIDField(primary_key=True)
    gift_num = SmallIntegerField()
    value = FloatField()
    # null = False means that this field upon entry cannot be blank, it establishes relationship
    donated_by = ForeignKeyField(Donor, null=False)


database.create_tables([Donor, Donation])
database.close()



