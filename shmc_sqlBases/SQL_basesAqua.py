"""
SQLAlchemy powered DB Bases: test, and production code.
by Sziller
"""

# imports for general Base handling START                                                   -   START   -
from sqlalchemy import Column, Integer, String, JSON, Float
from sqlalchemy.ext.declarative import declarative_base
# imports for general Base handling ENDED                                                   -   ENDED   -

# imports for local Base handling   START                                                   -   START   -
import time
import random as rnd
from cryptography import HashFunctions as HaFu
from shmc_basePackage import models
# imports for local Base handling   ENDED                                                   -   ENDED   -

Base = declarative_base()


# CLASS definitions START                                                                   -   START   -


class Process(Base):
    """=== Classname: Process(Base) ====================================================================================
    Class represents processes - these are time consuming happenings
    ============================================================================================== by Sziller ==="""
    __tablename__ = "processes"
    hash_hxstr: str = Column("hash_hxstr", String, primary_key=True)
    style: str = Column("style", String)
    start: str = Column("start", String)
    end: str = Column("end", String)

    def __init__(self,
                 style: str,
                 start: str,
                 end: str):
        self.style: str = style
        self.start: str = start
        self.end: str = end
        self.hash_hxstr: str = self.generate_id_hash()

    def generate_id_hash(self):
        """Function adds a unique ID to the row"""
        return HaFu.single_sha256_byte2byte(bytes(
            "{}{}".format(self.style, self.start),
            "utf-8")).hex()[:16]

    def return_as_dict(self):
        """=== Method name: return_as_dict =============================================================================
        Returns instance as a dictionary
        @return : dict - parameter: argument pairs in a dict
        ========================================================================================== by Sziller ==="""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def construct(cls, d_in):
        """=== Classmethod: construct ==================================================================================
        Input necessary class parameters to instantiate object of the class!
        @param d_in: dict - format data to instantiate new object
        @return: an instance of the class
        ========================================================================================== by Sziller ==="""
        return cls(**d_in)


class Event(Base):
    """=== Classname: Event(Base) ======================================================================================
    Class represents events - these are time consuming happenings
    ============================================================================================== by Sziller ==="""
    __tablename__ = "events"
    hash_hxstr: str = Column("hash_hxstr", String, primary_key=True)
    style: str = Column("style", String)
    at: str = Column("at", String)

    def __init__(self,
                 style: str,
                 at: str):
        self.style: str = style
        self.at: str = at
        self.hash_hxstr: str = self.generate_id_hash()

    def generate_id_hash(self):
        """Function adds a unique ID to the row"""
        return HaFu.single_sha256_byte2byte(bytes(
            "{}{}".format(self.style, self.at),
            "utf-8")).hex()[:16]

    def return_as_dict(self):
        """=== Method name: return_as_dict =============================================================================
        Returns instance as a dictionary
        @return : dict - parameter: argument pairs in a dict
        ========================================================================================== by Sziller ==="""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def construct(cls, d_in):
        """=== Classmethod: construct ==================================================================================
        Input necessary class parameters to instantiate object of the class!
        @param d_in: dict - format data to instantiate new object
        @return: an instance of the class
        ========================================================================================== by Sziller ==="""
        return cls(**d_in)


class Measurement(Base):
    """=== Classname: Record(Base) =====================================================================================
    Class represents general record who's data is to be stored and processed by the DB
    ============================================================================================== by Sziller ==="""
    __tablename__ = "measurements"
    mea_hash: str = Column("mea_hash", String, primary_key=True)
    mea_type: str = Column("mea_type", String)
    mea_loc: str = Column("mea_loc", String)
    mea_val: float = Column("mea_val", Float)
    mea_dim: str = Column("mea_dim", String)
    mea_time: str = Column("mea_time", String)
    timestamp: int = Column("timestamp", Integer)

    def __init__(self,
                 mea_type: str,
                 mea_loc: str,
                 mea_val: float,
                 mea_dim: str,
                 mea_time: str,
                 timestamp: int = 0
                 ):
        self.mea_type: str = mea_type
        self.mea_loc: str = mea_loc
        self.mea_val: float = mea_val
        self.mea_dim: str = mea_dim
        self.mea_time: str = mea_time
        self.timestamp: int = timestamp
        if self.timestamp == 0:
            self.timestamp = int(time.time())
        self.mea_hash: str = self.generate_id_hash()

    def generate_id_hash(self):
        """Function adds a unique ID to the row"""
        return HaFu.single_sha256_byte2byte(bytes(
            "{}{}".format(self.mea_type, self.timestamp),
            "utf-8")).hex()[:16]

    def return_as_dict(self):
        """=== Method name: return_as_dict =============================================================================
        Returns instance as a dictionary
        @return : dict - parameter: argument pairs in a dict
        ========================================================================================== by Sziller ==="""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def construct(cls, d_in):
        """=== Classmethod: construct ==================================================================================
        Input necessary class parameters to instantiate object of the class!
        @param d_in: dict - format data to instantiate new object
        @return: an instance of the class
        ========================================================================================== by Sziller ==="""
        return cls(**d_in)

    def __repr__(self):
        return "{:<16}-{:>12}: {:>6}{:<5}".format(self.mea_hash,
                                                  self.mea_loc,
                                                  self.mea_val,
                                                  self.mea_dim,
                                                  self.timestamp)

# CLASS definitions ENDED                                                                   -   ENDED   -
