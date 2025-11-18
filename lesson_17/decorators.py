import datetime

def log_calls(func):

    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)

        print(f"[{timestamp}] -- Виклик функції '{func.__name__}' з аргументами: ({signature})")

        result = func(*args, **kwargs)

        print(f"[{timestamp}] -- Функція '{func.__name__}' повернула результат: {result!r}")

        return result

    return wrapper

@log_calls
def multiply(a, b):
    return a * b

print(f"Ім'я функції: {multiply.__name__}")
multiply(3, 4)


def handle_exceptions(exception_type=Exception, default_return=None):

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_type as e:
                print(f"--- Помилка у функції '{func.__name__}' ---")
                print(f"Був перехоплений виняток типу {type(e).__name__}: {e}")
                return default_return
        return wrapper

    return decorator

@handle_exceptions(default_return="Не вдалося обчислити")
def failing_function(x):
    return 10 / x

print(f"\nІм'я функції: {failing_function.__name__}")
result = failing_function(0)
print(f"Результат: {result}")