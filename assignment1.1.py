def decorator(func_hello):
    def wrapper():
        print("Before the function is called.")
        func_hello()
        print("After the function is called.")
    return wrapper


@decorator
def func_hello():
    print("Hello, World!")

func_hello()


