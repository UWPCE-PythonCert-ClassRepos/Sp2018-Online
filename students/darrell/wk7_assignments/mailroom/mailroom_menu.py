from mailroom_class import Mailroom


mailroom = Mailroom()

def print_menu():  ## Your menu design here
    print(23 * "-", "Mailroom Main Menu", 23 * "-")
    print("1. Generate Report")
    print("2. List All Donors")
    print("3. List All Donations")
    print("q. Quit")
    print(66 * "-")

def process_result(result):
    print(f'\n{result}\n')


def start_menu():
    loop = True
    while loop:  ## While loop which will keep going until loop = False
        print_menu()  ## Displays menu
        choice = input("Enter your choice [1-2]: ")

        if choice == '1':
            process_result(mailroom.create_report())
        elif choice == '2':
            process_result(mailroom.list_donors())
        elif choice == '3':
            process_result(mailroom.list_donations())
        elif choice == 'q':
            print('\n===============\n'
                  '=== Goodbye ==='
                  '\n===============')
            break
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")


if __name__ == "__main__":

    # for k, v in initial_data.items():
    #     mailroom.donor_collection[k] = Donor(k, v['lname'], v['donations'])

    start_menu()
