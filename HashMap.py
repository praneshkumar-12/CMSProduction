import ctypes

class HashMap:
    def __init__(self):
        self.array_size = 10
        self.array = (ctypes.py_object * self.array_size)()
        for idx in range(self.array_size):
            self.array[idx] = None

    def _hash(self, key):
        return hash(key) % self.array_size

    def put(self, key, value):
        index = self._hash(key)
        if self.array[index] is None:
            self.array[index] = []

        bucket = self.array[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.array[index]
        if bucket is not None:
            for k, v in bucket:
                if k == key:
                    return v

        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.array[index]
        if bucket is not None:
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    del bucket[i]
                    return

        raise KeyError(key)
