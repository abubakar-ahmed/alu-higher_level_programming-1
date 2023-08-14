#!/usr/bin/python3
"""
Script that lists all State objects containing the letter a
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    host, port = "localhost", 3306

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@{host}:{port}/{database}",
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()

