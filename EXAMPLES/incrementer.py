class Incrementer:
    def __init__(self, increment=1):
        self._increment = increment
        self._value = 0

    def __call__(self):
        self._value += self._increment

    @property
    def value(self):
        return self._value
    
if __name__ == "__main__":
    inc = Incrementer()
    inc()
    inc()
    inc()
    print(f"inc.value: {inc.value}")
    # blah()

def blah():
    print("Hello from blah()")

# blah()