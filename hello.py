def hello():
    print("hello, world!")

hello()

#write a decorator function logs input and output and times it to a function
def log(func):
    def wrapper(*args, **kwargs):
        print("Calling {} with arguments {}".format(func.__name__, args))
        result = func(*args, **kwargs)
        print("{} returned {}".format(func.__name__, result))
        return result
    return wrapper

#invoke decorator function using hello function
@log
def hello():
    print("Hello, World!")

hello()