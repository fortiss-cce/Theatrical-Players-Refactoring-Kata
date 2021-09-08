from enum import Enum


class PlayType(str, Enum):
    TRAGEDY = "tragedy"
    COMEDY = "comedy"


class Play:
    def __init__(self, id: str, name: str, type: PlayType):
        self.id: str = id
        self.name: str = name
        self.type: PlayType = type