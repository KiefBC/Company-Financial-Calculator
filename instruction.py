import database

EMPTY_LINE = ''
COMPANY_NAME = '\nEnter company name: \n'
COMPANY_NUMBER = '\nEnter company number: \n'


def search_company():
    """
    Search for a company by ticker
    """
    c_query = input(f'{COMPANY_NAME}')
    # Grabbing the company name from the database
    company = database.session.query(database.CompanyDatabase).filter(
        database.CompanyDatabase.name.like(f'%{c_query}%')).all()
    if company:
        print(EMPTY_LINE)
        # Adding a counter to the company name to enumerate the list
        for count, c in enumerate(company):
            print(f'{count} {c.ticker} - {c.name}')
        n_query = input(f'{COMPANY_NUMBER}')
        selected_company = company[int(n_query)]
        # Grabbing the financial data from the database
        financial = database.session.query(database.FinancialDatabase).filter(
            database.FinancialDatabase.ticker == selected_company.ticker).first()
        # Calculating the financial ratios
        p_e = round(financial.market_price / financial.net_profit, 2)
        p_s = round(financial.market_price / financial.sales, 2)
        if financial.net_debt is None or financial.ebitda is None:
            nd_ebitda = None
        else:
            nd_ebitda = round(financial.net_debt / financial.ebitda, 2)
        roe = round(financial.net_profit / financial.equity, 2)
        roa = round(financial.net_profit / financial.assets, 2)
        l_a = round(financial.liabilities / financial.assets, 2)
        print(
            f'({selected_company.ticker}) {selected_company.name}\nP/E = {p_e}\nP/S = {p_s}\nND/EBITDA = {nd_ebitda}\nROE = {roe}\nROA = {roa}\nL/A = {l_a}')
    else:
        print('\nCompany not found!\n')


def list_all():
    """
    List all companies
    """
    print("\nCOMPANY LIST\n")
    companies = database.session.query(database.CompanyDatabase).all()
    for company in companies:
        print(company.ticker, company.name)

def top_10():
    """
    List the top 10 companies
    """
    print("\nTOP 10\n")
    companies = database.session.query(database.CompanyDatabase).limit(10).all()
    for company in companies:
        print(company.ticker, company.name)


def update_company():
    """
    Update a company
    """
    c_query = input(f'{COMPANY_NAME}')
    # Grabbing the company name from the database
    company = database.session.query(database.CompanyDatabase).filter(
        database.CompanyDatabase.name.like(f'%{c_query}%')).all()
    if company:
        print(EMPTY_LINE)
        # Adding a counter to the company name to enumerate the list
        for count, c in enumerate(company):
            print(f'{count} {c.ticker} - {c.name}')
        n_query = input(f'{COMPANY_NUMBER}')
        selected_company = company[int(n_query)]
        ebitda = float(input("Enter ebitda (in the format '987654321'):\n"))
        sales = float(input("Enter sales (in the format '987654321'):\n"))
        profit = float(input("Enter net profit (in the format '987654321'):\n"))
        market_price = float(input("Enter market price (in the format '987654321'): \n"))
        net_debt = float(input("Enter net debt (in the format '987654321'):\n"))
        assets = float(input("Enter assets (in the format '987654321'):\n"))
        equity = float(input("Enter equity (in the format '987654321'):\n"))
        cash_equivalents = float(input("Enter cash equivalents (in the format '987654321'):\n"))
        liabilities = float(input("Enter liabilities (in the format '987654321'):\n"))
        financial_dict = {'ebitda': ebitda, 'sales': sales, 'net_profit': profit,
                          'market_price': market_price, 'net_debt': net_debt, 'assets': assets, 'equity': equity,
                          'cash_equivalents': cash_equivalents, 'liabilities': liabilities}
        database.session.query(database.FinancialDatabase).filter(
            database.FinancialDatabase.ticker == selected_company.ticker).update(financial_dict)
        database.session.commit()
        print("\nCompany updated successfully!")
    else:
        print('\nCompany not found!')


def delete_company():
    """
    Delete a company
    """
    c_query = input(f'{COMPANY_NAME}')
    # Grabbing the company name from the database
    company = database.session.query(database.CompanyDatabase).filter(
        database.CompanyDatabase.name.like(f'%{c_query}%')).all()
    if company:
        print(EMPTY_LINE)
        # Adding a counter to the company name to enumerate the list
        for count, c in enumerate(company):
            print(f'{count} {c.ticker} - {c.name}')
        n_query = input(f'{COMPANY_NUMBER}')
        selected_company = company[int(n_query)]
        # Grabbing the financial data from the database
        financial = database.session.query(database.FinancialDatabase).filter(
            database.FinancialDatabase.ticker == selected_company.ticker).first()
        database.session.delete(financial)
        database.session.delete(selected_company)
        database.session.commit()
        print("\nCompany deleted successfully!")
    else:
        print('\nCompany not found!')


def add_entry(table, data) -> None:
    """
    Add a new entry to the database
    """
    for byte in data:
        for k, v in byte.items():
            if v == '':
                byte[k] = None

    for byte in data:
        database.session.add(table(**byte))
        database.session.commit()


def create_company():
    """
    Create a company
    """
    ticker = input("Enter ticker (in the format 'MOON'):\n")
    name = input("Enter company (in the format 'Moon Corp'):\n")
    sector = input('Enter industries (in the format "Technology"):\n')
    ebitda = float(input("Enter ebitda (in the format '987654321'):\n"))
    sales = float(input("Enter sales (in the format '987654321'):\n"))
    profit = float(input("Enter net profit (in the format '987654321'):\n"))
    market_price = float(input("Enter market price (in the format '987654321'): \n"))
    net_debt = float(input("Enter net debt (in the format '987654321'):\n"))
    assets = float(input("Enter assets (in the format '987654321'):\n"))
    equity = float(input("Enter equity (in the format '987654321'):\n"))
    cash_equivalents = float(input("Enter cash equivalents (in the format '987654321'):\n"))
    liabilities = float(input("Enter liabilities (in the format '987654321'):\n"))
    company_dict = {'ticker': ticker, 'name': name, 'sector': sector}
    financial_dict = {'ticker': ticker, 'ebitda': ebitda, 'sales': sales, 'net_profit': profit,
                      'market_price': market_price, 'net_debt': net_debt, 'assets': assets, 'equity': equity,
                      'cash_equivalents': cash_equivalents, 'liabilities': liabilities}
    database.add_entry(database.CompanyDatabase, [company_dict])
    database.add_entry(database.FinancialDatabase, [financial_dict])
    print("\nCompany created successfully!")


if __name__ == '__main__':
    print('One day it will make sense...')
    print('...but not today.')
