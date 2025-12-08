import threading

user_data = threading.local()

def process_data(user):
    user_data.user = user
    greet(user)
def greet(user):
    print(f"Hello, {user}, you data are processed")

threads = []

users = ["Alice", "Bob", "Ben"]
for user in users:
    t = threading.Thread(target=process_data, args = (user,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()