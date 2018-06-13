# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 11:58:22 2018

@author: seelc
"""

import datetime
from peewee import *
import sqlite3
import logging

#Creating database for donor storage
db = SqliteDatabase('donors.db')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BaseModel(Model):
    
    '''Basemodel that donor inherates from in order to set the database to db'''
    
    class Meta:
        database = db
        

          
class donor(BaseModel):
    
    '''Donor class stores all the information for an individual donor, inherates
    from Basemodel to correctly set database'''   
    
    logger.info("Created a new donor")
    donor_name = CharField(primary_key = True)
    db_donation_amount = DoubleField()
    donation_times = DoubleField()
    avg_donation = DoubleField()
    


class donor_storage():
    
    '''Donor storage allows for the aggregation of multiple donors and contains a 
    method for each action required of the mailroom program'''    
           
    def update_donor_list(self, name_request, donation_amount):
        
        '''Updates donor database file, either updating information for an existing
        donor or adding a new one'''
        
        assert int(donation_amount) > 0.0
        assert isinstance(name_request, str)
        
        logger.info("Updating donor database")
        try:
            query = donor.select().where(donor.donor_name == name_request)
            #If the donor is a repeat update all fields
            if query.exists():
                logger.info("Donor has previously donated")
                update_query = donor.select().where(donor.donor_name == name_request).get()
                update_query.db_donation_amount += float(donation_amount)
                update_query.donation_times += 1
                update_query.avg_donation = update_query.db_donation_amount/update_query.donation_times
                update_query.save()
        
            #If its a new donor, create the donor
            else:
                with db.transaction():
                    logger.info("New donor, first time donating")
                    new_donor = donor.create(donor_name = name_request, 
                                     db_donation_amount = donation_amount, donation_times = 1, 
                                     avg_donation = donation_amount)
                    new_donor.save()
        except Exception as error:
            logger.error("Couldnt create donor")
            
 

    def create_report(self):
        
        '''Prints out the donor database in the specified format, the code lacks
        elegance but I had a difficult time achieving the specified format without
        making it wordy'''
        
        logger.info("Entered create_report")
        max_name_length = 0
        max_donation_length = 0
        avg_gift_length = 0
        default_header = "Donor Name"+" "+ "|" +"Total Given" + "  |" + "Num Gifts" + "|" + "Average Gift"
        default_length = len(default_header)
        
        #Determing spacing required for table
        for donors in donor.select():
            if len(donors.donor_name) > max_name_length:
                max_name_length = len(donors.donor_name)
            if len(str(donors.db_donation_amount)) > max_donation_length:
                max_donation_length = len(str(donors.db_donation_amount))
            if len(str(avg_gift_length)) > avg_gift_length:
                avg_gift_length = len(str(avg_gift_length))
        
        first_column = max(max_name_length, len("Donor Name"))
        second_column = max(max_donation_length, len("Total Given"))
        third_column = max(avg_gift_length, len("Average Gift"))
        
        #Print statement that deals with printing each donors information in a 
        #correctly formatted fashion
        print("Donor Name" + " "*max(max_name_length - len("Donor Name"), 0)+  "|",
              "Total Given" + " " * max(max_donation_length - len("Total Given"), 0) + "|",
              "Num Gifts" + "|" + " "*max(avg_gift_length - len("Average Gift") ,0),
              "Average Gift")
        required_length = max_name_length + max_donation_length + avg_gift_length + 4
        #prints the second line with the correct number of dashes
        print("-"*max(default_length, required_length))
        
                
        for donors in donor.select():
        #Prints data for each donor object one line at a time
            
            print(donors.donor_name,
                  " "*(first_column - len(str(donors.donor_name))),
                  " "* (second_column - len(str(donors.db_donation_amount))),
                  donors.db_donation_amount,
                  " "*(len("Num Gifts")- len(str(donors.donation_times))),
                  donors.donation_times,
                  " "*(third_column - len(str(donors.avg_donation))),
                  donors.avg_donation)
            
   
    def send_group_thanks(self):
        
        '''Reads through the database and writes a new text file to each donor
        thanking them for there donation.'''
        
        logger.info("Entered send_group_thanks")
        for donors in donor.select():
            dateSent = str(datetime.date.today())
            group_Thanks = open("{}_{}".format(donors.donor_name, dateSent), "w")
            line_1 = "Dear {},\n\nThank you for your generous donation of ${},"
            line_2 = "it will be put to good use.\n\n-Sincerely, the team\n\n"
            group_Thanks.write((line_1 + line_2).format(donors.donor_name, donors.db_donation_amount))

    
    def delete_entry(self, entry_delete):
        
        '''Allows the user to remove a donor from the database'''
        
        logger.info("Entered delete entry method")
        try:
            query = donor.select().where(donor.donor_name == entry_delete)
            if query.exists():
                logger.info("Query exists, deleting donor")
                delete_donor = donor.select().where(donor.donor_name == entry_delete).get()
                delete_donor.delete_instance()

                
        except Exception as error:
            logger.error("Couldnt delete donor")
            
        finally:
            logger.error("Encountered unkown error")

        
    def clear_database(self):
        
        '''Completely clears the database of all donors'''
        
        logger.info("Deleting all records")
        for donors in donor.select():
            donors.delete_instance()
        logger.info("All records deleted")
            
           
def main():
    
    '''contains the primary loop providing user options and executing mailroom options
    based on user inputs'''
    
    db.connect()
    db.execute_sql('PRAGMA foreign_keys = ON;')
    db.create_tables([donor], safe = True)
    db.close()
    overall_storage = donor_storage()
    
    #promting the user to choose a main action
    userAction = ""
    while userAction !="4":
        userAction = input( "Choose an action: \n1 - Send a thank you\n2 - Create"+ 
                           " a Report\n3 - Send a thank you to everyone\n" + 
                           "4 - Delete an entry\n5 - Clear the Database\n6 - Quit\n")
        
        #Throws an exception if userAction isnt 1, 2, or 3
        try:
            assert userAction in ["1", "2", "3", "4", "5", "6"]
            #if the user chooses to send a thank you
            if userAction == "1":
                name_request = input("Please select a name: ")
                donation_amount = input("Please enter a donation amount: ")

                #Adds the new donor to the donor database
                overall_storage.update_donor_list(name_request, donation_amount)
        
            #if the user chooses to create a report
            elif userAction == "2":
                overall_storage.create_report()
                
            #if the user chooses to send a thank you to everyone
            elif userAction == "3":
                overall_storage.send_group_thanks()
            
            #Deleting a single donor, deals with case where user accidently enters
            #a donor incorrectly
            elif userAction == "4":
                entry_delete = input("Select a donor to delete: ")
                overall_storage.delete_entry(entry_delete)
            
            #Allows the user to clear the entire database
            elif userAction == "5":
                overall_storage.clear_database()
                
            #if none of the above options are chosen quits the program
            elif userAction == "6":
                logger.info("Quiting program and closeing database connection")
                db.close()
                break
            
        except ValueError:
            print("The value entered must be 1, 2, 3, or 4")

if __name__ == '__main__':
    main()         
    
    