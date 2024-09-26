import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(
            f"Function '{func.__name__}'\nelapsed time: {end_time - start_time} seconds\n"
        )
        return result

    return wrapper


{}
