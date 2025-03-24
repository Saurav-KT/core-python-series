"""parameterized decorator

create a decorator factory. A decorator factory is a function that returns a decorator.
This allows you to pass parameters to the decorator itself."""

def validate_log(log_type):
    def decorator(func):
        def inner(*args,**kwargs):
            # You can use the log_type parameter here
            if log_type=="error":
                print("Validating error log")
            elif log_type=="info":
                print("Validating info log")
            else:
                print("Unknown log type")

            # Call the original function
            return func(*args, **kwargs)
        return inner
    return decorator

@validate_log(log_type="error")
def collect_log(msg):
    print(f"Log collected:{msg}")

collect_log("something went wrong")

# Docorator without parameter

def validate_params(func):
    def inner(*args, **kwargs):
        # validate args
        for arg in args:
            if not isinstance(arg,(float, int)):
                raise ValueError(f"Invalid argument:{arg}. Expected a float or int.")

        for key,value in kwargs.items():
            if not isinstance(value,(float, int)):
                raise ValueError(f"Invalid argument:{key}={value}. Expected a float or int.")
        # If validation passes, call the original function
        return func(*args, **kwargs)
    return inner

@validate_params
def calculate(x: float,y:float):
    return x*y

print(calculate(2.5,5.3))