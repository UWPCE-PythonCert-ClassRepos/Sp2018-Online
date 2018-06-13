from mailroom_donor_report_mongodb import print_donor_report
import login_database
import uuid


def get_first(name):
    name_sp = name.split()
    if len(name_sp) == 1:
        return ''
    else:
        return name_sp[0]


def get_last(name):
    name_sp = name.split()
    if len(name_sp) == 1:
        return name
    else:
        return ' '.join(name_sp[1:])


def generate_letter(donor_doc):
    """
    Generates a Thank You letter to send to a donor. Uses the last value in their donations list to
    mention their last donation amount.
    :param donor: a donor dictionary entry
    :return: string containing the text of the Thank You letter.
    """
    format_string = """
Dear {first_name} {last_name},
   Thank you for your donation of ${last_donation:.2f}.
            Warmest Regards,
                Local Charity
"""
    result = format_string.format(
        first_name=get_first(donor_doc['donor_name']),
        last_name=get_last(donor_doc['donor_name']),
        last_donation=donor_doc['donations'][-1]
    )

    return result


def send_thank_you_menu(database):
    """
    Prompts for donor name, if not present, adds user to data. Prompts for donation
    and adds it to donor's data. Prints a 'Thank You' email populated with the donor's data.
    :return: None
    """

    while True:
        name = input("Enter a Full Name ('list' to show list of donors, 'q' to quit): ")
        if name == 'q' or name == '':
            return
        elif name == 'list':
            cursor = database.find({})
            for doc in cursor:
                print(doc['donor_name'])
            continue
        else:
            result = database.find({'donor_name': name})
            if result.count() == 0:
                database.insert({'uuid': str(uuid.uuid4()), 'donor_name': name})
            else:
                print("Donor already exists, adding donations to existing donor.")
            break

    while True:
        try:
            amount = float(input(f"Enter a donation amount for {name} : "))
            if amount <= 0:
                print('Amount donated must be a positive number.')
            else:
                break
        except ValueError:
            print('Please enter a numerical value.')

    database.update({'donor_name': name}, {'$push': {'donations': amount}})

    cursor = database.find({'donor_name': name})
    for doc in cursor:
        print(generate_letter(doc))


def modify_donor(database):
    donor_uuid = ""
    while True:
        name = input("Enter a Full Name ('list' to show list of donors, 'q' to quit) > ")
        if name == 'q' or name == '':
            return
        elif name == 'list':
            cursor = database.find({})
            for doc in cursor:
                print(doc['donor_name'])
            continue
        else:
            result = database.find({'donor_name': name})
        if result.count() == 0:
            print("Donor not found.")
        else:
            for doc in result:
                print(f"Donor found: \n\tUUID: {doc['uuid']}\n\tDonor Name:{doc['donor_name']}")
                donor_uuid = doc['uuid']
            break

    while True:
        choice = (input("(D)elete donor, (R)ename donor, (Q)uit > ")).lower()
        if choice == 'q' or choice == '':
            return
        elif choice == 'd':
            try:
                doc = database.delete_one({'uuid': donor_uuid})
                print("Deleted count: ", doc.deleted_count)
                return
            except Exception as e:
                print(str(e))

        elif choice == 'r':
            try:
                name = input("New name > ")
                result = database.update_one({'uuid': donor_uuid}, {'$set':{'donor_name': name}})
                print("matched: ", result.matched_count)
                print("modified: ", result.modified_count)
            except Exception as e:
                print(str(e))
            return


def menu(menu_data):
    """
    Prints the main user menu & retrieves user selection.
    :param: a menu list, consisting of iterable with three values:
        [0]: text to be presented to user
        [1]: function that should be called for the menu item
        [2]: parameter that should be used in the function call, None if no parameter call needed
    :return: two values:
        1) the function corresponding to the user's selection, or None on a bad selection
        raises ValueError if choice is non-numeric
        2) a parameter that should be used with the fn call, None if no parameter needed
    """
    print("\nPlease choose one of the following options:")

    for index, menu_item in enumerate(menu_data):   # Prints the menu user text
        print(f"{index + 1}) {menu_item[0]}")

    choice = int(input("> ")) - 1

    if choice in range(len(menu_data)):                     # Ensure that option chosen is within menu range, this
        return menu_data[choice][1], menu_data[choice][2]   # handles choosing 0, which would return menu_data[-1][1]

    return None


if __name__ == "__main__":

    with login_database.login_mongodb_cloud() as client:
        db = client['dev']
        mdb_mailroom = db['mailroom']

        menu_functions = [
            ('Send a Thank You', send_thank_you_menu, mdb_mailroom),
            ('Print a report', print_donor_report, mdb_mailroom),
            ('Modify Donor', modify_donor, mdb_mailroom),
            #('Send letters to everyone', dl.send_letters_all, None),
            #('Make donation projections', make_projections, dl),
            ('Quit', exit, None),
        ]
        while True:
            try:
                menu_fn, param = menu(menu_functions)
                if param:
                    menu_fn(param)
                else:
                    menu_fn()
            except TypeError:
                continue
            except ValueError:
                continue
