import asyncio

async def set_future(fut, value):
    await asyncio.sleep(1)
    fut.set_result(value)

async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    await set_future(fut, "Hello")
    print(fut.result())
asyncio.run(main())