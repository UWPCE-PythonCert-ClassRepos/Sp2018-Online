import unittest
from peewee import *
from v00_personjob_model import Person, Job, Department

class Results(unittest.TestCase):
    def setUp(self):
        database = SqliteDatabase('data/personjob.db')
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        self.test_person = Person.get(Person.person_name == "Andrew")

    def test_nickname(self):

        self.assertEqual(self.test_person.nickname, "Andy")

    def test_livesin(self):
        self.assertEqual(self.test_person.lives_in_town, "Sumner")

    def test_jobs(self):
        query = Job.get(Job.person_employed == "Andrew")
        self.assertEqual(query.job_name, "Analyst")

    def test_department(self):
        query = Department.get(Department.dep_job == "Analyst")
        self.assertEqual(query.dep_name, "Shipping")

