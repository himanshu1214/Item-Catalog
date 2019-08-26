from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Categories(Base):
    __tablename__ = 'category'
    name  = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        return {
        'name': self.name,
        'id': self.id
        }

class Items(Base):
    __tablename__='items'
    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    category_id =Column(Integer, ForeignKey('category.id'))
    category = relationship(Categories)

    @property
    def serialize(self):
        return {
        'name': self.name,
        'id': self.id,
        'description': self.description
        }

engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
