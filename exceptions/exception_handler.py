from functools import wraps

from constant.messages import ERROR_MESSAGE, SUCCESS_MESSAGE
from constant.constants import ErrorKeys, SuccessKeys

class MovieNotFoundError(Exception):
    
    def __init__(self, message: str = "Movie not found"):
        self.message = message
        super().__init__(self.message)

    def handle_error(self):
        error_message = ERROR_MESSAGE.get(ErrorKeys.movie_not_found.name, self.message)
        return error_message

def handle_operation(success_key: SuccessKeys, error_key: ErrorKeys):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                result = func(self, *args, **kwargs)

                success_message = SUCCESS_MESSAGE.get(success_key.name, "Success message not found")
                print(success_message)  
                return result
            
            except MovieNotFoundError as e:
                error_message = e.handle_error()
                print(error_message) 
                raise e 
            
            except Exception as e:
                error_message = ERROR_MESSAGE.get(error_key.name, "Error message not found")
                print(error_message)  
                raise e  
        return wrapper
    return decorator


