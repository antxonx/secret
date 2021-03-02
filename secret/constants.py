from enum import IntEnum, Enum

class OPTIONS(IntEnum):
    CREATE = 1
    READ = 2
    DELETE = 3
    EXIT = 99

class COMMANDS(Enum):
    BACK = "--back"
    EXIT = "--exit"
    END = "--end"
    def __str__(self):
        return str(self.value)