import asyncio


def my_callback(*args, **kwargs):
    print(loop.is_running())
    print("Callback processed")
    loop.stop()


loop = asyncio.get_event_loop()
loop.call_later(3, my_callback, loop)
loop.run_forever()
print(loop.is_running())