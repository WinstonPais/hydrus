"""Models for Hydra Classes."""

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///database.db')

Base = declarative_base()


class Classes(Base):
    """Class for Hydra Classes."""

    __tablename__ = "classes"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        """Verbose object name."""
        return "<id='%s', name='%s'>" % (self.id, self.name)


class Property(Base):
    """Class for Hydra Instance Properties.

    >>> prop1 = Property('hasWeight')
    >>> prop2 = Property('hasCost')
    """

    __tablename__ = "property"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type_ = Column(String)  # Can be ABSTRACT or INSTANCE depending on which one it is

    def __repr__(self):
        """Verbose object name."""
        return "<id='%s', name='%s', type_='%s'>" % (self.id, self.name, self.type_)


class Instance(Base):
    """Class for Hydra Object/Resource."""

    __tablename__ = "instance"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type_ = Column(Integer, ForeignKey("classes.id"), nullable=True)

    def __repr__(self):
        """Verbose object name."""
        return "<id='%s', name='%s', type_='%s'>" % (self.id, self.name, self.type_.name)


class Terminal(Base):
    """Class for Hydra Supported Terminals."""

    __tablename__ = "terminal"

    id = Column(Integer, primary_key=True)
    value = Column(String)
    unit = Column(String)

    def __repr__(self):
        """Verbose object name."""
        return "<id='%s', value='%s', unit='%s'>" % (self.id, self.value, self.unit)


# class Supported_Property(Base):
#     """Class for Hydra Supported Properties."""
#
#     __tablename__ = "supported"
#
#     class_id = Column(Integer, ForeignKey("classes.id"))
#     prop_id = Column(Integer, ForeignKey("property.id"))
#
#     def __repr__(self):
#         """Verbose object name."""
#         return "<class_id='%s', prop_id='%s'>" % (self.class_id, self.prop_id)


class Graph(Base):
    """Graph triple contains subject, predicate, object."""

    __tablename__ = "graph"

    id = Column(Integer, primary_key=True)
    subject = Column(Integer)
    subject_type = Column(String)   # Can be CLASS or INSTANCE depending on which one it is
    predicate = Column(Integer, ForeignKey("property.id"))
    object_id = Column(Integer, nullable=True)
    object_type = Column(String)    # Can be CLASS or TERMINAL depending on which one it is

    def __repr__(self):
        """Verbose object name."""
        return "<subject='%s', predicate='%s', object_='%s'>" % (self.subject, self.predicate, self.object_id)


if __name__ == "__main__":
    print("Creating models....")
    Base.metadata.create_all(engine)
    print("Done")
