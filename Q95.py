class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def info():
        print("This is a Counter class.")

Counter.increment()
Counter.increment()
print(f"Count: {Counter.count}")
Counter.info()
