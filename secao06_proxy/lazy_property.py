class LazyProperty:
    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__

    def __get__(self, obj, cls):
        if not obj:
            return None
        value = self.method(obj)
        setattr(obj, self.method_name, value)
        return value


class Test:
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        print(f'initializing self._resource wich is {self._resource}')
        self._resource = tuple(range(5))
        return self._resource


if __name__ == '__main__':
    t = Test()
    print(t.x)
    print(t.y)
    print(t.resource)
    print(t.resource)
