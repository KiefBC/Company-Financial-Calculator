import csv
from os.path import exists

from sqlalchemy import Column, String, create_engine, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///investor.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


def add_entry(table, data) -> None:
    """
    Add a new entry to the database
    """
    for byte in data:
        for k, v in byte.items():
            if v == '':
                byte[k] = None

    for byte in data:
        session.add(table(**byte))
        session.commit()


class CompanyDatabase(Base):
    __tablename__ = 'companies'

    ticker = Column(String, primary_key=True)
    name = Column(String)
    sector = Column(String)


class FinancialDatabase(Base):
    __tablename__ = 'financial'

    ticker = Column(String, primary_key=True)
    ebitda = Column(Float)
    sales = Column(Float)
    net_profit = Column(Float)
    market_price = Column(Float)
    net_debt = Column(Float)
    assets = Column(Float)
    equity = Column(Float)
    cash_equivalents = Column(Float)
    liabilities = Column(Float)


def main() -> None:
    # Create the database
    db_name = 'investor.db'
    if exists(db_name):
        print('Database already exists!')
        return  # Database is already made

    Base.metadata.create_all(engine)

    with open('companies.csv', 'r') as company_data, open('financial.csv', 'r') as fin_data:
        companies_content = list(csv.DictReader(company_data))
        financial_content = list(csv.DictReader(fin_data))

    # Add the data to the database
    add_entry(CompanyDatabase, companies_content)
    add_entry(FinancialDatabase, financial_content)
    session.commit()


if __name__ == '__main__':
    main()
    print('\nDatabase created successfully!\n')