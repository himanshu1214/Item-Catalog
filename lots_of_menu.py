from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Categories, Base, Items

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#Category :1
category1 = Categories(name='Soccer')
session.add(category1)
session.commit()

item1 = Items(name='soccer balls', description='For playing outside and indoors',
category= category1)
session.add(item1)
session.commit()

#Category :2
category1 = Categories(name='Basketball')
session.add(category1)
session.commit()

#Category: 3
category1 = Categories(name='Baseball')
session.add(category1)
session.commit()

#Category: 4
category1 = Categories(name='Frisbee')
session.add(category1)
session.commit()

#Category: 5: SnowBoarding
category1 = Categories(name='SnowBoarding')
session.add(category1)
session.commit()

#item1
item1 = Items(name='Goggles', description='Darkbrown goggles for snowboarding',
category=category1)
session.add(item1)
session.commit()

#item2
item2 = Items(name='SnowBoarding', description='Great cheap Snobaords this \
cold weather', category=category1)
session.add(item2)
session.commit()

#Category: 6
category1 = Categories(name='Foosball')
session.add(category1)
session.commit()

#Category: 7
category1 = Categories(name='Skating')
session.add(category1)
session.commit()

#Category:8
category1 = Categories(name='Hockey')
session.add(category1)
session.commit()

print("items added")
