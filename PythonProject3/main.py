import threading


def greet(name):
    print(f"Hello, {name}")


t = threading.Timer(5.0, greet, args=["Alice"])
t.start()
t.cancel()