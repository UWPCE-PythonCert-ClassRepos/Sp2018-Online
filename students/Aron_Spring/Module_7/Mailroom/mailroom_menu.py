import Mailroom.mailroom_functions
import Mailroom.mailroom_reporting

mf=Mailroom.mailroom_functions
mr=Mailroom.mailroom_reporting

def start_menu():
    loop = True
    while loop:  ## While loop which will keep going until loop = False
        print_menu()  ## Displays menu
        choice = input("Enter your choice [1-3]: ")

        if choice == '1':
            process_result(mr.list_donations())
        elif choice == '2':
            process_result(mr.list_donors())
        elif choice == '3':
            process_result(mr.sum_donations())
        elif choice == 'q':
            print('\n===============\n'
                  '=== Exit ==='
                  '\n===============')
            break
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")


if __name__ == "__main__":
    start_menu()