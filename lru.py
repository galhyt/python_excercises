
def print_repr(func):
    def inner(self, *args, **kwargs):
        if len(args) > 0 and len(kwargs) > 0:
            ret = func(self, *args, **kwargs)
        elif len(args) > 0:
            ret = func(self, *args)
        elif len(kwargs) > 0:
            ret = func(self, **kwargs)
        else:
            ret = func(self)

        print(f"{self} {func.__name__} {args if len(args) > 0 else ''}")
        return ret
    return inner


class LruCache:
    length: int
    data: dict
    queue: []

    def __init__(self, length):
        """ Queue for lru cache implementation """
        self.length = length
        self.data = {}
        self.queue = length * [None]

    def __repr__(self):
        return ','.join(map(str, self.queue))

    @print_repr
    def push(self, key, value=True):
        """ Push to start of queue array """
        if key not in self.data:
            bobble_to = self.length - 1
            while self.queue[bobble_to] is None and bobble_to >= 0:
                bobble_to -= 1
        else:
            bobble_to = self.find_in_queue(key)-1

        self.bobble(bobble_to)
        self.queue[0] = key
        self.data[key] = value

    def find_in_queue(self, key):
        for i in range(len(self.queue)):
            if self.queue[i] == key:
                return i
        return None

    def bobble(self, bobble_to):
        """ Bobble queue elements """
        if self.queue[0] is None:
            return

        if bobble_to == self.length - 1 and self.queue[bobble_to] is not None:
            del self.data[self.queue[bobble_to]]
            self.queue[bobble_to] = None

        for i in range(min(bobble_to, self.length-2), -1, -1):
            self.queue[i+1] = self.queue[i]

    @print_repr
    def get(self, key):
        """ Get key's value """
        if key not in self.data:
            return None

        bobble_to = self.find_in_queue(key)-1
        self.bobble(bobble_to)
        self.queue[0] = key

        return self.data[key]


def lru_emulation(text_stream: str):
    for c in text_stream:
        res = lru.get(c)
        if res is None:
            # Get from data repository other than cache and push the result to cache
            lru.push(c)


lru = LruCache(5)
lru_emulation("ABCADEFGDGHIFJKLMNLMOPQRASGFHTYETEB")
