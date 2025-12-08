import asyncio


async def say_hello(t, msg):
    await asyncio.sleep(t)
    print(msg, end="")
    await say_name(2, "Denis")


async def say_name(t, name):
    await asyncio.sleep(t)
    print(name)
    await say_end("END")


async def say_end(msg):
    print(msg)


async def main():
    task1 = asyncio.create_task(say_hello(1, "Hello, "))

    await task1


asyncio.run(main())