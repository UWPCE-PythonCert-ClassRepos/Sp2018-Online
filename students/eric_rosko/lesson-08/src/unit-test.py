#!/usr/bin/env python3

'''
Usage: 1.) navigate into src/ first

python3 -m unittest unit-test.py -v

python3 -m unittest -v unit-test.py unit-test.MongoTests


'''

# from unittest import unittest
from unittest import TestCase
# from learn_data import *
from mongodb_script import *
from login_database import *
import learn_data

import redis_script
import neo4j_script
import simple_script
import utilities
import json
import pickle

log = utilities.configure_logger('default', '../logs/unit-test.log')

class MongoTests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mongo_insert(self):
        furniture_items = learn_data.get_furniture_data_split_first_field()

        with login_mongodb_cloud() as client:
            db = client['dev']
            furniture = db['furniture']

            furniture.insert_many(furniture_items)
            query = {'description': 'Plastic'}
            results = furniture.find_one(query)

            print('Plastic products')
            pprint.pprint(results)

            furniture.delete_many({"product": {"$eq": "couch"}})

            query = {'product': 'couch'}
            results = furniture.find_one(query)
            print('The blue couch is deleted, print should show none:')
            pprint.pprint(results)

            cursor = furniture.find({'monthly_rental_cost': {'$gte': 15.00}}).sort('monthly_rental_cost', 1)

            print('Results of search')

            for doc in cursor:
                print(f"Cost: {doc['monthly_rental_cost']} product name: {doc['product']} Stock: {doc['in_stock_quantity']}")

            results = db['furniture'].find({})
            results_count = results.count()
            print("\nResults", results.count())
            for doc in results:
                print(f"XXX  Cost: {doc['monthly_rental_cost']} product name: {doc['product']} Stock: {doc['in_stock_quantity']}")

            db.drop_collection('furniture')

            self.assertEqual(results_count, 3)


    def test_mongo_add_one_get_couches(self):
            furniture_items = learn_data.get_furniture_data_split_first_field()

            with login_mongodb_cloud() as client:
                db = client['dev']
                furniture = db['furniture']

                furniture.insert_many(furniture_items)

                furniture.insert_one({
                                      'product': 'couch',
                                      'color': 'purple',
                                      'description': 'Low cotton',
                                      'monthly_rental_cost': 32.99,
                                      'in_stock_quantity': 1})

                cursor = furniture.find({"product": {"$eq": "couch"}})
                results_count = cursor.count()

                print('Results of search')

                for doc in cursor:
                    print(f"Cost: {doc['monthly_rental_cost']} product name: {doc['product']} Stock: {doc['in_stock_quantity']}")

                db.drop_collection('furniture')

                self.assertEqual(results_count, 4)


    def test_mongo_get_red_items(self):
            furniture_items = learn_data.get_furniture_data_split_first_field()

            with login_mongodb_cloud() as client:
                db = client['dev']
                furniture = db['furniture']

                furniture.insert_many(furniture_items)

                furniture.insert_one({
                                      'product': 'couch',
                                      'color': 'purple',
                                      'description': 'Low cotton',
                                      'monthly_rental_cost': 32.99,
                                      'in_stock_quantity': 1})

                cursor = furniture.find({"color": {"$eq": "Red"}})
                results_count = cursor.count()

                print('Results of search')

                for doc in cursor:
                    print(f"Cost: {doc['monthly_rental_cost']} product name: {doc['product']} Stock: {doc['in_stock_quantity']}")

                db.drop_collection('furniture')

                self.assertEqual(results_count, 2)


    def test_hello(self):
        print('hello')
        self.assertEqual(2, 2, "basic test should pass")


class Neo4jTests(TestCase):

    def setUp(self):
        self.driver = login_database.login_neo4j_cloud()
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")


    def tearDown(self):
        pass


    def test_basic(self):
        with self.driver.session() as session:
            # Create some nodes with labels

            for color in ["Red", "Green", "Blue"]:
                # cyph = "CREATE (n:Color {first_name:'%s'}) RETURN n" % (color)
                cyph = "CREATE (n:Color {name:'%s'}) RETURN n" % (color)
                session.run(cyph)

            cyph = """MATCH (p:Color)
                  RETURN p.name as name
                """
            result = session.run(cyph)
            print("Colors in database:")
            for record in result:
                # Color:  <Record p=<Node id=44 labels={'Color'} properties={'name': 'Red'}>>
                print("Color: ", record['name'])

            # CREATE (you:Person {name:"You"}) RETURN you


            for first, last in [('Bob', 'Jones'),
                                ('Nancy', 'Cooper'),
                                ('Alice', 'Cooper'),
                                ('Fred', 'Barnes'),
                                ]:
                cyph = "CREATE (n:Person {first_name:'%s', last_name: '%s'}) RETURN n" % (
                    first, last)
                session.run(cyph)

            # assing red to all people
            cyph = """MATCH (p:Person{} )
            CREATE (p)-[fav:FAVORITE_COLOR]->(color:Color {name:"Red"})
            RETURN p,fav,color
                """

            result = session.run(cyph)
            print("Colors in database:")
            for record in result:
                # Color:  <Record p=<Node id=44 labels={'Color'} properties={'name': 'Red'}>>
                print("Output: ", record)


            # assing red to all people
            cyph = """MATCH (p:Person{last_name:'Jones'} )
            CREATE (p)-[fav:FAVORITE_COLOR]->(color:Color {name:"Blue"})
            RETURN p,fav,color
                """

            result = session.run(cyph)

            result = session.run("""MATCH (p:Person{first_name:'Nancy'} )
                CREATE (p)-[:FAVORITE_COLOR]->(:Color {name:"Green"})
                RETURN p
                """)
            for item in result:
                print("\nXXX", item)


            cyph = """MATCH (c:Color {name: "Red"})-[:FAVORITE_COLOR]->(red_color_people)
                     RETURN red_color_people
                    """
            result = session.run(cyph)
            print("All Colors in database:")
            for record in result:
                print("Color: ", record)


class RedisTests(TestCase):

    def setUp(self):
        self.driver = login_database.login_neo4j_cloud()
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")


    def tearDown(self):
        pass


    def test_basic_set_and_get(self):
        r = login_database.login_redis_cloud()

        # pushing a list.  key must start with an int for some reason
        print("list example")
        r.lpush("1andy", '206-352-5931', '63223')
        print("1andy's telephone #", r.lindex("1andy", 1))
        print("1andy's zip code", r.lindex("1andy", 2))

        print("\ndictionary example")
        # pushing a dictionary

        # oddly, I can't use andy as a key after using 1andy as
        # a key in the list.  The list required a starting #.
        r.hmset("andy1", {'tel': '206-352-5931', 'zip': 63223})

        my_dict = r.hgetall("andy1")
        for key in my_dict.keys():
            print(key, "for andy1 is", my_dict[key])
        # print(my_dict[0])
        # print("andy telephone #:", r.hgetall("andy1"))

        # r.set('sam', ['206-562-7653', 55633])
        # r.set('linda', '253-351-5336', 26343)
        # r.set('joe', '206-352-8237', 98323)
        # r.set('jill', '253-152-5978', 98111)
        # r.set('susan', '206-352-5236', 98783)

        # r.rpush('andy', '206-352-5931')
        # r.rpush('andy', 55633)
        # print(r.range('andy', 0, 1))
        # log.info('Retrieve zip code')


        # email = r.get('andy')
        # log.info('But I must know the key')
        # log.info(f'The results of r.get: {email}')

        # log.info('Retrieve telephone #')
        # record = r.get('andy')
        # dict = Dict(record)
        # print(dict[0])

        # log.info('Retrieve zip code')
        # record = r.get('andy')
        # print(record)


        # log.info('Step 4: delete from cache')
        # r.delete('andy')
        # log.info(f'r.delete means andy is now: {email}')

        # log.info(
        #     'Step 6: Redis can maintain a unique ID or count very efficiently')
        # r.set('user_count', 21)
        # r.incr('user_count')
        # r.incr('user_count')
        # r.decr('user_count')
        # result = r.get('user_count')
        # log.info('I could use this to generate unique ids')
        # log.info(f'Redis says 21+1+1-1={result}')

        # log.info('Step 7: richer data for a SKU')
        r.rpush('186675', 'chair')
        r.rpush('186675', 'red')
        r.rpush('186675', 'leather')
        r.rpush('186675', '5.99')

        # log.info('Step 8: pull some data from the structure')
        cover_type = r.lindex('186675', 2)
        log.info(f'Type of cover = {cover_type}')


class SimplePersistenceTests(TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_basic(self):

        data = {'one': 1, 'two': 2}
        open_file = open('../data/data.pkl', 'wb')
        pickle.dump(data, open_file)
        open_file.close()

        log.info('Step 2: Now read it back from the pickle file')
        with open('../data/data.pkl', 'rb') as reader:
            read_data = pickle.load(reader)
            log.info('Step 3: Show that the write and read were successful')
            assert read_data == data
            log.info("and print the data")
            pprint.pprint(read_data)



if __name__ == "__main__":
    unittest.main()
