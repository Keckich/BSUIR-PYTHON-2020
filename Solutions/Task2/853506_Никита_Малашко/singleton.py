class MetaSingleton(type):
    instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self.instances:
            self.instances[self] = super(MetaSingleton, self).__call__(*args, **kwargs)
        return self.instances[self]


class SingletonValue(metaclass=MetaSingleton):
    def __init__(self, *args):
        self.args = args

    def get(self):
        return self.args


if __name__ == '__main__':
    val1 = SingletonValue(4, 8)
    val2 = SingletonValue(9, 7)
    print(val1.get())
    print(val2.get())
