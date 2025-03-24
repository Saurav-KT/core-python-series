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

# collect_log("something went wrong")

# Decorator example-2

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

# print(calculate(2.5,5.3))

# Decorator example-3
import time
def calculate_execution_time(func):
    def wrapper(*args,**kwargs):
        start_time= time.time()
        result=func(*args, **kwargs)
        end_time =time.time()
        print(f"{func.__name__} took {end_time- start_time} seconds to run")
        return result
    return wrapper

@calculate_execution_time
def process_payment():
    print("payment has been processed successfully")

# process_payment()

# Decorator example-4
import time
import random

def retry_and_wait(max_retries, initial_wait_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            wait_time = initial_wait_time
            while retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    retries += 1
                    if retries == max_retries:
                        print(f"Max retries ({max_retries}) reached. Last error: {e}")
                        raise
                    print(f"Attempt {retries} failed. Retrying in {wait_time} seconds... Error: {e}")
                    time.sleep(wait_time)
                    wait_time *= 2  # Exponential backoff
        return wrapper
    return decorator

@retry_and_wait(max_retries=3, initial_wait_time=1)
def random_operation():
    if random.random() < 0.8:  # Changed to 80% failure rate for demonstration
        raise ValueError("Operation failed!")
    return "Operation succeeded!"

# Test the function
for i in range(5):  # Run multiple tests to see different outcomes
    try:
        print(f"\nTest {i+1}:")
        print(random_operation())
    except Exception as e:
        print(f"Final error: {e}")