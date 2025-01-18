class MovieNotFoundError(Exception):
    def __init__(self, message: str = "Movie was not found"):
        self.message = message
        super().__init__(self.message)



"""this decorator was to give centralized feedback with a enum key, but with it methods's types are modified """
# def handle_operation(success_key: SuccessKeys, error_key: ErrorKeys):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(self, *args, **kwargs):
#             try:
#                 result = func(self, *args, **kwargs)
#                 success_message = SUCCESS_MESSAGE[success_key.value]
#                 return success_message, result
#             except MovieNotFoundError as e:
#                 error_message = ERROR_MESSAGE[error_key.value]
#                 raise e
#             except Exception as e:
#                 error_message = ERROR_MESSAGE[error_key.value]
#                 raise ValueError(error_message)
#         return wrapper
#     return decorator