import datetime
from enum import Enum

from constant.messages import ERROR_MESSAGE, SUCCESS_MESSAGE

class SuccessKeys(Enum):
    SUCCESS = SUCCESS_MESSAGE

class ErrorKeys(Enum):
    ERROR = ERROR_MESSAGE

def get_current_year():
    return datetime.datetime.now().year

CURRENT_YEAR = get_current_year()
