# coding: utf-8
from sqlalchemy import Boolean, Column, Float, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Room(Base):
    __tablename__ = 'room'

    room_id = Column(String, primary_key=True)
    room_size = Column(Integer, nullable=False)
    measurement_unit = Column(String, nullable=False)


class Airqualityproperty(Base):
    __tablename__ = 'airqualityproperties'

    room_id = Column(ForeignKey('room.room_id'), nullable=False)
    ventilator = Column(String, nullable=False)
    totalnumberofpeople = Column(Integer, nullable=False)
    co2 = Column(Float(53), nullable=False)
    co2measurementunit = Column(String, nullable=False)
    temperature = Column(Float(53), nullable=False)
    temperaturemeasurementunit = Column(String, nullable=False)
    humidity = Column(Float(53), nullable=False)
    humiditymeasurementunit = Column(String, nullable=False)
    time = Column(DateTime, primary_key=True)

    room = relationship('Room')


class Door(Base):
    __tablename__ = 'doors'

    door_id = Column(String, primary_key=True)
    room_id = Column(ForeignKey('room.room_id'), nullable=False)
    door_lock = Column(Boolean, nullable=False)
    connectsdoor = Column(String, nullable=False)
    time = Column(DateTime, nullable=False)

    room = relationship('Room')
    rooms = relationship('Room', secondary='roomtodoorrelations')


class Light(Base):
    __tablename__ = 'lights'

    room_id = Column(ForeignKey('room.room_id'), nullable=False)
    light_id = Column(String, nullable=False)
    turnon = Column(Boolean, nullable=False)
    energyconsumption = Column(Integer, nullable=False)
    energyconsumptionunit = Column(String, nullable=False)
    time = Column(DateTime, primary_key=True)

    room = relationship('Room')


class Ventilator(Base):
    __tablename__ = 'ventilators'

    room_id = Column(ForeignKey('room.room_id'), nullable=False)
    ventilator_id = Column(String, nullable=False)
    turnon = Column(Boolean, nullable=False)
    time = Column(DateTime, primary_key=True)

    room = relationship('Room')


class Window(Base):
    __tablename__ = 'windows'

    room_id = Column(ForeignKey('room.room_id'), nullable=False)
    window_id = Column(String, nullable=False)
    isopen = Column(Boolean, nullable=False)
    time = Column(DateTime, primary_key=True)

    room = relationship('Room')

class RoomToDoorRelations(Base):
    __tablename__ = 'roomtodoorrelations'

    door_id = Column(ForeignKey('doors.door_id'), primary_key=True, nullable=False)
    room_id = Column(ForeignKey('room.room_id'), primary_key=True,nullable=False)
    
    roomdoor = relationship('Room')
    roomsdoor = relationship('Door',overlaps="rooms")