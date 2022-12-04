import database
from instruction import search_company, update_company, create_company, delete_company, list_all

MAIN_MENU = "Welcome to the Investor Program!\n\nMAIN MENU\n0 Exit\n1 CRUD operations\n2 Show top ten companies by " \
            "criteria "
CRUD_MENU = "CRUD MENU\n0 Back\n1 Create a company\n2 Read a company\n3 Update a company\n4 Delete a company\n5 List " \
            "all companies"
TOP_TEN_MENU = "TOP TEN MENU\n0 Back\n1 List by ND/EBITDA\n2 List by ROE\n3 List by ROA"
NICE_DAY = "\nHave a nice day!"
TYPING_SPEED = 90  # wpm
NOT_YET = "Not implemented!"


def main():
    while True:
        menu_input = input(f'\n{MAIN_MENU}\nEnter an option: ')
        match menu_input:
            case '1':
                crud_input = input(f'\n{CRUD_MENU}\nEnter an option: ')
                match crud_input:
                    case '0':
                        print(NICE_DAY)
                        exit()
                    case '1':
                        create_company()
                    case '2':
                        search_company()
                    case '3':
                        update_company()
                    case '4':
                        delete_company()
                    case '5':
                        list_all()
                    case _:
                        print(NOT_YET)
            case '2':
                ten_menu = input(f'{TOP_TEN_MENU}\nEnter an option: ')
                match ten_menu:
                    case '0':
                        print(NICE_DAY)
                        exit()
                    case '1':
                        print(NOT_YET)
                    case '2':
                        print(NOT_YET)
                    case '3':
                        print(NOT_YET)
                    case _:
                        print(NOT_YET)
            case '0':
                print(NICE_DAY)
                exit()
            case _:
                print('Invalid option!')


if __name__ == '__main__':
    database.main()
    main()
