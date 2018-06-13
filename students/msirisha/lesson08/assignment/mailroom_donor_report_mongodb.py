def print_donor_report(database):
    """
    Prints a formatted report on the donors with name, amount given, number of gifts, and average gift.
    :return: None
    """
    name_max = 30

    rpt_title = "Donor Name" + ' ' * (name_max - 9) + "| Total Given | Num Gifts | Average Gift"
    print(rpt_title)
    print("-" * len(rpt_title))

    cursor = database.find({})

    for doc in cursor:
        # print(f"UUID: {doc['uuid']} Name: {doc['name']} Donations: {doc['donations']}")
        print(f"{doc['donor_name']:{name_max}}  $ {sum(doc['donations']):>10.2f}" +
              f"   {len(doc['donations']):>9}  ${sum(doc['donations'])/len(doc['donations']):>12.2f}")