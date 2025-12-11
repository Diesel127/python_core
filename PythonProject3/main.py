import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
print(loop)
new_loop = asyncio.new_event_loop()
asyncio.set_event_loop(new_loop)
print(asyncio.get_event_loop())