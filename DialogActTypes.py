from enum import Enum

class DialogActTypes(Enum):
    UNDEFINED = 1
    HELLO = 2
    GOODBYE = 3
    INFORM = 4
    REQUEST = 5
    REQALTS = 6
    CONFIRM = 7
    DENY = 8
    REORDER = 9
    CHECK = 10
    REVISE = 11
    REPEAT = 12
    RETURN_CHECK = 13
    RECOMMEND = 14