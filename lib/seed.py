#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

# Clear our database before each new seed 
session.query(Game).delete()
session.commit()

# Faker to generate 50 random games
games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60) # Use random library to generate prices
    )
for i in range(50)]

session.bulk_save_objects(games)
session.commit()