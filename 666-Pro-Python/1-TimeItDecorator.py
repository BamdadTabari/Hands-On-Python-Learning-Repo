import time
from random import randrange

def timeit(func):
    """
    Decorator to measure the execution time of a function.
    :param func: The function to measure.
    :return: The function wrapped with timing functionality.
    """
    def wrapper(*args, **kwargs):
        # Capture the start time
        start_time = time.perf_counter()
        # Execute the function
        result = func(*args, **kwargs)
        # Capture the end time
        end_time = time.perf_counter()
        # Calculate the elapsed time
        elapsed_time = end_time - start_time
        
        # Print the elapsed time
        print(f"Execution time of {func.__name__}: {elapsed_time:.10f} seconds")
        
        return result
    
    return wrapper

# Example usage
@timeit
def example_function():
    # Code for the function
    var = 3 * randrange(0,1000000)
    return var

example_function()
