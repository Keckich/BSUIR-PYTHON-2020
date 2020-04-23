def cached(func):
    arg = {}

    def wrap(*args):
        res = func(*args)
        if arg.get(args) is res:
            return f'Result is {arg[args]}'
        else:
            arg.setdefault(args, res)
        return func(*args)
    return wrap


@cached
def example1(x, n, t):
    return (x ** n) + t

